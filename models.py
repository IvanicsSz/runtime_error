import pygame


class Sprite:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Player(Sprite):

    def __init__(self, alive=True, move_cd=0, *args, **kwargs):
        self.alive = alive
        self.move_cd = move_cd
        super().__init__(*args, **kwargs)


class Fire(Sprite):

    def __init__(self, timer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = timer


class Bomb(Sprite):

    def __init__(self, timer=0, active=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = timer
        self.active = active

class Wall(Sprite):

    def __init__(self, fix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fix = fix
