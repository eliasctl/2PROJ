import pygame
import ast
from time import sleep
from .getData import getData
from .updateData import updateData
from .updateField import updateField
from .lose import create_defeat_screen
from .win import create_victory_screen
from .getTroops import getTroops
from .getCivilizations import getCivilizations
from .economie import Player
from .getSpecialCapacity import getSpecialCapacity
from .deleteGame import deleteGame
from .deletePlayer import deletePlayer


def gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
    pygame.draw.rect(gameWindow, (255, 0, 0), (0, 0, 50, 50))
    pygame.display.flip()
    troops = getTroops()
    civilizations = getCivilizations()
    specialCapacity = getSpecialCapacity()
    player = Player()
    print(player.gold)
    print(player.xp)

    # Game loop
    running = True
    while running:
        game = getData(idGame)
        for element in game:
            if type(game[element]) == str:
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
        newGame, player = updateField(game, player)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                buttonSize = min(screen_width, screen_height) // 20
                if (mouse_pos[0] > screen_width // 3.85 - buttonSize // 2 and mouse_pos[0] < screen_width // 3.85 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize): 
                    # Clicked on troop 1 (light weight)
                    idTroop = 1 + ((int(game["player1Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer1"] == None:
                        game["waitingListPlayer1"] = []
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else:
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 3.15 - buttonSize and mouse_pos[0] < screen_width // 3.15 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 2 (medium weight)
                    idTroop = 2 + ((int(game["player1Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer1"] == None:
                        game["waitingListPlayer1"] = []
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 2.8 - buttonSize and mouse_pos[0] < screen_width // 2.8 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 3 (heavy weight)
                    idTroop = 3 + (int(game["player1Civilization"] -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer1"] == None:
                        game["waitingListPlayer1"] = []
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], int(troopData["hp"])*difficulty, troopData["damage"]]) 
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 1.56 - buttonSize and mouse_pos[0] < screen_width // 1.56 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # New era 
                    if game["player1Civilization"] < 4 and player.xp >= civilizations[game["player1Civilization"]]["xpCost"]:
                        player.xp -= civilizations[game["player1Civilization"]]["xpCost"]
                        game["player1Civilization"] += 1
                        game["player2Civilization"] += 1
                    else:
                        print("You can't have more than 4 eras or you don't have enough xp")
                elif (mouse_pos[0] > screen_width // 1.47 - buttonSize and mouse_pos[0] < screen_width // 1.47 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Special attack
                    if game["player1SpecialCapacity"] == False and player.xp >= specialCapacity[game["player1Civilization"]]["cost"]:
                        game["player1SpecialCapacity"] = True
                    else:
                        print("You can't use the special attack yet")
        

        print("--------------Waiting List-----------------------")
        print(game["waitingListPlayer1"])

        print("--------------XP and Gold-----------------------")
        print(player.xp)
        print(player.gold)

        print("--------------Passive income-----------------------")
        player.passive_income(game["player1Civilization"])
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
