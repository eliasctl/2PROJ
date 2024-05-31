import pygame
from .getData import getData
from .updateData import updateData
from .updateField import updateField


def game(gameWindow, idGame, idPlayer):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
    pygame.draw.rect(gameWindow, (255, 0, 0), (0, 0, 50, 50))
    pygame.display.flip()
    game = getData()

    # Game loop
    running = True
    while running:
        game = getData()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the game field
        updateField(game["field"], gameWindow, None) #, game["waitingList"])
        # print(game)
        # game["game"] = game.pop("id")
        # game.pop("player1Id")
        # game.pop("player2Id")
        # game["player1HPCamp"] = 2500
        # print("-----------------")
        # print(game)
        # print("-----------------")
        # updateData(game)
        # running = False

    # Quit the game
    pygame.quit()