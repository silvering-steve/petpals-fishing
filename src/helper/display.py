import pyautogui as py2


class Display:
    def __init__(self):
        self.white_pos, self.bait_pos = self.get_coordinates(py2.size())

    def get_coordinates(self, screen_size):

        match screen_size[0]:
            case 1920:
                white_pos = (10, 1070)
                bait_pos = (245, 1000)

            case 1600:
                white_pos = (10, 830)
                bait_pos = (195, 830)

            case 1366:
                white_pos = (10, 700)
                bait_pos = (160, 700)

            case 1360:
                white_pos = (10, 700)
                bait_pos = (160, 700)

            case _:
                raise "Resolution is not supported"

        return white_pos, bait_pos
