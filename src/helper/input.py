import pyautogui as py2
from PIL import Image
import time


class Clicker:
    @staticmethod
    def click(bait_pos: tuple | list[float]) -> None:
        x, y = (int(bait_pos[0] + 25), int(bait_pos[1] + 25))

        py2.moveTo(x=x, y=y)

        time.sleep(.1)

        py2.leftClick()

    @staticmethod
    def getscreen(white_pos: tuple) -> (list[bool], Image):
        screen = py2.screenshot()

        r, g, b = screen.getpixel(white_pos)
        cond = [r == 255, g == 255, b == 255]

        return cond, screen
