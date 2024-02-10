from typing import Tuple, Any

from ultralytics import YOLO


class Model:
    def __init__(self) -> None:
        self.model = YOLO("models/bubbles.onnx", task="detect")

    def __call__(self, *args, **kwargs) -> tuple[bool, Any] | None:
        result = self.model(kwargs["image"], conf=0.82, verbose=False, imgsz=256)

        try:
            is_button = 1 in result[0].boxes.cls

            return is_button, result[0].boxes.xywh.tolist()
        except IndexError:
            return None

