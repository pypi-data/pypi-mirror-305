import time
import numpy as np

import typer
from typing_extensions import Annotated

import onnxruntime as ort
import onnxruntime_extensions

from yolo2onnx_extended.exporter import YOLO2ONNXExporter


def export_model(
    torch_model_path: str,
    num_classes: int,
    onnx_opset: int = 18,
    insert_image_cropping: bool = False,
    result_format: str = None,
    conf_threshold: float = 0.5,
    iou_threshold: float = 0.6,
    crop_percentages: tuple = None,
    image_shape: tuple = None,
):
    """
    Export a YOLO model to ONNX format with optional image cropping.
    Args:
        torch_model_path (str): Path to the PyTorch model file.
        num_classes (int): Number of classes in the model.
        onnx_opset (int, optional): ONNX opset version to use. Default is 18.
        insert_image_cropping (bool, optional): Whether to insert image cropping operation in the exported model. Default is False.
        result_format (str, optional): Format of the result. Default is None.
        conf_threshold (float, optional): Confidence threshold for the model. Default is 0.5.
        iou_threshold (float, optional): Intersection over Union (IoU) threshold for the model. Default is 0.6.
        crop_percentages (tuple, optional): Crop percentages for the image cropping operation. Default is None.
        image_shape (tuple, optional): Shape of the image for the image cropping operation. Default is None.
    Returns:
        None
    """

    # Set crop percentages and image shape for the image cropping operation if selected
    if insert_image_cropping:
        print("Inserting image cropping operation in the exported model")
        crop_percentages = crop_percentages
        image_shape = image_shape
    else:
        crop_percentages = None
        image_shape = None

    # Create the exporter
    exporter = YOLO2ONNXExporter(
        torch_model_path=torch_model_path,
        num_classes=num_classes,
        onnx_opset=onnx_opset,
        crop_pecentages=crop_percentages,  # insert image cropping in the exported model
        image_shape=image_shape,  # insert image cropping in the exported model
    )

    # Export the model with default parameters
    exporter.export_to_onnx_extensions(
        iou_threshold=iou_threshold,
        score_threshold=conf_threshold,
        result_as_image_format=result_format,
    )


def run_inference(
    onnx_model_path,
    test_image_path,
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
    result_format=None,
):
    session_options = ort.SessionOptions()

    # register onnxruntime_extensions custom ops library
    session_options.register_custom_ops_library(
        onnxruntime_extensions.get_library_path()
    )

    # Create the session
    session = ort.InferenceSession(
        str(onnx_model_path), providers=providers, sess_options=session_options
    )
    input_names = [i.name for i in session.get_inputs()]

    # Load the image
    st_image_load = time.time()
    image = np.frombuffer(open(test_image_path, "rb").read(), dtype=np.uint8)

    # print image shape considering as matrix, not stream buffer
    inp = {input_names[0]: image}
    print(
        f"Image loading time: {(loading_time := time.time() - st_image_load):.3f} seconds"
    )

    # Run the model
    print("Starting detection...")
    st_detection = time.time()
    model_output = (
        ["image_out"]
        if result_format is not None
        else ["nms_output_with_scaled_boxes_and_keypoints"]
    )
    st_detection = time.time()
    outputs = session.run(model_output, inp)[0]

    print(
        f"Detection time: {(detection_time := time.time() - st_detection):.3f} seconds"
    )

    print(f"Total inference time: {loading_time + detection_time:.3f} seconds")

    if result_format is not None:
        open(f"result.{result_format}", "wb").write(outputs)
        print(f"Detection results image stored in 'result.{result_format}'")
    else:
        print("Detection results:")
        print(outputs)


def yolo2onnx(
    path_to_model: str = typer.Argument(..., help="Filename of the model to export"),
    num_classes: int = typer.Argument(..., help="Number of classes in the model"),
    conf_threshold: float = typer.Option(
        0.5, help="Confidence score threshold for detections"
    ),
    iou_threshold: float = typer.Option(
        0.6, help="Intersection over union threshold for non-maximum suppression"
    ),
    onnx_opset: int = typer.Option(18, help="ONNX opset version"),
    result_as_image: bool = typer.Option(
        False, help="Return detections as Image instead of array"
    ),
    insert_image_cropping: bool = typer.Option(
        False, help="Insert image cropping operation in the exported onnx model"
    ),
    crop_percentages: Annotated[float, "crop_percentages"] = typer.Option(
        None, help="Crop percentages (h, w) for the image crop operation"
    ),
    image_shape: Annotated[int, "image_shape"] = typer.Option(
        None, help="Original image shape (h, w)"
    ),
    test_inference: bool = typer.Option(True, help="Run inference on a test image"),
    test_image_path: str = typer.Option(None, help="Path to the test image"),
    use_cuda: bool = typer.Option(False, help="Use CUDA for inference"),
):
    """
    Export a YOLO model to ONNX format with optional pre and post-processing steps.
    Args:
        path_to_model (str): Filename of the model to export.
        num_classes (int): Number of classes in the model.
        conf_threshold (float, optional): Confidence score threshold for detections. Defaults to 0.5.
        iou_threshold (float, optional): Intersection over union threshold for non-maximum suppression. Defaults to 0.6.
        onnx_opset (int, optional): ONNX opset version. Defaults to 18.
        result_as_image (bool, optional): Return detections as Image instead of array. Defaults to False.
        insert_image_cropping (bool, optional): Insert image cropping operation in the exported ONNX model. Defaults to False.
        crop_percentages (float, optional): Crop percentages (h, w) for the image crop operation. Defaults to None.
        image_shape (int, optional): Original image shape (h, w). Defaults to None.
        test_inference (bool, optional): Run inference on a test image. Defaults to True.
        test_image_path (str, optional): Path to the test image. Defaults to None.
        use_cuda (bool, optional): Use CUDA for inference. Defaults to False.
    Raises:
        typer.Exit: If required arguments for cropping are not provided.
        typer.Exit: If test_inference is True and test_image_path is not provided.
    """
    if insert_image_cropping:
        if crop_percentages is None or len(crop_percentages) != 2:
            typer.echo(
                "Error: Using cropping requires crop_percentages to be specified as a tuple or list of two elements"
            )
            raise typer.Exit()
        if image_shape is None or len(image_shape) != 2:
            typer.echo(
                "Error: Using cropping requires image_shape to be specified as a tuple or list of two elements"
            )
            raise typer.Exit()

    # Export the model
    export_model(
        torch_model_path=path_to_model,
        num_classes=num_classes,
        onnx_opset=onnx_opset,
        insert_image_cropping=insert_image_cropping,
        result_format="jpg" if result_as_image else None,
        conf_threshold=conf_threshold,
        iou_threshold=iou_threshold,
    )

    if test_inference:
        if not test_image_path:
            typer.echo(
                "Error: Test image path must be specified if test_inference is True"
            )
            raise typer.Exit()
        else:
            run_inference(
                onnx_model_path=f"{path_to_model.split('.pt')[0]}.with_pre_post_processing.onnx",
                test_image_path=test_image_path,
                providers=(
                    ["CPUExecutionProvider"]
                    if not use_cuda
                    else ["CUDAExecutionProvider"]
                ),
                result_format="jpg" if result_as_image else None,
            )
