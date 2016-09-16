import pygame
from visuals import *

class Sprite:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Player(Sprite):

    def __init__(self, player_id, *args, **kwargs):
        self.player_id = player_id
        super().__init__(*args, **kwargs)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        origin = [self.x, self.y]
        if [key[pygame.K_DOWN], key[pygame.K_s]][self.player_id]:
            if Visuals.can_move(x=self.x, y=self.y+1):
                self.y += 1
        if [key[pygame.K_UP], key[pygame.K_w]][self.player_id]:
            if Visuals.can_move(x=self.x, y=self.y-1):
                self.y -= 1
        if [key[pygame.K_LEFT], key[pygame.K_a]][self.player_id]:
            if Visuals.can_move(x=self.x-1, y=self.y):
                self.x -= 1
        if [key[pygame.K_RIGHT], key[pygame.K_d]][self.player_id]:
            if Visuals.can_move(x=self.x+1, y=self.y):
                self.x += 1
        return [origin, self.x, self.y]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Bomb(Sprite):

    def __init__(self, timer, radius, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.timer = timer
        self. radius = radius
