from PIL import Image
from game.init import init
import pygame

gameWindow, screen_width, screen_height = init()
pygame.init()
pygame.display.set_caption("Game")
# pygame.draw.rect(gameWindow, (255, 0, 0), (screen_width/2, screen_height/2, 50, 50))

field = {0: [0, 0, 0, 0, 0], 1: [0, 0, 0, 0, 0], 2: [1, 2, 0, 0, 0], 3: [0, 0, 0, 0, 0], 4: [0, 0, 0, 0, 0], 5: [1, 5, 0, 0, 0], 6: [0, 0, 0, 0, 0], 7: [0, 0, 0, 0, 0], 8: [2, 4, 0, 0, 0], 
9: [0, 0, 0, 0, 0], 10: [0, 0, 0, 0, 0], 11: [2, 8, 0, 0, 0], 12: [0, 0, 0, 0, 0], 13: [0, 0, 0, 0, 0], 14: [0, 0, 0, 0, 0], 15: [0, 0, 0, 0, 0], 16: [0, 0, 0, 0, 0], 
17: [0, 0, 0, 0, 0], 18: [0, 0, 0, 0, 0], 19: [0, 0, 0, 0, 0], 20: [0, 0, 0, 0, 0], 21: [0, 0, 0, 0, 0], 22: [0, 0, 0, 0, 0], 23: [0, 0, 0, 0, 0], 24: [0, 0, 0, 0, 0]}

troopSize = min(screen_width, screen_height) // 19.5

pygame.draw.rect(gameWindow, (255,0,0), (screen_width // 7.2, screen_height // 1.17, troopSize, troopSize), 2)

# #Drrawing the field
for i in range(25):
    if field[i][0] == 1:
        pygame.draw.rect(gameWindow, (0,255,0), (screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize))
    elif field[i][0] == 2:
        pygame.draw.rect(gameWindow, (0,0,255), (screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize))
    else:
        pygame.draw.rect(gameWindow, (0,0,0), (screen_width // 7.2 + troopSize*i, screen_height // 1.17, troopSize, troopSize))


while True:
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.flip()
