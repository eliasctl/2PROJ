from game.createPlayer import createPlayer
from game.gameBegin import gameBegin
from game.init import init
from game.game import game
# from game.menu import menu
def main():
    # #Asking for player name 
    # idPlayer = createPlayer()
    # gameBegin(idPlayer)
    gameWindow = init()
    game(gameWindow)
    

if __name__ == "__main__":
    main()