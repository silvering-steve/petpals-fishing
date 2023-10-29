import pyautogui as py2
from PIL import Image
import time


class Clicker:
    @staticmethod
    def click(x: float, y: float) -> None:
        x, y = (int(x + 25), int(y + 25))

        py2.moveTo(x=x, y=y)

        time.sleep(.1)

        py2.leftClick()

    @staticmethod
    def getscreen() -> (list[bool], Image):
        screen = py2.screenshot()

        r, g, b = screen.getpixel((10, 1070))
        cond = [r == 255, g == 255, b == 255]

        return cond, screen
