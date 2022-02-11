import pygame
from Neural_Network import NeuralNetwork
import constants as c


class Bird:
    # load bird images
    FRAMES = c.BIRD_IMGS
    # max limit rotation for flapping the bird
    MAX_ROTATION = 25
    # how much do we want to rotate the bird each frame
    ROT_VEL = 20
    # how much time we see each frame
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        # object cords on screen
        self.x = x
        self.y = y
        self.tilt = 0
        self.velocity = 0
        self.tick_count = 0
        self.prev_height = self.y
        self.count_img = 0
        self.img = self.FRAMES[0]
        self.brain = NeuralNetwork()

    def bird_jump(self):
        self.velocity = c.VEL_JUMP
        self.tick_count = 0
        self.prev_height = self.y

    def bird_move(self):
        self.tick_count += 1

        # calculating the distance that the bird move (delta X = V0 * t +  0.5 * g * t**2)
        distance = self.velocity * self.tick_count + (0.5 * c.GRAVITY) * self.tick_count ** 2

        # we don't want to let the bird increase the distance more than 16 pixels
        if distance >= c.MAX_DISTANCE:
            distance = c.MAX_DISTANCE

        # if distance is less than zero we want to increase a bit the bird distance movement
        if distance < 0:
            distance -= c.MIN_DISTANCE

        self.y = self.y + distance

        # update bird tilt rotation
        if distance < 0 or self.y < self.prev_height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw_bird(self, window):
        self.count_img += 1

        # draw base on time bird wings according to animation time display (wings movement)
        if self.count_img < self.ANIMATION_TIME:
            self.img = self.FRAMES[0]
        elif self.count_img < self.ANIMATION_TIME * 2:
            self.img = self.FRAMES[1]
        elif self.count_img < self.ANIMATION_TIME * 3:
            self.img = self.FRAMES[2]
        elif self.count_img < self.ANIMATION_TIME * 4:
            self.img = self.FRAMES[1]
        elif self.count_img < self.ANIMATION_TIME * 4 + 1:
            self.img = self.FRAMES[0]
            self.count_img = 0

        # while downfall bird wings are flat
        if self.tilt <= -80:
            self.img = self.FRAMES[1]
            self.count_img = self.ANIMATION_TIME * 2  # starting from frame 2 to save the order of frames

        # rotate bird image
        rotate_image = pygame.transform.rotate(self.img, self.tilt)
        new_img_rect = rotate_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)

        # draw on screen
        window.blit(rotate_image, new_img_rect)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def bird_hit_ground(self):
        return self.y + self.img.get_height() >= c.BASE_START_POS

    def bird_flew_away(self):
        return self.y < 0

    def use_logic(self, data_pipe):
        top_pipe_dis = abs(self.y - data_pipe[0])
        bot_pipe_dis = abs(self.y - data_pipe[1])
        make_call = self.brain.calculate([top_pipe_dis, bot_pipe_dis, self.y])
        if make_call[0] > make_call[1]:
            self.bird_jump()
