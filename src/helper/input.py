import time
from typing import Any

import pyautogui as py2

from PIL import Image

from src.models import model


class Clicker:
    @staticmethod
    def click(bait_pos: tuple | list[float]) -> None:
        x, y = (int(bait_pos[0] + 25), int(bait_pos[1] + 25))

        py2.moveTo(x=x, y=y)

        time.sleep(.1)

        py2.leftClick()

    @staticmethod
    def get_coordinate() -> tuple[bool, Any] | None:
        screen = py2.screenshot()

        return model(image=screen)
