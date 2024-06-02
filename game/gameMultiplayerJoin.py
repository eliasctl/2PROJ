import datetime
import pygame
import ast
from time import sleep
from .getData import getData
from .updateData import updateData
from .lose import create_defeat_screen
from .win import create_victory_screen
from .getTroops import getTroops
from .getCivilizations import getCivilizations
from .economy import Player
from .getSpecialCapacity import getSpecialCapacity
from .deleteGame import deleteGame
from .deletePlayer import deletePlayer
from .joinGame import joinGame


def gameMultiplayerJoin(gameWindow, screen_width, screen_height, idGame, idPlayer):

    startTime = datetime.datetime.now()

    joinGame(idPlayer, idGame, startTime)

    game = getData(idGame)

    startTime = datetime.datetime.strptime(game["startTime"], "%Y-%m-%d %H:%M:%S")

    # Wait until startTime + 20 seconds
    while datetime.datetime.now() < startTime + datetime.timedelta(seconds=2):
        print("Waiting for the game to start")
        print(datetime.datetime.now())
        pass

    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
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
        player.gold = game["player2Gold"]
        player.xp = game["player2XP"]
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
            create_victory_screen()
        elif game["player2HPCamp"] <= 0:
            running = False
            create_defeat_screen()
    
        game.pop("player1Id")
        game.pop("player2Id")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                buttonSize = min(screen_width, screen_height) // 20
                if (mouse_pos[0] > screen_width // 3.85 - buttonSize // 2 and mouse_pos[0] < screen_width // 3.85 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize): 
                    # Clicked on troop 1 (light weight)
                    idTroop = 1 + ((int(game["player2Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer2"] == None:
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer2"]) == str:
                        game["waitingListPlayer2"] = ast.literal_eval(game["waitingListPlayer2"])
                    if len(game["waitingListPlayer2"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else:
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 3.15 - buttonSize and mouse_pos[0] < screen_width // 3.15 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 2 (medium weight)
                    idTroop = 2 + ((int(game["player2Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer2"] == None:
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer2"]) == str:
                        game["waitingListPlayer2"] = ast.literal_eval(game["waitingListPlayer2"])
                    if len(game["waitingListPlayer2"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 2.8 - buttonSize and mouse_pos[0] < screen_width // 2.8 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 3 (heavy weight)
                    idTroop = 3 + (int(game["player2Civilization"] -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer2"] == None:
                        game["waitingListPlayer2"] = []
                    if type(game["waitingListPlayer2"]) == str:
                        game["waitingListPlayer2"] = ast.literal_eval(game["waitingListPlayer2"])
                    if len(game["waitingListPlayer2"]) < 5 and player.gold >= troopData["cost"]:
                        player.gold -= troopData["cost"]
                        game["waitingListPlayer2"].append([2, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else :
                        print("You can't buy this troop or waiting list is full")
                elif (mouse_pos[0] > screen_width // 1.56 - buttonSize and mouse_pos[0] < screen_width // 1.56 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # New era 
                    if game["player2Civilization"] < 4 and player.xp >= civilizations[game["player2Civilization"]]["xpCost"]:
                        player.xp -= civilizations[game["player2Civilization"]]["xpCost"]
                        game["player2Civilization"] += 1
                    else:
                        print("You can't have more than 4 eras or you don't have enough xp")
                elif (mouse_pos[0] > screen_width // 1.47 - buttonSize and mouse_pos[0] < screen_width // 1.47 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Special attack
                    if game["player2SpecialCapacity"] == False and player.xp >= specialCapacity[game["player2Civilization"]]["cost"]:
                        game["player2SpecialCapacity"] = True
                    else:
                        print("You can't use the special attack yet")
        

        print("--------------Waiting List-----------------------")
        print(game["waitingListPlayer2"])

        print("--------------XP and Gold-----------------------")
        print(player.xp)
        print(player.gold)

        print("--------------Passive income-----------------------")
        player.passive_income(game["player2Civilization"])
        print(player.xp)
        print(player.gold)

        game["player2Gold"] = player.gold
        game["player2Xp"] = player.xp

        updateData(game)

        sleep(1)

    # Quit the game
    pygame.quit()

    # Delete the game
    deleteGame(idGame)
    
    # Delete the player
    deletePlayer(idPlayer)
