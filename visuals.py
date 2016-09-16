import pygame
from models import *
import random
bg = pygame.image.load("sprites/bg.jpg")
stone = pygame.image.load("sprites/stone.jpg")
brick = pygame.image.load("sprites/brick.jpg")
player_1 = pygame.image.load("sprites/hit1.png")
player_2 = pygame.image.load("sprites/hit1.png")
bomb = pygame.image.load("sprites/bomb.png")

class Visuals:

    gamefield = []
    player1 = None
    player2 = None
    for i in range(15):
        gamefield.append([0] * 13)

    @classmethod
    def game_init(cls):
        for i in range(15):
            for j in range(13):
                if i == 0 or i == 14 or j == 0 or j == 12 or (i % 2 == 0 and j % 2 == 0):
                    cls.gamefield[i][j] = Wall(x=i * 78, y=j * 78, image=stone, fix=True)
        # cls.player1 = Player(x=1 * 78, y=1 * 78, image=player_1, player_id=1)
        # cls.player2 = Player(x=13 * 78, y=11 * 78, image=player_2, player_id=2)
        for f, column in enumerate(cls.gamefield):
            for h, row in enumerate(column):
                if not (row != 0 or (f == 1 and h == 1) or (f == 13 and h == 11) or
                        (f == 2 and h == 1) or (f == 1 and h == 2) or (f == 12 and h == 11) or (f == 13 and h == 10)):
                    if random.choice([0, 1]):
                        cls.gamefield[f][h] = Wall(x=f * 78, y=h * 78, image=brick, fix=False)

    # @classmethod
    # def draw_gamefield(cls):
    #     game_display.blit(bg, (0, 0))
    #     for i, column in enumerate(cls.gamefield):
    #         for j, row in enumerate(column):
    #             if row != 0:
    #                 game_display.blit(row.image, (i * 78, j * 78))
