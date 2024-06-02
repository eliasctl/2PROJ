from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
from game.gameSingleplayer import gameSingleplayer
from game.gameMultiplayer import gameMultiplayer
from game.menu import menu
def main():
    difficulty = menu()
    idPlayer = createPlayer()
    idGame = gameBegin(idPlayer)
    gameWindow, screen_width, screen_height = init()
    match difficulty:
        case "easy":
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=0.5)
        case "medium":
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=0.7)
        case "difficult":
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=1)
        case "impossible":
            gameSingleplayer(gameWindow, screen_width, screen_height, idGame, idPlayer, difficulty=1.5)
        case "multiplayer":
            gameMultiplayer(gameWindow, screen_width, screen_height, idGame, idPlayer)
        case _:
            print("Invalid difficulty")
    
if __name__ == "__main__":
    main()