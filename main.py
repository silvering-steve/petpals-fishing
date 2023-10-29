from src.models.models import Model
from src.helper.input import Clicker

import time
import keyboard

if __name__ == "__main__":
    model = Model()

    for i in range(5):
        print(f"Bot start in {5 - i}")
        time.sleep(1)

    while not keyboard.is_pressed("q"):
        is_fishing, screen = Clicker.getscreen()

        coordinate = model(image=screen)

        if all(is_fishing):
            Clicker.click(245, 1000)

        if coordinate is None:
            print("Point not detected")
        else:
            x, y = coordinate[0], coordinate[1]

            Clicker.click(x, y)

            print(f"Point detected at {x} {y}")

            time.sleep(.7)
