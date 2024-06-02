from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
from game.game import game
# from game.menu import menu
def main():
    # #Displaying the menu
    # Before the menu the player can select a name, if its empty : we choose player + the last id used and increment it
    # idPlayer = menu()
    idPlayer = "1"
    idGame = gameBegin(idPlayer)
    gameWindow, screen_width, screen_height = init()
    game(gameWindow, screen_width, screen_height, idGame, idPlayer)
    

if __name__ == "__main__":
    main()