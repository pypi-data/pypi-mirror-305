# Exporting YOLO models to ONNX with embedded pre and post processing

This repository contains the code to export Yolo models to ONNX format using the runtime extensions to **add pre and post processing** to the exported ONNX.

Models supported:

* [X] YOLOv8 Classification
* [X] YOLOv8 Object Detection
* [X] YOLOv8 Segmentation.
  * [ ] Processing of resulting box coordinates only covered. Segmentation polygon not supported yet

## Python Installation

* [PyTorch](https://pytorch.org/get-started/locally/): `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
* [Ultralyics](https://docs.ultralytics.com/quickstart/): `pip install ultralytics`
* [ONNX Runtime](https://onnxruntime.ai/docs/install/):
  * CPU: `pip install onnxruntime`
  * GPU (CUDA 11.8): `pip install onnxruntime-gpu`
* [ONNX Runtime Extensions](https://pytorch.org/get-started/locally/): `pip install onnxruntime-extensions`

## Use of exported model in other platforms (C/C#/C++/JavaScript/Android/iOS)

ONNX packages need to be installed. Check the supported versions for the platform you are using.

* ONNX Runtime installations for other platforms can be found in the [documentation](https://onnxruntime.ai/docs/install/).
* ONNX Extensions installations can be found in the [documentation](https://pytorch.org/get-started/locally/).

**[Inference install table for all languagues](Be aware of the supported versions of the extensions.)**

## Useful resources and Ideas

* [API - Python API documentation (onnxruntime.ai)](https://onnxruntime.ai/docs/api/python/api_summary.html)
* CUDA Optimization: [NVIDIA - CUDA | onnxruntime](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html)
* Model Quantization with ONNX
* ONNX Model Visualizer: [Netron](https://netron.app/)
* Processing Segmentation YOLOV8 ONNX: https://github.com/ibaiGorordo/ONNX-YOLOv8-Instance-Segmentation/

## Inference Benchmarks

* **CPU** (Intel(R) Core(TM) i7-10850H CPU @ 2.70GHz  6 cores, 12 virtual):
  * Object Detection `0.35 secs` per image
* **GPU** (NVIDIA Quadro T2000 with Max-Q Design):
  * Object Detection:  `4 - 5 secs` for first image. `0.068` for rest of images
