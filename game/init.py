import sys
import pygame
import requests
import array
from PIL import Image
import pyglet 
def init(backgroundImage, baseImage):
    if backgroundImage == None:
        backgroundImage = pygame.image.load("game/tempImages/Caveman.jpg")
    if baseImage == None:
         baseImage = pygame.image.load("game/tempImages/base.png")

    # Set the URL
    url = 'http://eliascastel.ddns.net:3001'

    # Initialize pygame 
    pygame.init()

    # Get the screen size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h


    # Set the caption of the window
    pygame.display.set_caption("My Game")

    # Calculate the appropriate width and height while maintaining the aspect ratio
    aspect_ratio = screen_width / screen_height
    if screen_width / screen_height > aspect_ratio:
        width = int(screen_height * aspect_ratio)
        height = screen_height
    else:
        width = screen_width
        height = int(screen_width / aspect_ratio)

    # Create the window
    gameWindow = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    # Set the colors
    colorGrey = (128, 128, 128)
    # colorBackground = (50, 137, 250)
    # Load the background image
    backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
    gameWindow.blit(backgroundImage, (0, 0))

    pygame.mixer.music.load("Music\With Gun & Crucifix - Epic Rock Orchestral Music.mp3")
    pygame.mixer.music.play(-1)  # -1 loops the music indefinitely
    # Infos emplacement on the top left
    infosEmplacement = pygame.Rect(0, 0, screen_width // 5, screen_height // 10)
    pygame.draw.rect(gameWindow, colorGrey, infosEmplacement)

    # Experience text
    font = pygame.font.Font(None, 48)
    expText = font.render("XP: 0", True, (255, 255, 255))
    expText_rect = expText.get_rect(center=(infosEmplacement.width // 2, infosEmplacement.height // 4))
    gameWindow.blit(expText, expText_rect)

    # Gold text
    goldText = font.render("GOLD: 0", True, (255, 255, 255))
    goldText_rect = goldText.get_rect(center=(infosEmplacement.width // 2, infosEmplacement.height // 4 * 3))
    gameWindow.blit(goldText, goldText_rect)

    # Setting image on the top right
    settingImage = pygame.image.load("game/tempImages/parametre.png")
    settingImage = pygame.transform.scale(settingImage, (80, 80))  # Reducing the size of the image
    settingRect = settingImage.get_rect()
    settingRect.topright = (screen_width - 20 , 20)
    gameWindow.blit(settingImage, settingRect)
               
    # Base image on the left and right
    leftBaseRect = baseImage.get_rect()
    leftBaseRect.topleft = (0, screen_height // 1.3 - leftBaseRect.height // 2)
    gameWindow.blit(baseImage, leftBaseRect)

    rightBaseRect = baseImage.get_rect()
    rightBaseRect.topright = (screen_width, screen_height // 1.3 - rightBaseRect.height // 2)
    gameWindow.blit(baseImage, rightBaseRect)

    # Life bar
    font = pygame.font.Font(None, 24)
    leftLifeBar = pygame.Rect(0, leftBaseRect.bottom, leftBaseRect.width, 20)
    pygame.draw.rect(gameWindow, (255, 0, 0), leftLifeBar)
    pygame.draw.rect(gameWindow, (0, 255, 0), leftLifeBar.inflate(-5, -5))

    rightLifeBar = pygame.Rect(screen_width - rightBaseRect.width, rightBaseRect.bottom, rightBaseRect.width, 20)
    pygame.draw.rect(gameWindow, (255, 0, 0), rightLifeBar)
    pygame.draw.rect(gameWindow, (0, 255, 0), rightLifeBar.inflate(-5, -5))

    skeleton_warrior_img = pyglet.image.load_animation("pixelart/Troop/caveman gifs/skeletonwarriorwalk.gif")
    sprite = pyglet.sprite.Sprite(skeleton_warrior_img)
    # Troop 1
    troopSize = min(screen_width, screen_height) // 20
    troopRect = pygame.Rect(screen_width // 3.85 - troopSize // 2, screen_height * 4 // 4.1 - troopSize // 2, troopSize, troopSize)

    # Render and display the troop (action button)
    troop1 = font.render("1", True, (0, 0, 0))
    troop1_rect = troop1.get_rect(center=troopRect.center)
    gameWindow.blit(troop1, troop1_rect)
    pygame.draw.rect(gameWindow, (0,0,0), troopRect, 2)



    

    # Troop 2
    troop2Rect = pygame.Rect(screen_width // 3.15 - troopSize, screen_height * 4 // 4.1 - troopSize // 2, troopSize, troopSize)

    # Render and display the troop (action button)
    troop2 = font.render("2", True, (0,0,0))
    troop2_text_rect = troop2.get_rect(center=troop2Rect.center)
    gameWindow.blit(troop2, troop2_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), troop2Rect, 2)

    # Troop 3
    troop3Rect = pygame.Rect(screen_width // 2.8 - troopSize, screen_height * 4 // 4.1 - troopSize // 2, troopSize, troopSize)

    # Render and display the troop (action button)
    troop3 = font.render("3", True, (0,0,0))
    troop3_text_rect = troop3.get_rect(center=troop3Rect.center)
    gameWindow.blit(troop3, troop3_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), troop3Rect, 2)

    # Turrets 1
    turretsSize = min(screen_width, screen_height) // 20
    turretsRect = pygame.Rect(screen_width // 2.4 - turretsSize, screen_height * 4 // 4.1 - turretsSize // 2, turretsSize, turretsSize)

    # Render and display the turrets (action button)
    turrets1 = font.render("t1", True, (0,0,0))
    turrets1_text_rect = turrets1.get_rect(center=turretsRect.center)
    gameWindow.blit(turrets1, turrets1_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), turretsRect, 2)

    # Turrets 2
    turretsSize = min(screen_width, screen_height) // 20
    turretsRect = pygame.Rect(screen_width // 2.19 - turretsSize, screen_height * 4 // 4.1 - turretsSize // 2, turretsSize, turretsSize)

    # Render and display the turrets (action button)
    turrets2 = font.render("t2", True, (0,0,0))
    turrets2_text_rect = turrets2.get_rect(center=turretsRect.center)
    gameWindow.blit(turrets2, turrets2_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), turretsRect, 2)

    # Turrets 3
    turretsSize = min(screen_width, screen_height) // 20
    turretsRect = pygame.Rect(screen_width // 2.01- turretsSize, screen_height * 4 // 4.1 - turretsSize // 2, turretsSize, turretsSize)

    # Render and display the turrets (action button)
    turrets3 = font.render("t3", True, (0,0,0))
    turrets3_text_rect = turrets3.get_rect(center=turretsRect.center)
    gameWindow.blit(turrets3, turrets3_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), turretsRect, 2)

    # Turrets 4
    turretsSize = min(screen_width, screen_height) // 20
    turretsRect = pygame.Rect(screen_width // 1.86- turretsSize, screen_height * 4 // 4.1 - turretsSize // 2, turretsSize, turretsSize)

    # Render and display the turrets (action button)
    turrets4 = font.render("t4", True, (0,0,0))
    turrets4_text_rect = turrets4.get_rect(center=turretsRect.center)
    gameWindow.blit(turrets4, turrets4_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), turretsRect, 2)

    # Turrets 5
    turretsSize = min(screen_width, screen_height) // 20
    turretsRect = pygame.Rect(screen_width // 1.73- turretsSize, screen_height * 4 // 4.1 - turretsSize // 2, turretsSize, turretsSize)

    # Render and display the turrets (action button)
    turrets5 = font.render("t5", True, (0,0,0))
    turrets5_text_rect = turrets5.get_rect(center=turretsRect.center)
    gameWindow.blit(turrets5, turrets5_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), turretsRect, 2)

    # NewEra
    EraSize = min(screen_width, screen_height) // 20
    EraRect = pygame.Rect(screen_width // 1.56 - EraSize, screen_height * 4 // 4.1 - EraSize // 2, EraSize, EraSize)

    # Render and display the Era (action button)
    Era = font.render("E1", True, (0,0,0))
    Era_text_rect = Era.get_rect(center=EraRect.center)
    gameWindow.blit(Era, Era_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), EraRect, 2)

    # Special Attack
    SaSize = min(screen_width, screen_height) // 20
    SaRect = pygame.Rect(screen_width // 1.47 - SaSize, screen_height * 4 // 4.1 - SaSize // 2, SaSize, SaSize)

    # Render and display the Era (action button)
    Sa = font.render("Sa", True, (0,0,0))
    Sa_text_rect = Sa.get_rect(center=SaRect.center)
    gameWindow.blit(Sa, Sa_text_rect)
    pygame.draw.rect(gameWindow, (0,0,0), SaRect, 2)

    return gameWindow, screen_width, screen_height
