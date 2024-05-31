from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
from game.game import game
from game.menu import menu
# from game.menu import menu
def main():
    # #Displaying the menu
    menu()
    idPlayer = "1"
    idGame = gameBegin(idPlayer)

    # #Asking for player name 
    # idPlayer = createPlayer()
    # gameBegin(idPlayer)
    gameWindow = init()
    game(gameWindow, idGame, idPlayer)
    

if __name__ == "__main__":
    main()