import pygame
from models import *
import random

pygame.init()
game_exit = False
width = 1170
height = 1014

bg = pygame.image.load("sprites/bg.jpg")
stone = pygame.image.load("sprites/stone.jpg")
brick = pygame.image.load("sprites/brick.jpg")
player_1 = pygame.image.load("sprites/hit1.png")
player_2 = pygame.image.load("sprites/hit1.png")
bomb = pygame.image.load("sprites/bomb.png")

gamefield = []
for i in range(15):
    gamefield.append([0] * 13)
player1 = Player(x=1, y=1, image=player_1, player_id=0)
player2 = Player(x=13, y=11, image=player_2, player_id=1)
bombs = []
bombs.append(Bomb(x=0, y=0, image=bomb))
bombs.append(Bomb(x=0, y=0, image=bomb))


def game_init():
    for i in range(15):
        for j in range(13):
            if i == 0 or i == 14 or j == 0 or j == 12 or (i % 2 == 0 and j % 2 == 0):
                gamefield[i][j] = Wall(x=i, y=j, image=stone, fix=True)
    for f, column in enumerate(gamefield):
        for h, row in enumerate(column):
            if not (row != 0 or (f == 1 and h == 1) or (f == 13 and h == 11) or
                    (f == 2 and h == 1) or (f == 1 and h == 2) or (f == 12 and h == 11) or (f == 13 and h == 10)):
                if random.choice([0, 1]):
                    gamefield[f][h] = Wall(x=f, y=h, image=brick, fix=False)


def draw_gamefield():
    game_display.blit(bg, (0, 0))
    for i, column in enumerate(gamefield):
        for j, row in enumerate(column):
            if row != 0:
                game_display.blit(row.image, (i*78, j*78))
    game_display.blit(player1.image, (player1.x*78, player1.y*78))
    game_display.blit(player2.image, (player2.x * 78, player2.y * 78))
    for i in bombs:
        if i.active:
            game_display.blit(i.image, (i.x*78, i.y*78))


def handle_keys():
    """ Handles Keys """
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if can_move(x=player1.x, y=player1.y+1):
            player1.y += 1
    elif key[pygame.K_UP]:
        if can_move(x=player1.x, y=player1.y-1):
            player1.y -= 1
    if key[pygame.K_LEFT]:
        if can_move(x=player1.x-1, y=player1.y):
            player1.x -= 1
    elif key[pygame.K_RIGHT]:
        if can_move(x=player1.x+1, y=player1.y):
            player1.x += 1
    if key[pygame.K_s]:
        if can_move(x=player2.x, y=player2.y+1):
            player2.y += 1
    elif key[pygame.K_w]:
        if can_move(x=player2.x, y=player2.y-1):
            player2.y -= 1
    if key[pygame.K_a]:
        if can_move(x=player2.x-1, y=player2.y):
            player2.x -= 1
    elif key[pygame.K_d]:
        if can_move(x=player2.x+1, y=player2.y):
            player2.x += 1
    if key[pygame.K_q]:
        plant_bomb(x=player1.x, y=player1.y, player=0)
    if key[pygame.K_p]:
        plant_bomb(x=player2.x, y=player2.y, player=1)


def can_move(x, y):
    return gamefield[x][y] == 0


def plant_bomb(x, y, player):
    bombs[player].x = x
    bombs[player].y = y
    bombs[player].timer = pygame.time.get_ticks()
    bombs[player].active = True


def check_bombs():
    for i in bombs:
        if pygame.time.get_ticks() - i.timer > 2000:
            explode(i)
            i.active = False


def explode(bomb):
    if bomb.x >= 1 and can_extend(x=bomb.x-1, y=bomb.y):
        gamefield[bomb.x-1][bomb.y] = 0
        if bomb.x >= 2 and can_extend(x=bomb.x-2, y=bomb.y):
            gamefield[bomb.x-2][bomb.y] = 0
    if bomb.x <= 13 and can_extend(x=bomb.x+1, y=bomb.y):
        gamefield[bomb.x+1][bomb.y] = 0
        if bomb.x <= 12 and can_extend(x=bomb.x+2, y=bomb.y):
            gamefield[bomb.x+2][bomb.y] = 0
    if bomb.y >= 1 and can_extend(x=bomb.x, y=bomb.y-1):
        gamefield[bomb.x][bomb.y-1] = 0
        if bomb.y >= 2 and can_extend(x=bomb.x, y=bomb.y-2):
            gamefield[bomb.x][bomb.y-2] = 0
    if bomb.y <= 11 and can_extend(x=bomb.x, y=bomb.y+1):
        gamefield[bomb.x][bomb.y+1] = 0
        if bomb.x <= 10 and can_extend(x=bomb.x, y=bomb.y+2):
            gamefield[bomb.x][bomb.y+2] = 0

def can_extend(x, y):
    return gamefield[x][y] == 0 or not isinstance(gamefield[x][y], Wall) or not gamefield[x][y].fix


game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('BomberMan - Jungle ed.')


game_init()
while not game_exit:
    draw_gamefield()
    check_bombs()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    handle_keys()


pygame.quit()
