import pyautogui as py2
from PIL import Image


class Clicker:
    @staticmethod
    def click(x: float, y: float) -> None:
        x, y = (int(x + 25), int(y + 25))

        py2.click(x=x, y=y)

    @staticmethod
    def getscreen() -> (list[bool], Image):
        screen = py2.screenshot()

        r, g, b = screen.getpixel((10, 1070))
        cond = [r == 255, g == 255, b == 255]

        return cond, screen
