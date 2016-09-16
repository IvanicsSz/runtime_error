from models import *
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
width = 1170
height = 1014

game_display = pygame.display.set_mode((width, height))
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

player1 = Player(x=1, y=1, image=player_1, player_id=0)
player2 = Player(x=13, y=11, image=player_2, player_id=1)
player1_rect = player1.image.get_rect()
player2_rect = player2.image.get_rect()

def draw_gamefield():
    game_display.blit(bg, (0, 0))
    for i, column in enumerate(Visuals.gamefield):
        for j, row in enumerate(column):
            if row != 0:
                game_display.blit(row.image, (i*78, j*78))
    game_display.blit(player1.image, (player1.x*78, player1.y*78))
    game_display.blit(player2.image, (player2.x * 78, player2.y * 78))


Visuals.game_init()


while not game_exit:
    draw_gamefield()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    # player1.draw(game_display)
    player1.handle_keys()
    # player2.draw(game_display)
    player2.handle_keys()
    pygame.time.delay(100)
    print(player1.get_rects())
    print(player2.get_rects())
    print(player1_rect.left, player1_rect.right)
    # if player1.left < 0 or player1.right > width:
    #     speed[0] = -speed[0]
    # if player1.top < 0 or player1.bottom > height:
    #     speed[1] = -speed[1]


pygame.quit()
