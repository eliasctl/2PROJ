import pygame
import ast
from time import sleep

import pyglet
from .getData import getData
from .updateData import updateData
from .updateField import updateField
from .lose import create_defeat_screen
from .win import create_victory_screen
from .getTroops import getTroops
from .getCivilizations import getCivilizations
from .economy import Player
from .getSpecialCapacity import getSpecialCapacity
from .deleteGame import deleteGame
from .deletePlayer import deletePlayer


def gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
    pygame.display.flip()
    troops = getTroops()
    civilizations = getCivilizations()
    specialCapacity = getSpecialCapacity()
    player = Player()
    player2 = Player()
    print(player.gold)
    print(player.xp)

    # Game loop
    running = True
    while running:
        game = getData(idGame)
        print("waiting list player 1 after get data: ", game)
        for element in game:
            if type(game[element]) == str and element != "startTime":
                game[element] = ast.literal_eval(game[element])
        if game["field"] == None:
            game["field"] = {}
            for i in range(25):
                game["field"][i] = [0, 0, 0, 0, 0]
        # Test if the game is over
        if game["player1HPCamp"] <= 0:
            running = False
            create_defeat_screen()
        elif game["player2HPCamp"] <= 0:
            running = False
            create_victory_screen()
    
        game.pop("player1Id")
        game.pop("player2Id")
        newGame, player = updateField(game, player, player2)

        troopSize = min(screen_width, screen_height) // 19.5

        # #Drawing the field
        for i in range(0, 25):
            if game["field"][i][0] == 1:
                rectanglePlayer1 = pygame.Rect(screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize)
                pygame.draw.rect(gameWindow, (156, 255, 199), rectanglePlayer1)
                image = pygame.image.load('./game/tempImages/troops/'+troops[game["field"][i][1]]["image"])
                image_rect = pygame.transform.scale(image, (troopSize, troopSize))
                gameWindow.blit(image_rect, rectanglePlayer1)

            elif game["field"][i][0] == 2:
                rectanglePlayer2 = pygame.Rect(screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize)
                pygame.draw.rect(gameWindow, (173, 158, 255), rectanglePlayer2)
                image = pygame.image.load('./game/tempImages/troops/'+troops[game["field"][i][1]]["image"])
                image_rect = pygame.transform.scale(image, (troopSize, troopSize))
                image_rect = pygame.transform.flip(image_rect, True, False)
                gameWindow.blit(image_rect, rectanglePlayer2)
            else:
                pygame.draw.rect(gameWindow, (255, 255, 255, 0), (screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize))

        # Drawing infos xp and gold
        infosEmplacement = pygame.Rect(0, 0, screen_width // 5, screen_height // 10)
        pygame.draw.rect(gameWindow, (128, 128, 128), infosEmplacement)
        font = pygame.font.Font(None, 48)
        expText = font.render("XP: " + str(player.xp), True, (255, 255, 255))
        expText_rect = expText.get_rect(center=(infosEmplacement.width // 2, infosEmplacement.height // 4))
        gameWindow.blit(expText, expText_rect)
        goldText = font.render("GOLD: " + str(player.gold), True, (255, 255, 255))
        goldText_rect = goldText.get_rect(center=(infosEmplacement.width // 2, infosEmplacement.height // 4 * 3))
        gameWindow.blit(goldText, goldText_rect)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                buttonSize = min(screen_width, screen_height) // 20
                if (mouse_pos[0] > screen_width // 3.85 - buttonSize // 2 and mouse_pos[0] < screen_width // 3.85 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize): 
                    # Clicked on troop 1 (light weight)
                    idTroop = 1 + ((int(newGame["player1Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if newGame["waitingListPlayer1"] == None:
                        newGame["waitingListPlayer1"] = []
                        newGame["waitingListPlayer2"] = []
                    if type(newGame["waitingListPlayer1"]) == str:
                        newGame["waitingListPlayer1"] = ast.literal_eval(newGame["waitingListPlayer1"])
                    if len(newGame["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        newGame["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        newGame["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else:
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 3.15 - buttonSize and mouse_pos[0] < screen_width // 3.15 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 2 (medium weight)
                    idTroop = 2 + ((int(newGame["player1Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if newGame["waitingListPlayer1"] == None:
                        newGame["waitingListPlayer1"] = []
                        newGame["waitingListPlayer2"] = []
                    if type(newGame["waitingListPlayer1"]) == str:
                        newGame["waitingListPlayer1"] = ast.literal_eval(newGame["waitingListPlayer1"])
                    if len(newGame["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        newGame["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        newGame["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 2.8 - buttonSize and mouse_pos[0] < screen_width // 2.8 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 3 (heavy weight)
                    idTroop = 3 + (int(newGame["player1Civilization"] -1) * 3)
                    troopData = troops[idTroop-1]
                    if newGame["waitingListPlayer1"] == None:
                        newGame["waitingListPlayer1"] = []
                        newGame["waitingListPlayer2"] = []
                    if type(newGame["waitingListPlayer1"]) == str:
                        newGame["waitingListPlayer1"] = ast.literal_eval(newGame["waitingListPlayer1"])
                    if len(newGame["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        newGame["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        newGame["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 1.56 - buttonSize and mouse_pos[0] < screen_width // 1.56 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # New era 
                    if newGame["player1Civilization"] < 4 and player.xp >= civilizations[newGame["player1Civilization"]]["xpCost"]:
                        player.xp -= civilizations[newGame["player1Civilization"]]["xpCost"]
                        newGame["player1Civilization"] += 1
                        newGame["player2Civilization"] += 1
                    else:
                        print("You can't have more than 4 eras or you don't have enough xp")
                elif (mouse_pos[0] > screen_width // 1.47 - buttonSize and mouse_pos[0] < screen_width // 1.47 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Special attack
                    if newGame["player1SpecialCapacity"] == False and player.xp >= specialCapacity[newGame["player1Civilization"]]["cost"]:
                        newGame["player1SpecialCapacity"] = True
                    else:
                        print("You can't use the special attack yet")
        

        print("--------------Waiting List-----------------------")
        print(newGame["waitingListPlayer1"])

        print("--------------XP and Gold-----------------------")
        print(player.xp)
        print(player.gold)

        print("--------------Passive income-----------------------")
        player.passive_income(newGame["player1Civilization"])
        print(player.xp)
        print(player.gold)

        updateData(newGame)

        sleep(1)

    # Quit the game
    pygame.quit()

    # Delete the game
    deleteGame(idGame)
    
    # Delete the player
    deletePlayer(idPlayer)
