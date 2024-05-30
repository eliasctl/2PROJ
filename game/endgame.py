import pygame
import sys
import pygame.mixer

# Initialize Pygame
pygame.init()

# Set up display dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endgame Credits")

# Set up fonts
font = pygame.font.SysFont("Arial", 36 , bold=True)

# Set up colors
WHITE = (255, 255, 255)

# Set up credits
credits = [
    "Endgame Credits",
    "Directed by Your Name",
    "Produced by Producer Name",
    "Written by Writer Name",
    "Art Direction by Art Director Name",
    "Music by Composer Name",
    "Special Thanks to Special Thanks List",
    "And all the amazing contributors!",
]

# Set up scrolling speed
scroll_speed = 1
# Background music
pygame.mixer.music.load("Music\With Gun & Crucifix - Epic Rock Orchestral Music.mp3")
pygame.mixer.music.play(-1)

#The volume of the music
pygame.mixer.music.set_volume(0.5)


# Main loop
def run_game():
    y_position = SCREEN_HEIGHT
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw credits
        for i, line in enumerate(credits):
            text_surface = font.render(line, True, WHITE)
            screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, y_position + i * 40))

        # Update position
        y_position -= scroll_speed
        if y_position < -len(credits) * 40:
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
