from src.helper.display import Display
from src.models.models import Model
from src.helper.input import Clicker

import time
import keyboard

if __name__ == "__main__":
    model = Model()
    display = Display()

    for i in range(5):
        print(f"Bot start in {5 - i}")
        time.sleep(1)

    while not keyboard.is_pressed("q"):
        is_fishing, screen = Clicker.getscreen(display.white_pos)

        coordinate = model(image=screen)

        if all(is_fishing):
            Clicker.click(display.bait_pos)

        if coordinate is None:
            print("Point not detected")
        else:
            Clicker.click(coordinate)

            print(f"Point detected at {coordinate[0]} {coordinate[1]}")

            time.sleep(.7)
