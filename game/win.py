import pygame
import subprocess
def create_victory_screen():
    # Initialize Pygame
    pygame.init()

    # Set up the window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Victory Screen")

    # Set up the font
    font = pygame.font.Font(None, 48)

    # Set up the victory message
    victory_text = font.render("YOU WON!", True, (255, 255, 255))
    victory_text_rect = victory_text.get_rect(center=(window_width // 2, window_height // 2))

    # Set up the close button
    close_button_text = font.render("Close", True, (255, 255, 255))
    close_button_rect = close_button_text.get_rect(center=(window_width // 2, window_height // 2 + 100))

    # Set up the restart button
    restart_button_text = font.render("Restart", True, (255, 255, 255))
    restart_button_rect = restart_button_text.get_rect(center=(window_width // 2, window_height // 2 + 200))

    # Load the victory image
    victory_image = pygame.image.load("pixelart/victory.png")
    victory_image_rect = victory_image.get_rect(center=(window_width // 2, window_height // 2 - 100))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if close_button_rect.collidepoint(mouse_pos):
                    running = False
                elif restart_button_rect.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "game\menu.py"])
                    running = False

        # Clear the screen
        window.fill((0, 0, 0))

        # Draw the victory image, message, and buttons
        window.blit(victory_image, victory_image_rect)
        window.blit(victory_text, victory_text_rect)
        window.blit(close_button_text, close_button_rect)
        window.blit(restart_button_text, restart_button_rect)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

# Call the function to create the victory screen
# create_victory_screen()