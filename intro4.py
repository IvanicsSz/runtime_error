import pygame
import sys

# write in the windows header
pygame.display.set_caption('Hello World!')

# Game Loops and Game States
while True:  # main game loop
    for event in pygame.event.get():  # checking event what you have created
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            sys.exit()
            # 1.Handles events.
            # 2.Updates the game state.
            # every happening handled here movement, bomb ...
            # 3.Draws the game state to the screen.

            # pygame.event.Event Objects example: keyboard pressed, mouse move and so on
            # Event that exists in the event module
        pygame.display.update()
        # If you want the images on other
        # Surface objects to appear on the screen, you must ―blit‖ them (that is, copy them) to the display
        # Surface object with the blit() method

# Animation
