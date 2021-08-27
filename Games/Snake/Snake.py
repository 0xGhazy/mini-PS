import pygame
import sys
import random
import os
import json

# init pygame object
pygame.init()

#------------------------------#
# Game's Options / Global Vars #
#------------------------------#

# reading game sittings
os.chdir(os.path.dirname(__file__))
content = ""
with open("sn_configuration.json", 'r') as f:
    content = json.load(f)

# game colors in rgb form
bg_color = tuple(content['bg_color'])
target_color = tuple(content['target_color'])
gm_ov_msg_color = tuple(content['game_over_message_color'])
snake_color = tuple(content['snake_color'])

# game window dimensions
width = content["screen_width"]
height = content["screen_height"]
game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption(("mini-PS: SNAKE GAME"))

clock = pygame.time.Clock()
snake_size = content["snake_size"]
sanke_speed = content["sanke_speed"]
message_font= pygame.font.SysFont('SOUNDER',30)
score_font =pygame.font.SysFont('SOUNDER',30)



#FUNCTIONS

def print_score(score):
    """ Display currant player score.
    Args:
        score ([int]): [feed numbers]
    """

    text = score_font.render(" Score : " + str(score), True, (255, 255, 255))
    # append the text to the top-right
    game_display.blit(text,[0,0])


def draw_snake (snake_size, snake_pixels):
    """ Drawing the snake in it's currant size.
    Args:
        snake_size ([int]):
        snake_pixels ([int]): snake area
    """

    for pixel in snake_pixels:
        pygame.draw.rect(game_display, snake_color, [pixel[0], pixel[1], snake_size, snake_size])


def _SnakeGameRun_():
    """  This function used to call thw game in the main application. """

    # flag vars
    game_over = False
    game_close = False

    # Put the snake in the middle of the window
    # using the previous global bars
    x = width / 2
    y = height / 2

    # Make snake movement paused in the start of the game.
    x_speed = 0
    y_speed = 0

    # Init snake size with 1 pixel
    snake_pixels = []
    snake_lenght = 1

    target_x = round(random.randrange(0 , width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0 , height - snake_size) / 10.0) * 10.0


    while not game_over:
        while game_close:
            game_display.fill(bg_color)
            game_over_message = message_font.render("GAME OVER! " + f"Your Score is: {str(snake_lenght-1)}", True, gm_ov_msg_color)
            message = message_font.render("         Press [N] for new game OR Press [Q] to quite game.", True, gm_ov_msg_color)
            game_display.blit(game_over_message, [width / 3, height / 3])
            game_display.blit(message, [width / 20, height / 2])
            pygame.display.update()

            # taking main options inputs/events from the player.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # if player prees [Q]
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # if player prees [n]
                    if event.key == pygame.K_n:
                        # calling the game again
                        _SnakeGameRun_()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
                pygame.quit()
                sys.exit

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x_speed = -snake_size
                   y_speed = 0
               if event.key == pygame.K_RIGHT:
                   x_speed =snake_size
                   y_speed = 0
               if event.key == pygame.K_UP:
                   x_speed = 0
                   y_speed = -snake_size
               if event.key == pygame.K_DOWN:
                   x_speed = 0
                   y_speed = snake_size
        # check if the player crashing borders.
        if x >= width or x < 0 or y > height or y < 0:
         game_close = True

        x += x_speed
        y += y_speed
        # Update bord.
        game_display.fill(bg_color)
        # draw the target in its position.
        pygame.draw.rect(game_display,target_color,[target_x, target_y, snake_size, snake_size])
        snake_pixels.append([x, y])

        # check if the snake eat
        if len(snake_pixels) > snake_lenght:
           del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
          if pixel == [x, y]:
            game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_lenght - 1)

        pygame.display.update()

        # check if the snake eat the target
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            # increasing snake kength.
            snake_lenght += 1

        clock.tick(sanke_speed)

    quit()



_SnakeGameRun_()