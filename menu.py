import pygame
import uglyshit

pygame.init()

menu_exit = False
bg = pygame.image.load("sprites/jungle.jpg")
racoon = []
racoon.append(pygame.image.load("sprites/menuracoon.png"))
racoon.append(pygame.image.load("sprites/menuracoon2.png"))
panda = []
panda.append(pygame.image.load("sprites/menupanda.png"))
panda.append(pygame.image.load("sprites/menupanda2.png"))
menu_music = pygame.mixer.Sound('menu.ogg')


i = 0
while not menu_exit:
    game_display = pygame.display.set_mode((1170, 1014))
    pygame.display.set_caption('BomberMan - Panda VS Racoon')
    game_display.blit(bg, (0, 0))
    font = pygame.font.SysFont('arial', 50)
    text = font.render("Welcome to BomBEARman", 1, (0, 255, 0))
    textpos = text.get_rect()
    textpos.centerx = game_display.get_rect().centerx
    textpos.centery = game_display.get_rect().centery - 50
    game_display.blit(text, textpos)
    text2 = font.render("Panda VS Racoon", 1, (0, 255, 0))
    textpos = text2.get_rect()
    textpos.centerx = game_display.get_rect().centerx
    textpos.centery = game_display.get_rect().centery
    game_display.blit(text2, textpos)
    text3 = font.render("Press SPACE to start", 1, (0, 255, 0))
    textpos = text3.get_rect()
    textpos.centerx = game_display.get_rect().centerx
    textpos.centery = game_display.get_rect().centery + 50
    game_display.blit(text3, textpos)
    text4 = font.render("or ESCAPE to quit", 1, (0, 255, 0))
    textpos = text4.get_rect()
    textpos.centerx = game_display.get_rect().centerx
    textpos.centery = game_display.get_rect().centery + 100
    game_display.blit(text4, textpos)

    i = (i+1) % 2
    show_racoon = racoon[i]
    show_panda = panda[i]
    picpos = show_racoon.get_rect()
    picpos.x = game_display.get_rect().centerx + 430
    picpos.centery = game_display.get_rect().centery
    game_display.blit(show_racoon, picpos)
    pygame.display.update()
    picpos = show_panda.get_rect()
    picpos.x = game_display.get_rect().centerx - 500
    picpos.centery = game_display.get_rect().centery
    game_display.blit(show_panda, picpos)
    pygame.display.update()

    key = pygame.key.get_pressed()
    menu_music.play()
    if key[pygame.K_SPACE]:
        menu_music.fadeout(500)
        uglyshit.main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            menu_exit = True

    pygame.time.delay(200)


pygame.quit()
