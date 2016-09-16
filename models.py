class Sprite:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Player(Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bomb(Sprite):

    def __init__(self, timer, radius, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.timer = timer
        self. radius = radius

class Wall(Sprite):

    def __init__(self, fix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fix = fix