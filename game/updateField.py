import ast
# Use of the function updateField
# This function is used to update the game field
# It update the troops position, the troops HP, the troops attack and the camp HP


# Type of game field :
# dictionary with 25 keys (0 to 24) and each key has a list of 2 elements
# Each key is the position of a troop on the field
# The first element of the list is the player id of the troop
# The second element of the list is the troop id
# The third element of the list is the troop type
# The fourth element of the list is the troop HP
# The fifth element of the list is the troop attack


# Creation of the game field
# my_dict = {}
# for i in range(25):
#     my_dict[i] = [0, 0]
# my_dict_json = json.dumps(my_dict)


# Example of game field
# my_dict = {
#     0: [1, 1, 1, 100, 10],
#     1: [1, 2, 2, 100, 10],
#     ...
#     24: [2, 1, 1, 400, 10]
# }


def updateField(game, player, player2):
    field, waitingListPlayer1, waitingListPlayer2, player1HPCamp, player2HPCamp, player2Gold, player2XP = game["field"], game["waitingListPlayer1"], game["waitingListPlayer2"], game["player1HPCamp"], game["player2HPCamp"], game["player2Gold"], game["player2XP"]

    if player2Gold == None:
        player2Gold = 0
    if player2XP == None:
        player2XP = 0

    if type(field) == str:
        field = ast.literal_eval(field)
    if type(waitingListPlayer1) == str:
        waitingListPlayer1 = ast.literal_eval(waitingListPlayer1)
    if type(waitingListPlayer2) == str:
        waitingListPlayer2 = ast.literal_eval(waitingListPlayer2)
    if type(player1HPCamp) == str:
        player1HPCamp = ast.literal_eval(player1HPCamp)
    if type(player2HPCamp) == str:
        player2HPCamp = ast.literal_eval(player2HPCamp)
    if type(player2Gold) == str:
        player2Gold = ast.literal_eval(player2Gold)
    if type(player2XP) == str:
        player2XP = ast.literal_eval(player2XP)
    
    # Loop throught the field for player 1
    for element in reversed(field):
        if field[element][0] == 1:
            # Test if the troop is a ranged troop
            if field[element][2] == 2:

                # Test if the troop can attack the camp
                if element == 22:
                    # Camp attack
                    player2HPCamp -= field[element][4]

                # Test if the troop has an enemy to attack in his range
                elif (field[element+1][0] == 2) or (field[element+2][0] == 2) or (field[element+3][0] == 2):
                    # Attack the troop in front of him
                    if field[element+1][0] == 2:
                        field[element+1][3] -= field[element][4]
                        if field[element+1][3] <= 0:
                            player.earn_xp_and_gold(field[element+1][1])
                            field[element+1] = [0, 0, 0, 0, 0]
                    elif field[element+2][0] == 2:
                        field[element+2][3] -= field[element][4]
                        if field[element+2][3] <= 0:
                            player.earn_xp_and_gold(field[element+2][1])
                            field[element+2] = [0, 0, 0, 0, 0]
                    elif field[element+3][0] == 2:
                        field[element+3][3] -= field[element][4]
                        if field[element+3][3] <= 0:
                            player.earn_xp_and_gold(field[element+3][1])
                            field[element+3] = [0, 0, 0, 0, 0]


                # Test if the troop can move
                elif field[element+1][0] == 0:
                    field[element+1] = field[element]
                    field[element] = [0, 0, 0, 0, 0]

            # Test if the troop is a melee troop
            elif field[element][2] != 0:

                # Test if the troop can attack the camp
                if element == 23:
                    # Camp attack
                    player2HPCamp -= field[element][4]
                
                # Test if the troop has an enemy to attack in his range
                elif (field[element+1][0] == 2):
                    # Attack the troop in front of him
                    field[element+1][3] -= field[element][4]
                    if field[element+1][3] <= 0:
                        player.earn_xp_and_gold(field[element+1][1])
                        field[element+1] = [0, 0, 0, 0, 0]
                    

                # Test if the troop can move
                elif field[element+1][0] == 0:
                    field[element+1] = field[element]
                    field[element] = [0, 0, 0, 0, 0]

    # Loop throught the field for player 2
    for element in field:
        if field[element][0] == 2:
            # Test if the troop is a ranged troop
            if field[element][2] == 2:

                # Test if the troop can attack the camp
                if element == 2:
                    # Camp attack
                    player1HPCamp -= field[element][4]

                # Test if the troop has an enemy to attack in his range
                elif (field[element-1][0] == 1) or (field[element-2][0] == 1) or (field[element-3][0] == 1):
                    # Attack the troop in front of him
                    if field[element-1][0] == 1:
                        field[element-1][3] -= field[element][4]
                        if field[element-1][3] <= 0:
                            player2.earn_xp_and_gold(field[element-1][1])
                            field[element-1] = [0, 0, 0, 0, 0]
                    elif field[element-2][0] == 1:
                        field[element-2][3] -= field[element][4]
                        if field[element-2][3] <= 0:
                            player2.earn_xp_and_gold(field[element-2][1])
                            field[element-2] = [0, 0, 0, 0, 0]
                    elif field[element-3][0] == 1:
                        field[element-3][3] -= field[element][4]
                        if field[element-3][3] <= 0:
                            player2.earn_xp_and_gold(field[element-3][1])
                            field[element-3] = [0, 0, 0, 0, 0]

                # Test if the troop can move
                elif field[element-1][0] == 0:
                    field[element-1] = field[element]
                    field[element] = [0, 0, 0, 0, 0]

            # Test if the troop is a melee troop
            elif field[element][2] != 0:

                # Test if the troop can attack the camp
                if element == 1:
                    # Camp attack
                    player1HPCamp -= field[element][4]
                
                # Test if the troop has an enemy to attack in his range
                elif (field[element - 1][0] == 1):

                    # Attack the troop in front of him
                    field[element-1][3] -= field[element][4]
                    if field[element-1][3] <= 0:
                        player2.earn_xp_and_gold(field[element-1][1])
                        field[element-1] = [0, 0, 0, 0, 0]

                # Test if the troop can move
                elif field[element-1][0] == 0:
                    field[element-1] = field[element]
                    field[element] = [0, 0, 0, 0, 0]

    if waitingListPlayer1 != None and field[0] == [0, 0, 0, 0, 0] and waitingListPlayer1 != []:
        field[0] = waitingListPlayer1[0]
        waitingListPlayer1.pop(0)
    if waitingListPlayer2 != None and field[24] == [0, 0, 0, 0, 0] and waitingListPlayer2 != []:
        field[24] = waitingListPlayer2[0]
        waitingListPlayer2.pop(0)

    if player1HPCamp <= 0:
        print("Player 2 wins")
    elif player2HPCamp <= 0:
        print("Player 1 wins")

    print("---------------------Field----------------------------")
    for element in field:
        print(field[element])
    print("\n\n\n")

    game["field"], game["waitingListPlayer1"], game["waitingListPlayer2"], game["player1HPCamp"], game["player2HPCamp"], game["player2Gold"], game["player2XP"] = field, waitingListPlayer1, waitingListPlayer2, player1HPCamp, player2HPCamp, player2.gold, player2.xp
    
    print("---------------------Game----------------------------")
    print(game["field"])
    return game, player


# newField = {}
# for i in range(25):
#     newField[i] = [0, 0, 0, 0, 0]

# newField[0] = [1, 2, 2, 100, 10]
# newField[1] = [1, 1, 1, 100, 10]
# newField[24] = [2, 1, 1, 400, 10]
# newField[23] = [2, 2, 1, 400, 10]
# print("-------------------------------------------------")
# for element in newField:
#     print(newField[element])
# field1 = updateField(newField, None, None)
# for i in range(100):
#     print("-------------------------------------------------")
#     for element in field1:
#         print(field1[element])
#     field1 = updateField(field1, None, None)