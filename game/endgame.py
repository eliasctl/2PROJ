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
initial_font_size = 36
font = pygame.font.SysFont("Arial", initial_font_size, bold=True)

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
scroll_speed = 2

# Set up starting and ending y positions
start_y = SCREEN_HEIGHT + 100  # Starting y position
end_y = SCREEN_HEIGHT - 200  # Ending y position

# Background music
pygame.mixer.music.load("Music\Rick Astley - Never Gonna Give You Up (Instrumental) HD Audio.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Main loop
def run_game():
    y_position = start_y
    spacing = 60  # Initial spacing between lines
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw credits with adjusted spacing and font size
        for i, line in enumerate(credits):
            font_size = initial_font_size - i * 2  # Decrease font size gradually
            font = pygame.font.SysFont("Arial", max(18, font_size), bold=True)  # Minimum font size 18
            text_surface = font.render(line, True, WHITE)
            screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, y_position + i * spacing))

        # Update position and spacing
        y_position -= scroll_speed
        if y_position < end_y:
            spacing -= 0.1  # Decrease spacing towards the end

        # Exit the loop when credits reach the ending position
        if y_position < end_y - len(credits) * spacing:
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
