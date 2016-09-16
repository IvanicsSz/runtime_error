import pygame
import os

# it is better to have an extra variable, than an extremely long line.
img_path = os.path.join('ball.gif')


class Bird:  # represents the bird, not the game
    def __init__(self, x, y):
        """ The constructor of the class """
        self.image = pygame.image.load(img_path)
        # the bird's position
        self.x = x
        self.y = y

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]:  # down key
            self.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left

    def handle_keys2(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_s]:  # down key
            self.y += dist  # move down
        elif key[pygame.K_w]:  # up key
            self.y -= dist  # move up
        if key[pygame.K_d]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_a]:  # left key
            self.x -= dist  # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((60, 50))

bird = Bird(0, 0)  # create an instance
bird2 = Bird(60, 60)
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    bird2.handle_keys2()
    bird.handle_keys()  # handle the keys

    screen.fill((255, 255, 255))  # fill the screen with white
    bird.draw(screen)  # draw the bird to the screen
    bird2.draw(screen)
    pygame.display.update()  # update the screen

    clock.tick(40)
