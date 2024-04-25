import pygame
import ctypes

# Initialize pygame 
pygame.init()

# Get the screen size
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

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
colorBackground = (50, 137, 250)
gameWindow.fill(colorBackground)

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
baseImage = pygame.image.load("game/tempImages/base.png")
leftBaseRect = baseImage.get_rect()
leftBaseRect.topleft = (0, screen_height // 1.8 - leftBaseRect.height // 2)
gameWindow.blit(baseImage, leftBaseRect)

rightBaseRect = baseImage.get_rect()
rightBaseRect.topright = (screen_width, screen_height // 1.8 - rightBaseRect.height // 2)
gameWindow.blit(baseImage, rightBaseRect)

# Life bar
font = pygame.font.Font(None, 24)
leftLifeBar = pygame.Rect(0, leftBaseRect.bottom, leftBaseRect.width, 20)
pygame.draw.rect(gameWindow, (255, 0, 0), leftLifeBar)
pygame.draw.rect(gameWindow, (0, 255, 0), leftLifeBar.inflate(-5, -5))

rightLifeBar = pygame.Rect(screen_width - rightBaseRect.width, rightBaseRect.bottom, rightBaseRect.width, 20)
pygame.draw.rect(gameWindow, (255, 0, 0), rightLifeBar)
pygame.draw.rect(gameWindow, (0, 255, 0), rightLifeBar.inflate(-5, -5))

# Life bar text
leftLifeText = font.render("XXXhp", True, (255, 255, 255))
leftLifeTextRect = leftLifeText.get_rect(center=(leftLifeBar.width // 2, leftLifeBar.centery + 25))
gameWindow.blit(leftLifeText, leftLifeTextRect)

rightLifeText = font.render("XXXhp", True, (255, 255, 255))
rightLifeTextRect = rightLifeText.get_rect(center=(screen_width - rightLifeBar.width // 2, rightLifeBar.centery + 25))
gameWindow.blit(rightLifeText, rightLifeTextRect)


# Screen refresh
pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()