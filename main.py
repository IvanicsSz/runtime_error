from models import *
import random

pygame.init()
pygame.mixer.init()

game_exit = False
width = 1170
height = 1014

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('BomberMan - Jungle ed.')


player1 = Player(x=1, y=1, image=player_1, player_id=0)
player2 = Player(x=13, y=11, image=player_2, player_id=1)

def draw_gamefield():
    game_display.blit(bg, (0, 0))
    for i, column in enumerate(Visuals.gamefield):
        for j, row in enumerate(column):
            if row != 0:
                game_display.blit(row.image, (i*78, j*78))
    game_display.blit(player1.image, (player1.x*78, player1.y*78))
    game_display.blit(player2.image, (player2.x * 78, player2.y * 78))

def play_blast():
    blast = 'blast.wav'
    key = pygame.key.get_pressed()
    if key[pygame.K_b]:
        pygame.mixer.music.load(blast)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
          pygame.time.Clock().tick(10)

Visuals.game_init()

while not game_exit:
    draw_gamefield()
    pygame.display.update()
    play_blast()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    player1.handle_keys()
    player2.handle_keys()
    pygame.time.delay(50)

pygame.quit()
