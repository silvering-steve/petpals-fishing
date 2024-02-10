class Display:
    def __init__(self, screen_size):
        match screen_size[0]:
            case 1920:
                self.bait_pos = (245, 1000)

            case 1600:
                self.bait_pos = (195, 830)

            case 1366:
                self.bait_pos = (160, 700)

            case 1360:
                self.bait_pos = (160, 700)

            case _:
                raise "Resolution is not supported"
