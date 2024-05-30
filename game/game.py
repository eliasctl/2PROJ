import pygame


def game(gameWindow):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
    pygame.draw.rect(gameWindow, (255, 0, 0), (0, 0, 50, 50))
    pygame.display.flip()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit the game
    pygame.quit()