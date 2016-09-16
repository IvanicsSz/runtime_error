import pygame
from models import *
import numpy
import random
from visuals import Visuals

pygame.init()
bg = pygame.image.load("sprites/bg.jpg")
stone = pygame.image.load("sprites/stone.jpg")
brick = pygame.image.load("sprites/brick.jpg")
player_1 = pygame.image.load("sprites/hit1.png")
player_2 = pygame.image.load("sprites/hit1.png")
bomb = pygame.image.load("sprites/bomb.png")

game_exit = False

game_display = pygame.display.set_mode((1170, 1014))
pygame.display.set_caption('BomberMan - Jungle ed.')

# gamefield = numpy.zeros((15, 13))
# gamefield = []
# for i in range(15):
#     gamefield.append([0]*13)


# def game_init():
#     for i in range(15):
#         for j in range(13):
#             if i == 0 or i == 14 or j == 0 or j == 12 or (i % 2 == 0 and j % 2 == 0):
#                 cls.gamefield[i][j] = Wall(x=i*78, y=j*78, image=stone, fix=True)
#     cls.gamefield[1][1] = Player(x=1*78, y=1*78, image=player_1, player_id=1)
#     cls.gamefield[13][11] = Player(x=13*78, y=11*78, image=player_2, player_id=2)
#     for f, column in enumerate(cls.gamefield):
#         for h, row in enumerate(column):
#             if not (row != 0 or (f == 2 and h == 1) or (f == 1 and h == 2) or (f == 12 and h == 11) or (f == 13 and h == 10)):
#                 if random.choice([0, 1]):
#                     cls.gamefield[f][h] = Wall(x=f*78, y=h*78, image=brick, fix=False)


def draw_gamefield():
    game_display.blit(bg, (0, 0))
    for i, column in enumerate(Visuals.gamefield):
        for j, row in enumerate(column):
            if row != 0:
                game_display.blit(row.image, (i*78, j*78))

Visuals.game_init()

while not game_exit:
    draw_gamefield()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True


pygame.quit()
