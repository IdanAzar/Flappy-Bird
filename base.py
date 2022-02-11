import constants as c


class Base:
    VELOCITY = 5
    WIDTH = c.BASE_IMG.get_width()
    IMAGE = c.BASE_IMG

    def __init__(self, y):
        # set y cord of base image ( Y cord of each base image is the same)
        self.y = y

        # set x1 to be top left corner of first base image
        self.x1 = 0

        # set x2 to be top left corner of second base image that comes right after the first image
        self.x2 = self.WIDTH

    def move_base(self):
        # move 2 base images with same velocity
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        # check if one base image is out of the screen, so we will cycle it to be right after the other base image
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw_base(self, window):
        # draw first base image
        window.blit(self.IMAGE, (self.x1, self.y))
        # draw second base image
        window.blit(self.IMAGE, (self.x2, self.y))
