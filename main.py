from src.helper import object_coordinate
from src.helper.input import Clicker

import time
import keyboard

if __name__ == "__main__":
    for i in range(5):
        print(f"Bot start in {5 - i}")
        time.sleep(1)

    while not keyboard.is_pressed("q"):
        is_fishing, coordinate = Clicker.get_coordinate()

        if is_fishing:
            Clicker.click(object_coordinate.bait_pos)

        if len(coordinate) == 0:
            print("Point not detected")
        else:
            Clicker.click(coordinate[0])

            print(f"Point detected at {coordinate[0][0]} {coordinate[0][1]}")

            time.sleep(.7)
