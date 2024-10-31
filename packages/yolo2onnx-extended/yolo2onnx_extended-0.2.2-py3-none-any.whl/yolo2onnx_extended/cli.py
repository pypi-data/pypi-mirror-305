import typer

from .yolo2onnx import yolo2onnx

app = typer.Typer()
app.command()(yolo2onnx)


if __name__ == "__main__":
    app()