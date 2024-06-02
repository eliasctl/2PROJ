import pygame
import ast
import json
from time import sleep
from .getData import getData
from .updateData import updateData
from .updateField import updateField
from .lose import create_defeat_screen
from .win import create_victory_screen
from .getTroops import getTroops
from .getCivilizations import getCivilizations


def game(gameWindow, screen_width, screen_height, idGame, idPlayer):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Game")
    pygame.draw.rect(gameWindow, (255, 0, 0), (0, 0, 50, 50))
    pygame.display.flip()
    troops = getTroops()
    civilizations = getCivilizations()
    xp = 0
    gold = 1000
    

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
        newGame = updateField(game)
        
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
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5:
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else:
                        print("You can't have more than 5 troops waiting")
                elif (mouse_pos[0] > screen_width // 3.15 - buttonSize and mouse_pos[0] < screen_width // 3.15 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 2 (medium weight)
                    idTroop = 2 + ((int(game["player1Civilization"]) -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer1"] == None:
                        game["waitingListPlayer1"] = []
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5:
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else :
                        print("You can't have more than 5 troops waiting")
                elif (mouse_pos[0] > screen_width // 2.8 - buttonSize and mouse_pos[0] < screen_width // 2.8 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Clicked on troop 3 (heavy weight)
                    idTroop = 3 + (int(game["player1Civilization"] -1) * 3)
                    troopData = troops[idTroop-1]
                    if game["waitingListPlayer1"] == None:
                        game["waitingListPlayer1"] = []
                    if type(game["waitingListPlayer1"]) == str:
                        game["waitingListPlayer1"] = ast.literal_eval(game["waitingListPlayer1"])
                    if len(game["waitingListPlayer1"]) < 5:
                        game["waitingListPlayer1"].append([1, idTroop, troopData["type"], troopData["hp"], troopData["damage"]])
                    else :
                        print("You can't have more than 5 troops waiting")
                elif (mouse_pos[0] > screen_width // 1.56 - buttonSize and mouse_pos[0] < screen_width // 1.56 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # New era 
                    if game["player1Civilization"] < 4 and xp >= civilizations[game["player1Civilization"]]["xp"]:
                        xp -= civilizations[game["player1Civilization"]]["xp"]
                        game["player1Civilization"] += 1
                    else:
                        print("You can't have more than 4 eras")
                elif (mouse_pos[0] > screen_width // 1.47 - buttonSize and mouse_pos[0] < screen_width // 1.47 + buttonSize) and (mouse_pos[1] > screen_height * 4 // 4.1 - buttonSize // 2 and mouse_pos[1] < screen_height * 4 // 4.1 + buttonSize):
                    # Special attack
                    if game["specialAttack"] == True:
                        game["specialAttack"] = False
                    else:
                        print("You can't use the special attack yet")
        
        print(game["waitingListPlayer1"])
        # print(game)
        # Update the game field
        print("--------------New Game-----------------------")
        print(newGame)

        print("--------------Updating Game-----------------------")
        newGame["field"] = json.dumps(newGame["field"])
        updateData(newGame)
        # # print(game)
        # game["player1HPCamp"] = 2500
        # print("-----------------")
        # print(game)
        # print("-----------------")
        
        # running = False
        sleep(0.5)

    # Quit the game
    pygame.quit()

    # Delete the game

    # Delete the player
