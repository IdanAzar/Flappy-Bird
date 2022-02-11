import pygame
import constants as c
import random


class Pipe:
    # space between 2 pipes
    GAP_PIPES = 200

    # setting pipe velocity on x dir
    PIPE_VELOCITY = 5

    def __init__(self, x):
        # pipe x cord
        self.x = x

        # set y cord to zero, and then we will random pipe y cord
        self.height = 0

        self.top = 0
        self.bottom = 0

        # load images for upsidedown pipe and vertical pipe
        self.top_pipe = pygame.transform.flip(c.PIPE_IMG, False, True)
        self.bot_pipe = c.PIPE_IMG

        # set flag for bird is passed between pipes
        self.is_passed = False

        # setting y cord for each pipe
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)

        # placing top pipe in correct position
        self.top = self.height - self.top_pipe.get_height()
        # placing the bottom pipe with gap between them
        self.bottom = self.height + self.GAP_PIPES

    def move_pipe(self):
        # pipe is moving in negative velocity
        self.x -= self.PIPE_VELOCITY

    def draw_pipes(self, window):
        window.blit(self.top_pipe, (self.x, self.top))
        window.blit(self.bot_pipe, (self.x, self.bottom))

    @staticmethod
    def get_mask(image):
        return pygame.mask.from_surface(image)

    def collide(self, game_bird):
        # getting mask for each image object to get the image pixels
        bird_mask = game_bird.get_mask()
        top_mask = self.get_mask(self.top_pipe)
        bot_mask = self.get_mask(self.bot_pipe)

        # calculating the offset between left corner of the bird to each pipe
        top_offset = (self.x - game_bird.x, self.top - round(game_bird.y))
        bot_offset = (self.x - game_bird.x, self.bottom - round(game_bird.y))

        # check point of collision with each pipe if point is exist
        bot_point = bird_mask.overlap(bot_mask, bot_offset)
        top_point = bird_mask.overlap(top_mask, top_offset)

        # check if point exist
        if top_point or bot_point:
            return True
        return False

    def data_nw(self):
        return self.height, self.bottom
