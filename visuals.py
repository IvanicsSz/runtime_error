import pygame
import random
bg = pygame.image.load("sprites/bg copy.gif")
stone = pygame.image.load("sprites/stone.gif")
brick = pygame.image.load("sprites/brick copy.gif")
player_1 = pygame.image.load("sprites/hit1 copy.gif")
player_2 = pygame.image.load("sprites/hit1 copy.gif")
bomb = pygame.image.load("sprites/bomb copy.gif")


class Wall:
    def __init__(self, x, y, image, fix):
        self.x = x
        self.y = y
        self.image = image
        self.fix = fix


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
        for f, column in enumerate(cls.gamefield):
            for h, row in enumerate(column):
                if not (row != 0 or (f == 1 and h == 1) or (f == 13 and h == 13) or (f == 2 and h == 1)
                       or (f == 1 and h == 2) or (f == 12 and h == 11) or (f == 13 and h == 10)):
                    if random.choice([0, 1]):
                        cls.gamefield[f][h] = Wall(x=f * 78, y=h * 78, image=brick, fix=False)

    @classmethod
    def can_move(cls, x, y):
        return cls.gamefield[x][y] == 0
