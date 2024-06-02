from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
from game.gameSingleplayer import gameSingleplayer
from game.gameMultiplayerCreate import gameMultiplayerCreate
from game.gameMultiplayerJoin import gameMultiplayerJoin
from game.menu import menu
def main():
    difficulty = menu()
    match difficulty:
        case "easy":
            idPlayer = createPlayer()
            idGame = gameBegin(idPlayer)
            gameWindow, screen_width, screen_height = init()
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=0.5)
        case "medium":
            idPlayer = createPlayer()
            idGame = gameBegin(idPlayer)
            gameWindow, screen_width, screen_height = init()
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=0.7)
        case "difficult":
            idPlayer = createPlayer()
            idGame = gameBegin(idPlayer)
            gameWindow, screen_width, screen_height = init()
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=1)
        case "impossible":
            idPlayer = createPlayer()
            idGame = gameBegin(idPlayer)
            gameWindow, screen_width, screen_height = init()
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=1.5)
        case "multiplayer":
            idPlayer = createPlayer()
            idGame = gameBegin(idPlayer)
            gameWindow, screen_width, screen_height = init()
            # Create the game with the API but waiting for the second player
            gameMultiplayerCreate(gameWindow, screen_width, screen_height, idGame, idPlayer)
        case _ if isinstance(difficulty, int):  # Add this line to test if difficulty is an integer
            print("Joining multiplayer game")
            idPlayer = createPlayer()
            gameWindow, screen_width, screen_height = init()
            gameMultiplayerJoin(gameWindow, screen_width, screen_height, difficulty, idPlayer)
        case _:
            print("Invalid difficulty")
    
if __name__ == "__main__":
    idPlayer = createPlayer()
    idGame = gameBegin(idPlayer)
    gameWindow, screen_width, screen_height = init()
    gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=0.7)
    # main()