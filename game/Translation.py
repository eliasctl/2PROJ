from googletrans import Translator
import pygame

pygame.init()

# Define the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Language Selection")

# Define the button dimensions and positions
button_width = 200
additional_languages = ["English", "Espagnol", "Français", "Deutsch", "Italiano", "Português"]

button_height = 50
button_padding = 20

button_x = (screen_width - button_width) // 2
button_y = (screen_height - (button_height + button_padding) * len(additional_languages)) // 2

# Define the button colors
button_color = (0, 128, 255)
button_hover_color = (0, 0, 255)

# Create the buttons
buttons = []
for i, language in enumerate(additional_languages):
    button_rect = pygame.Rect(button_x, button_y + (button_height + button_padding) * i, button_width, button_height)
    button_text = language.upper()
    button_font = pygame.font.Font(None, 32)
    button = pygame.draw.rect(screen, button_color, button_rect)
    button_text = button_font.render(button_text, True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    buttons.append((button, language))

translator = Translator()

def translate_menu(menu, dest_language):
    translated_menu = []
    try:
        # Translate each item in the menu to the destination language
        for item in menu:
            translation = translator.translate(item, dest=dest_language).text
            translated_menu.append(translation)
    except Exception as e:
        print(f"Error translating menu: {e}")
    return translated_menu

menu = ["Hello, how are you?", "What would you like to order?", "Please wait for your food."]
# Default destination language code for each button
additional_languages_codes = ["en", "es", "fr", "de", "it", "pt"]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button, language in buttons:
                if button.collidepoint(mouse_pos):
                    print(f"Selected language: {language}")
                    # Find the index of the selected button and get the corresponding language code
                    button_index = buttons.index((button, language))
                    dest_language_code = additional_languages_codes[button_index]
                    # Translate the menu items to the selected language
                    translated_menu = translate_menu(menu, dest_language_code)
                    # Print the translated menu items
                    for i, translated_text in enumerate(translated_menu):
                        print(f"Menu item {i+1}: {translated_text}")

    pygame.display.flip()

pygame.quit()
