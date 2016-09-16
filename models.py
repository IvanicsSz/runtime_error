import pygame


class Sprite:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Player(Sprite):

    def __init__(self, player_id, *args, **kwargs):
        self.player_id = player_id
        super().__init__(*args, **kwargs)


class Bomb(Sprite):

    def __init__(self, timer=0, active=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = timer
        self.active = active

class Wall(Sprite):

    def __init__(self, fix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fix = fix
