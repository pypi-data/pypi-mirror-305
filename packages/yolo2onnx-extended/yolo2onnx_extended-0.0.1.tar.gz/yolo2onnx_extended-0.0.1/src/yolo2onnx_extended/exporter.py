import shutil

from typing import List
import numpy as np

import ultralytics
import onnx
import onnxruntime as ort
from onnxruntime_extensions.tools.pre_post_processing import *


class YOLO2ONNXExporter:

    def __init__(
        self,
        torch_model_path: str,
        num_classes: int = 1,
        onnx_opset: int = 18,
        onnx_model_path: str = None,
    ):
        assert torch_model_path.endswith(".pt"), "The model should be a .pt file."

        self.torch_model_path = Path(torch_model_path)  # path to the torch model
        self.torch_model = self.load_torch_model()  # torch model
        self.task = (
            self.torch_model.task
        )  # task of the model: detect / classify / segment
        self.onnx_opset = onnx_opset  # ONNX opset version
        self.num_classes = num_classes  # number of classes in the model

        # if there is a raw onnx model already it will be loaded
        self.onnx_model_path = Path(onnx_model_path) if onnx_model_path else None
        self.onnx_model = (
            self.load_onnx_model(onnx_model_path) if onnx_model_path else None
        )  # onnx model

        # initialize pre and post-processing pipeline related variables
        self.pipeline = None  # pre and post-processing pipeline
        self.yolo_v8_or_later = False  # result transpose required for YoloV8 or later

    def load_torch_model(self):
        return ultralytics.YOLO(str(self.torch_model_path))  # load a pretrained model

    def load_onnx_model(self):
        return onnx.load(str(self.onnx_model_path.resolve(strict=True)))

    def export_to_raw_onnx(
            self,
            save_raw_onnx: bool = True,
            onnx_model_name: str = None,
            simplify: bool = False,
            dynamic: bool = False,
            nms: bool = False,
            quant_int8: bool = False,
            quant_half: bool = False,
        ):
            """
            Export the YOLO torch model to raw ONNX format.

            Args:
                save_raw_onnx (bool, optional): Whether to save the raw ONNX model. Defaults to True.
                onnx_model_name (str, optional): Name of the saved ONNX model. Defaults to None.
                simplify (bool, optional): Whether to simplify the exported ONNX model. Defaults to False.
                dynamic (bool, optional): Whether to export the model with dynamic shape support. Defaults to False.
                nms (bool, optional): Whether to enable non-maximum suppression in the exported ONNX model. Defaults to False.
                quant_int8 (bool, optional): Whether to quantize the exported ONNX model to int8 data type. Defaults to False.
                quant_half (bool, optional): Whether to quantize the exported ONNX model to float16 data type. Defaults to False.

            Returns:
                onnx_model: The exported ONNX model.
            """
            # export to onnx
            onnx_model = self.torch_model.export(
                format="onnx",
                opset=self.onnx_opset,
                simplify=simplify,
                dynamic=dynamic,
                nms=nms,
                int8=quant_int8,
                half=quant_half,
            )  # export the model to ONNX format
            assert onnx_model, "Failed to export yolo torch model to onnx"

            # save the raw model wiht onnx format if desired
            if save_raw_onnx:
                if onnx_model_name is not None:
                    shutil.move(self.torch_model_path.with_suffix(".onnx"), onnx_model_name)
                else:
                    onnx_model_name = self.torch_model_path.with_suffix(".onnx")
                self.onnx_model_path = Path(onnx_model_name)

            self.onnx_model = self.load_onnx_model()

            return onnx_model

    def add_pre_processing(
        self,
        input_shape: List[int] = None,
    ):

        # model = onnx.load(str(model_file.resolve(strict=True)))
        inputs = [create_named_value("image", onnx.TensorProto.UINT8, ["num_bytes"])]

        model_input_shape = self.onnx_model.graph.input[0].type.tensor_type.shape
        model_output_shape = self.onnx_model.graph.output[0].type.tensor_type.shape

        # We will use the input_shape to create the model if provided by user.
        if input_shape is not None:
            assert len(input_shape) == 2, "The input_shape should be [h, w]."
            w_in = input_shape[1]
            h_in = input_shape[0]
        else:
            assert model_input_shape.dim[-1].HasField(
                "dim_value"
            ) and model_input_shape.dim[-2].HasField(
                "dim_value"
            ), "please provide input_shape in the command args."

            w_in = model_input_shape.dim[-1].dim_value
            h_in = model_input_shape.dim[-2].dim_value

        # Yolov5(v3,v7) has an output of shape (batchSize, 25200, 85) (Num classes + box[x,y,w,h] + confidence[c])
        # Yolov8 has an output of shape (batchSize, 84,  8400) (Num classes + box[x,y,w,h])
        # https://github.com/ultralytics/ultralytics/blob/e5cb35edfc3bbc9d7d7db8a6042778a751f0e39e/examples/YOLOv8-CPP-Inference/inference.cpp#L31-L33
        # We always want the box info to be the last dim for each of iteration.
        # For new variants like YoloV8, we need to add an transpose op to permute output back.
        output_shape = [
            (
                model_output_shape.dim[i].dim_value
                if model_output_shape.dim[i].HasField("dim_value")
                else -1
            )
            for i in [-2, -1]
        ]
        if output_shape[0] != -1 and output_shape[1] != -1:
            self.yolo_v8_or_later = output_shape[0] < output_shape[1]
        else:
            assert (
                len(self.onnx_model.graph.input) == 1
            ), "Doesn't support adding pre and post-processing for multi-inputs model."
            try:
                import onnxruntime
            except ImportError:
                raise ImportError(
                    """Please install onnxruntime and numpy to run this script. eg 'pip install onnxruntime numpy'.
    Because we need to execute the model to determine the output shape in order to add the correct post-processing"""
                )

            # Generate a random input to run the model and infer the output shape.
            session = onnxruntime.InferenceSession(
                self.onnx_model, providers=["CPUExecutionProvider"]
            )  # TODO: Check if correct, else str(onnx_model_path)
            input_name = session.get_inputs()[0].name
            input_type = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[
                self.onnx_model.graph.input[0].type.tensor_type.elem_type
            ]
            inp = {
                input_name: np.random.rand(1, 3, h_in, w_in).astype(dtype=input_type)
            }
            outputs = session.run(None, inp)[0]
            assert (
                len(outputs.shape) == 3 and outputs.shape[0] == 1
            ), "shape of the first model output is not (1, n, m)"
            if outputs.shape[1] < outputs.shape[2]:
                self.yolo_v8_or_later = True
            assert (
                self.num_classes + 4 == outputs.shape[2]
                or self.num_classes + 5 == outputs.shape[2]
            ), "The output shape is neither (1, num_boxes, num_classes+4(reg)) nor (1, num_boxes, num_classes+5(reg+obj))"

        self.pipeline = PrePostProcessor(inputs, self.onnx_opset)
        # precess steps are responsible for converting any jpg/png image to CHW BGR float32 tensor
        # jpg-->BGR(Image Tensor)-->Resize (scaled Image)-->LetterBox (Fix sized Image)-->(from HWC to)CHW-->float32-->1CHW
        self.pipeline.add_pre_processing(
            [
                ConvertImageToBGR(),  # jpg/png image to BGR in HWC layout
                # Resize an arbitrary sized image to a fixed size in not_larger policy
                Resize((h_in, w_in), policy="not_larger"),
                LetterBox(
                    target_shape=(h_in, w_in)
                ),  # padding or cropping the image to (h_in, w_in)
                ChannelsLastToChannelsFirst(),  # HWC to CHW
                ImageBytesToFloat(),  # Convert to float in range 0..1
                Unsqueeze([0]),  # add batch, CHW --> 1CHW
            ]
        )

    def add_post_processing_classification(self, argmax_output: bool = True):
        if self.onnx_model.graph.node[-1].op_type != "Softmax":
            self.pipeline.add_post_processing([Softmax()])

        # Get the class with the highest confidence. e.g.,: [0.1, 0.2, 0.7] -> 2
        if argmax_output:
            self.pipeline.add_post_processing([ArgMax(axis=1)])

    def add_post_processing_object_detection(self, result_as_image_format: str = None):
        # NMS and drawing boxes
        post_processing_steps = [
            Squeeze([0]),  # - Squeeze to remove batch dimension
        ]

        if self.yolo_v8_or_later:
            post_processing_steps += [
                Transpose([1, 0]),  # transpose to (num_boxes, box+scores)
                # split  elements into the box and scores for the classes. no confidence value to apply to scores
                Split(num_outputs=2, axis=-1, splits=[4, self.num_classes]),
            ]
        else:
            post_processing_steps += [
                # Split bounding box from confidence and scores for each class
                # Apply confidence to the scores.
                SplitOutBoxAndScoreWithConf(num_classes=self.num_classes),
            ]

        post_processing_steps += [
            SelectBestBoundingBoxesByNMS(),  # pick best bounding boxes with NonMaxSuppression
            # Scale bounding box coords back to original image
            (
                ScaleNMSBoundingBoxesAndKeyPoints(name="ScaleBoundingBoxes"),
                [
                    # A connection from original image to ScaleBoundingBoxes
                    # A connection from the resized image to ScaleBoundingBoxes
                    # A connection from the LetterBoxed image to ScaleBoundingBoxes
                    # We can use the three image to calculate the scale factor and offset.
                    # With scale and offset, we can scale the bounding box back to the original image.
                    utils.IoMapEntry(
                        "ConvertImageToBGR", producer_idx=0, consumer_idx=1
                    ),
                    utils.IoMapEntry("Resize", producer_idx=0, consumer_idx=2),
                    utils.IoMapEntry("LetterBox", producer_idx=0, consumer_idx=3),
                ],
            ),
        ]

        if result_as_image_format is not None:
            post_processing_steps += [
                # DrawBoundingBoxes on the original image
                # Model imported from pytorch has CENTER_XYWH format
                # two mode for how to color box,
                #   1. colour_by_classes=True, (colour_by_classes), 2. colour_by_classes=False,(colour_by_confidence)
                (
                    DrawBoundingBoxes(
                        mode="CENTER_XYWH",
                        num_classes=self.num_classes,
                        colour_by_classes=True,
                    ),
                    [
                        utils.IoMapEntry(
                            "ConvertImageToBGR", producer_idx=0, consumer_idx=0
                        ),
                        utils.IoMapEntry(
                            "ScaleBoundingBoxes", producer_idx=0, consumer_idx=1
                        ),
                    ],
                ),
                # Encode to jpg/png
                ConvertBGRToImage(image_format=result_as_image_format),
            ]

        self.pipeline.add_post_processing(post_processing_steps)

    def add_post_processing_segmentation(self, result_as_image_format: str = None):
        # NMS and drawing boxes
        post_processing_steps = [
            Squeeze([0]),  # - Squeeze to remove batch dimension
        ]

        if self.yolo_v8_or_later:
            post_processing_steps += [
                Transpose([1, 0]),  # transpose to (num_boxes, box+scores)
                # split  elements into the box and scores for the classes. no confidence value to apply to scores
                Split(num_outputs=3, axis=-1, splits=[4, self.num_classes, 32]),
            ]
        else:
            post_processing_steps += [
                # Split bounding box from confidence and scores for each class
                # Apply confidence to the scores.
                SplitOutBoxAndScoreWithConf(num_classes=self.num_classes),
            ]

        post_processing_steps += [
            SelectBestBoundingBoxesByNMS(
                has_mask_data=True
            ),  # pick best bounding boxes with NonMaxSuppression
            # Scale bounding box coords back to original image
            (
                ScaleNMSBoundingBoxesAndKeyPoints(num_key_points=16),
                [
                    # A connection from original image to ScaleBoundingBoxes
                    # A connection from the resized image to ScaleBoundingBoxes
                    # A connection from the LetterBoxed image to ScaleBoundingBoxes
                    # We can use the three image to calculate the scale factor and offset.
                    # With scale and offset, we can scale the bounding box back to the original image.
                    utils.IoMapEntry(
                        "ConvertImageToBGR", producer_idx=0, consumer_idx=1
                    ),
                    utils.IoMapEntry("Resize", producer_idx=0, consumer_idx=2),
                    utils.IoMapEntry("LetterBox", producer_idx=0, consumer_idx=3),
                ],
            ),
        ]
        if result_as_image_format is not None:
            post_processing_steps += [
                # DrawBoundingBoxes on the original image
                # Model imported from pytorch has CENTER_XYWH format
                # two mode for how to color box,
                #   1. colour_by_classes=True, (colour_by_classes), 2. colour_by_classes=False,(colour_by_confidence)
                Split(
                    num_outputs=2,
                    axis=-1,
                    splits=[6, 32],
                    name="SplitScaledBoxesAndKeypoints",
                ),
                (
                    DrawBoundingBoxes(
                        mode="CENTER_XYWH",
                        num_classes=self.num_classes,
                        colour_by_classes=True,
                    ),
                    [
                        utils.IoMapEntry(
                            "ConvertImageToBGR", producer_idx=0, consumer_idx=0
                        ),
                        utils.IoMapEntry(
                            "SplitScaledBoxesAndKeypoints",
                            producer_idx=0,
                            consumer_idx=1,
                        ),
                    ],
                ),
                # Encode to jpg/png
                ConvertBGRToImage(image_format=result_as_image_format),
            ]

        self.pipeline.add_post_processing(post_processing_steps)

    def add_post_processing(
        self, clf_argmax_output: bool = True, result_as_image_format: str = None
    ):

        # add post-processing steps depending on the model type
        if self.task == "classify":
            self.add_post_processing_classification(argmax_output=clf_argmax_output)
        elif self.task == "detect":
            self.add_post_processing_object_detection(result_as_image_format)
        elif self.task == "segment":
            self.add_post_processing_segmentation(result_as_image_format)

    def export_to_onnx_extensions(
            self,
            onnx_model_name: str = None,
            save_raw_onnx_model=True,
            input_shape: List[int] = None,
            clf_argmax_output: bool = True,
            result_as_image_format: str = None,
        ):
            """
            Export the model to ONNX format with pre and post-processing steps.

            Args:
                onnx_model_name (str, optional): Name of the ONNX model file. Defaults to None.
                save_raw_onnx_model (bool, optional): Whether to save the raw ONNX model. Defaults to True.
                input_shape (List[int], optional): Shape of the input. Defaults to None.
                clf_argmax_output (bool, optional): Whether to apply argmax to classifier output. Defaults to True.
                result_as_image_format (str, optional): Format of the result as an image. Defaults to None.

            Returns:
                onnx_model_with_pre_post_processing: The ONNX model with pre and post-processing steps.
            """

            # export the model to onnx format (raw, without pre and post-processing steps)
            if self.onnx_model is None:
                self.export_to_raw_onnx(
                    save_raw_onnx=save_raw_onnx_model, onnx_model_name=onnx_model_name
                )

            # add pre-processing steps
            self.add_pre_processing(input_shape=input_shape)

            # add post-processing steps
            self.add_post_processing(
                clf_argmax_output=clf_argmax_output,
                result_as_image_format=result_as_image_format,
            )

            # save the model with pre and post-processing steps
            onnx_model_with_pre_post_processing = self.pipeline.run(self.onnx_model)
            # run shape inferencing to validate the new model. shape inferencing will fail if any of the new node
            # types or shapes are incorrect. infer_shapes returns a copy of the model with ValueInfo populated,
            # but we ignore that and save new_model as it is smaller due to not containing the inferred shape information.
            _ = onnx.shape_inference.infer_shapes(
                onnx_model_with_pre_post_processing, strict_mode=True
            )

            output_file = self.onnx_model_path.with_suffix(
                suffix=".with_pre_post_processing.onnx"
            )
            onnx.save_model(onnx_model_with_pre_post_processing, str(output_file.resolve()))

            return onnx_model_with_pre_post_processing
