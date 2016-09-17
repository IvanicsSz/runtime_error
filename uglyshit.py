import pygame
from models import *
import random


pygame.mixer.init()
try:
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joysticks[0].init()
    joysticks[1].init()
    player1_joystick = joysticks[0]
    player2_joystick = joysticks[1]
except IndexError:
    player1_joystick = None
    player2_joystick = None


game_exit = False
width = 1170
height = 1014

bg = pygame.image.load("sprites/bg.jpg")
stone = pygame.image.load("sprites/stone.jpg")
brick = pygame.image.load("sprites/brick.jpg")
player_1 = pygame.image.load("sprites/hit1.png")
player_2 = pygame.image.load("sprites/hit1.png")
bomb = pygame.image.load("sprites/bomb.png")
fire = pygame.image.load("sprites/fire.jpg")


gamefield = []
for i in range(15):
    gamefield.append([0] * 13)
    players = []
    players.append(Player(x=1, y=1, image=player_1))
    players.append(Player(x=13, y=11, image=player_2))
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
                if not isinstance(row, Fire):
                    game_display.blit(row.image, (i*78, j*78))
                elif isonfire(row):
                    game_display.blit(row.image, (i*78, j*78))
                else:
                    gamefield[i][j] = 0
    for i in players:
        if i.alive:
            game_display.blit(i.image, (i.x*78, i.y*78))
    for i in bombs:
        if i.active:
            game_display.blit(i.image, (i.x*78, i.y*78))


def handle_joystick():
    try:
        if e.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            if player1jy > 0 and not move_cd(players[0]):
                if can_move(x=players[0].x, y=players[0].y+1):
                    players[0].y += 1
                    players[0].move_cd = pygame.time.get_ticks()
            elif player1jy < 0 and not move_cd(players[0]):
                if can_move(x=players[0].x, y=players[0].y-1):
                    players[0].y -= 1
                    players[0].move_cd = pygame.time.get_ticks()
            if player1jx < 0 and not move_cd(players[0]):
                if can_move(x=players[0].x-1, y=players[0].y):
                    players[0].x -= 1
                    players[0].move_cd = pygame.time.get_ticks()
            elif player1jx > 0 and not move_cd(players[0]):
                if can_move(x=players[0].x+1, y=players[0].y):
                    players[0].x += 1
                    players[0].move_cd = pygame.time.get_ticks()
            player2jx, player2jy = player2_joystick.get_axis(0), player2_joystick.get_axis(1)
            if player2jy > 0 and not move_cd(players[1]):
                if can_move(x=players[1].x, y=players[1].y+1):
                    players[1].y += 1
                    players[1].move_cd = pygame.time.get_ticks()
            elif player2jy < 0 and not move_cd(players[1]):
                if can_move(x=players[1].x, y=players[1].y-1):
                    players[1].y -= 1
                    players[0].move_cd = pygame.time.get_ticks()
            if player2jx < 0 and not move_cd(players[1]):
                if can_move(x=players[1].x-1, y=players[1].y):
                    players[1].x -= 1
                    players[1].move_cd = pygame.time.get_ticks()
            elif player2jx > 0 and not move_cd(players[1]):
                if can_move(x=players[1].x+1, y=players[1].y):
                    players[1].x += 1
                    players[1].move_cd = pygame.time.get_ticks()
        if e.type == pygame.locals.JOYBUTTONDOWN:
            player1Button = player1_joystick.get_button(0)
            if player1Button > 0 and not bombs[0].active:
                plant_bomb(x=players[0].x, y=players[0].y, player=0)
            player2Button = player2_joystick.get_button(0)
            if player2Button > 0 and not bombs[1].active:
                plant_bomb(x=players[1].x, y=players[1].y, player=1)
    except:
           pass


def handle_keys():
    """ Handles Keys """
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] and not move_cd(players[0]):
        if can_move(x=players[0].x, y=players[0].y+1):
            players[0].y += 1
            players[0].move_cd = pygame.time.get_ticks()
    elif key[pygame.K_UP] and not move_cd(players[0]):
        if can_move(x=players[0].x, y=players[0].y-1):
            players[0].y -= 1
            players[0].move_cd = pygame.time.get_ticks()
    if key[pygame.K_LEFT] and not move_cd(players[0]):
        if can_move(x=players[0].x-1, y=players[0].y):
            players[0].x -= 1
            players[0].move_cd = pygame.time.get_ticks()
    elif key[pygame.K_RIGHT] and not move_cd(players[0]):
        if can_move(x=players[0].x+1, y=players[0].y):
            players[0].x += 1
            players[0].move_cd = pygame.time.get_ticks()
    if key[pygame.K_s] and not move_cd(players[1]):
        if can_move(x=players[1].x, y=players[1].y+1):
            players[1].y += 1
            players[1].move_cd = pygame.time.get_ticks()
    elif key[pygame.K_w] and not move_cd(players[1]):
        if can_move(x=players[1].x, y=players[1].y-1):
            players[1].y -= 1
            players[0].move_cd = pygame.time.get_ticks()
    if key[pygame.K_a] and not move_cd(players[1]):
        if can_move(x=players[1].x-1, y=players[1].y):
            players[1].x -= 1
            players[1].move_cd = pygame.time.get_ticks()
    elif key[pygame.K_d] and not move_cd(players[1]):
        if can_move(x=players[1].x+1, y=players[1].y):
            players[1].x += 1
            players[1].move_cd = pygame.time.get_ticks()
    if key[pygame.K_q] and not bombs[0].active:
        plant_bomb(x=players[0].x, y=players[0].y, player=0)
    if key[pygame.K_p] and not bombs[1].active:
        plant_bomb(x=players[1].x, y=players[1].y, player=1)


def can_move(x, y):
    return gamefield[x][y] == 0 and all([not(i.x == x and i.y == y) for i in bombs if i.active is True])


def plant_bomb(x, y, player):
    bombs[player].x = x
    bombs[player].y = y
    bombs[player].timer = pygame.time.get_ticks()
    bombs[player].active = True


def check_bombs():
    for i in bombs:
        if pygame.time.get_ticks() - i.timer > 2000 and i.active:
            explode(i)
            i.active = False


def explode(bomb):
    play_blast()
    gamefield[bomb.x][bomb.y] = Fire(x=bomb.x, y=bomb.y, image=fire, timer=pygame.time.get_ticks())
    hit_player(x=bomb.x, y=bomb.y)
    if bomb.x >= 1 and can_extend(x=bomb.x-1, y=bomb.y):
        gamefield[bomb.x-1][bomb.y] = Fire(x=bomb.x-1, y=bomb.y, image=fire, timer=pygame.time.get_ticks())
        hit_player(x=bomb.x-1, y=bomb.y)
        if bomb.x >= 2 and can_extend(x=bomb.x-2, y=bomb.y):
            gamefield[bomb.x-2][bomb.y] = Fire(x=bomb.x-2, y=bomb.y, image=fire, timer=pygame.time.get_ticks())
            hit_player(x=bomb.x-2, y=bomb.y)
    if bomb.x <= 13 and can_extend(x=bomb.x+1, y=bomb.y):
        gamefield[bomb.x+1][bomb.y] = Fire(x=bomb.x+1, y=bomb.y, image=fire, timer=pygame.time.get_ticks())
        hit_player(x=bomb.x+1, y=bomb.y)
        if bomb.x <= 12 and can_extend(x=bomb.x+2, y=bomb.y):
            gamefield[bomb.x+2][bomb.y] = Fire(x=bomb.x+2, y=bomb.y, image=fire, timer=pygame.time.get_ticks())
            hit_player(x=bomb.x+2, y=bomb.y)
    if bomb.y >= 1 and can_extend(x=bomb.x, y=bomb.y-1):
        gamefield[bomb.x][bomb.y-1] = Fire(x=bomb.x, y=bomb.y-1, image=fire, timer=pygame.time.get_ticks())
        hit_player(x=bomb.x, y=bomb.y-1)
        if bomb.y >= 2 and can_extend(x=bomb.x, y=bomb.y-2):
            gamefield[bomb.x][bomb.y-2] = Fire(x=bomb.x, y=bomb.y-2, image=fire, timer=pygame.time.get_ticks())
            hit_player(x=bomb.x, y=bomb.y-2)
    if bomb.y <= 11 and can_extend(x=bomb.x, y=bomb.y+1):
        gamefield[bomb.x][bomb.y+1] = Fire(x=bomb.x, y=bomb.y+1, image=fire, timer=pygame.time.get_ticks())
        hit_player(x=bomb.x, y=bomb.y+1)
        if bomb.y <= 10 and can_extend(x=bomb.x, y=bomb.y+2):
            gamefield[bomb.x][bomb.y+2] = Fire(x=bomb.x, y=bomb.y+2, image=fire, timer=pygame.time.get_ticks())
            hit_player(x=bomb.x, y=bomb.y+2)


def can_extend(x, y):
    return gamefield[x][y] == 0 or not isinstance(gamefield[x][y], Wall) or not gamefield[x][y].fix


def hit_player(x, y):
    for i in players:
        if i.x == x and i.y == y:
            i.alive = False


def isonfire(fire):
    return not pygame.time.get_ticks() - fire.timer > 300


def move_cd(player):
    return not pygame.time.get_ticks() - player.move_cd > 200


def play_blast():
    blast = 'blast.wav'
    pygame.mixer.music.load(blast)
    pygame.mixer.music.play()


game_display = pygame.display.set_mode((width, height))


def main():
    global game_exit
    game_init()
    while not game_exit and all([i.alive for i in players]):
        draw_gamefield()
        check_bombs()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        handle_keys()


# pygame.quit()
