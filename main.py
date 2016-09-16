import pygame
from models import *

pygame.init()
bg = pygame.image.load("sprites/bg.jpg")
stone = pygame.image.load("sprites/stone.jpg")

game_exit = False

game_display = pygame.display.set_mode((1170, 1014))
pygame.display.set_caption('Bomberman - Jungle ed.')

while not game_exit:
    game_display.blit(bg, (0, 0))
    walls = []
    for i in range(15):
        for j in range(13):
            if i == 0 or i == 14 or j == 0 or j == 12 or (i % 2 == 0 and j % 2 == 0):
                new = Wall(x=i*78, y=j*78, image=stone, fix=True)
                walls.append(new)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True


pygame.quit()
