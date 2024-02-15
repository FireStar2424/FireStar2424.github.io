import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
gray = (50, 50, 50)  # Darker gray color
blue = (50, 153, 213)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('snek by firestar2424')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.Font("ARCADECLASSIC.ttf", 35)
footer_font = pygame.font.SysFont("bahnschrift", 20)

def Your_score(score):
    value = score_font.render("Your score is " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def title_screen():
    title = True

    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    title = False
                    break
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        dis.fill(gray)
        message("Welcome to Snek!", white, -50)
        message("Press 'S' to start or 'Q' to quit", white)
        message("firestar2424 2024", white, 220, footer_font)

        pygame.display.update()

    gameLoop()

def message(msg, color, y_displace=0, font=None):
    if font is None:
        font = font_style
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2 + y_displace))
    dis.blit(mesg, text_rect)

def gameLoop():
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    title_screen()

title_screen()
pygame.quit()
quit()
