from ultralytics import YOLO


class Model:
    def __init__(self) -> None:
        self.model = YOLO("models/yolov8/best.pt")

    def __call__(self, *args, **kwargs) -> list[float] | None:
        result = self.model(kwargs["image"], conf=0.88, verbose=False)

        try:
            return result[0].boxes.xywh[0].tolist()
        except IndexError:
            return None
