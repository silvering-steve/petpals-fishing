import os
from typing import Tuple, Any

import wget
from ultralytics import YOLO


class Model:
    def __init__(self) -> None:
        if not os.path.exists("models/bubbles.onnx"):
            wget.download(
                url="https://silveringtrialstorage.blob.core.windows.net/trial-container/models/detection/onnx/bubbles.onnx",
                out="./models"
            )

        try:
            self.model = YOLO("models/bubbles.onnx", task="detect")

            print("Model loaded!")
        except:
            raise 'Error when loading model'

    def __call__(self, *args, **kwargs) -> tuple[bool, Any] | None:
        result = self.model(kwargs["image"], conf=0.82, verbose=False, imgsz=256)

        try:
            is_button = 1 in result[0].boxes.cls

            return is_button, result[0].boxes.xywh.tolist()
        except IndexError:
            return None

