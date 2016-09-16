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

    def get_rects(self):
        rect = self.image.get_rect()
        return [rect.topleft, rect.top, rect.right, rect.left, rect.bottom]

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        origin = [self.x, self.y]
        if [key[pygame.K_DOWN], key[pygame.K_s]][self.player_id]:
            # if can_move(x=self.x, y=self.y+1):
            self.y += 1
        if [key[pygame.K_UP], key[pygame.K_w]][self.player_id]:
            # if can_move(x=self.x, y=self.y-1):
            self.y -= 1
        if [key[pygame.K_LEFT], key[pygame.K_a]][self.player_id]:
            # if can_move(x=self.x-1, y=self.y):
            self.x -= 1
        if [key[pygame.K_RIGHT], key[pygame.K_d]][self.player_id]:
            # if can_move(x=self.x+1, y=self.y):
            self.x += 1

        return [origin, self.x, self.y]

    # @staticmethod
    # def can_move(x, y):
    #     return Visuals.gamefield[x][y] == 0

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))



class Bomb(Sprite):

    def __init__(self, timer, radius, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.timer = timer
        self. radius = radius

class Wall(Sprite):

    def __init__(self, fix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fix = fix
