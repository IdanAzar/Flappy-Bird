import pygame
import constants as c
import bird
import pipe
import base


def initialize_window():
    # creating screen
    window = pygame.display.set_mode(c.SCREEN_SIZE)

    # name the screen
    pygame.display.set_caption(' flappy bird: BY Idan Azar :) ')

    return window


def draw_objects_on_screen(window, game_bird, pipes, game_base, score):
    # draw background image
    window.blit(c.BG_IMG, (0, 0))

    # draw all pipes
    for frame_pipe in pipes:
        frame_pipe.draw_pipes(window)

    # draw base image
    game_base.draw_base(window)

    # draw all bird image
    game_bird.draw_bird(window)

    # draw score info
    txt_info = c.STATS_FONT.render("Score: " + str(score), 1, (255, 102, 153))
    window.blit(txt_info, (c.SCREEN_WIDTH - 10 - txt_info.get_width(), 10))

    # update window
    pygame.display.update()


def game():
    # creating window
    pygame.init()
    window = initialize_window()

    # creating initial objects on screen
    game_bird = bird.Bird(*c.BIRD_START_POS)
    game_base = base.Base(c.BASE_START_POS)
    pipes = [pipe.Pipe(c.PIPE_START_POS)]

    # init score for game
    game_score = 0

    # flag for game loop!
    game_run = True

    # creating 60 FPS clock
    clock = pygame.time.Clock()

    # game loop
    while game_run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_bird.bird_jump()

        game_bird.bird_move()

        # check if bird hit the ground (game over)
        if game_bird.bird_hit_ground() or game_bird.bird_flew_away():
            game_run = False  # to do

        # creating list of pipe that will be removed from pipes list after scan pipes list
        pipes_to_remove = []

        # at the start we don't want to create new pipe until the bird pass one
        add_new_pipe = False

        for game_pipe in pipes:
            # check for colliding bird and pipe
            if game_pipe.collide(game_bird):
                # game ends
                game_run = False
                break

            # check when pipe should be removed when it passed the window
            if game_pipe.x + game_pipe.top_pipe.get_width() < 0:
                pipes_to_remove.append(game_pipe)

            # check if bird passed the current pipe and update if we need to change the score
            if not game_pipe.is_passed and game_pipe.x < game_bird.x:
                game_pipe.is_passed = True
                add_new_pipe = True

            # move pipe cords
            game_pipe.move_pipe()

        # update score and generate new pipe
        if add_new_pipe:
            game_score += 1
            pipes.append(pipe.Pipe(c.PIPE_MID_POS))

        # remove all pipes that pass the window from pipes list
        for remove_pipe in pipes_to_remove:
            pipes.remove(remove_pipe)

        # move base cords
        game_base.move_base()

        # draw all objects and update window
        draw_objects_on_screen(window, game_bird, pipes, game_base, game_score)

    pygame.quit()


def main():
    game()


if __name__ == '__main__':
    main()
