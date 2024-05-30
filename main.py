from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
import pygame

# from game.menu import menu
def main():
    # #Asking for player name 
    # idPlayer = createPlayer()
    # gameBegin(idPlayer)
    gameWindow = init()
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

if __name__ == "__main__":
    main()