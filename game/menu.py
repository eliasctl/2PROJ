import pygame
from googletrans import Translator
import webbrowser
import subprocess


import pygame.mixer

def menu():
    # Initialisation de Pygame
    pygame.init()

    # Configuration de la fenêtre du jeu
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Game Menu")

    # Chargement de l'image de fond
    background_image = pygame.image.load("game/tempImages/Nature.png")
    # Redimensionnement de l'image de fond pour correspondre à la taille de la fenêtre
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    # Affichage de l'image de fond

    # Définition des couleurs
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Définition de la police
    font = pygame.font.Font(None, 28)

    # Initialize the translator
    translator = Translator()

    # Function to translate text to the chosen language
    def translate_text(text, dest_language):
        try:
            translation = translator.translate(text, dest=dest_language)
            return translation.text
        except ValueError:
            print(f"Error: {dest_language} is not a valid destination language.")
            return text
        except Exception as e:
            print(f"Error translating text: {e}")
            return text

    # Classe pour les boutons
    class Button:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text

        def draw(self):
            pygame.draw.rect(window, WHITE, self.rect)
            text_surface = font.render(self.text, True, BLACK)
            text_rect = text_surface.get_rect(center=self.rect.center)
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

    # Classe pour les cases à cocher
    class Checkbox:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.checked = False

        def draw(self):
            pygame.draw.rect(window, WHITE, self.rect)
            pygame.draw.rect(window, BLACK, self.rect, 2)

            if self.checked:
                pygame.draw.line(window, BLACK, (self.rect.x + 5, self.rect.centery), (self.rect.centerx, self.rect.bottom - 5), 2)
                pygame.draw.line(window, BLACK, (self.rect.centerx, self.rect.bottom - 5), (self.rect.right - 5, self.rect.y + 5), 2)

            text_surface = font.render(translate_text(self.text, current_language), True, BLACK)  # Translate text
            text_rect = text_surface.get_rect(topleft=(self.rect.right + 10, self.rect.y))
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

        def toggle(self):
            self.checked = not self.checked

    # Classe pour la boîte de texte
    class TextBox:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.font = pygame.font.Font(None, 28)
            self.render_text()

        def update_text(self, new_text):
            self.text = new_text
            self.render_text()

        def render_text(self):
            lines = self.text.split('\n')
            line_height = self.font.get_linesize()
            max_visible_lines = self.rect.height // line_height
            total_height = len(lines) * line_height
            self.text_surfaces = [self.font.render(line, True, WHITE) for line in lines]
            self.text_rects = [text_surface.get_rect(topleft=(self.rect.x, self.rect.y + i * line_height)) for i, text_surface in enumerate(self.text_surfaces)]

        def draw(self):
            pygame.draw.rect(window, BLACK, self.rect)
            for i in range(min(len(self.text_surfaces), self.rect.height // self.font.get_linesize())):
                window.blit(self.text_surfaces[i], self.text_rects[i])

    # Classe pour le curseur (slider)
    class Slider:
        def __init__(self, x, y, width, height, min_value, max_value, default_value, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.min_value = min_value
            self.max_value = max_value
            self.value = default_value
            self.text = text

        def draw(self):
            pygame.draw.rect(window, WHITE, self.rect)
            pygame.draw.rect(window, BLACK, self.rect, 2)

            # Calcul de la position du curseur en fonction de la valeur
            range_ = self.max_value - self.min_value
            if range_ != 0:
                normalized_value = (self.value - self.min_value) / range_
                cursor_x = int(self.rect.x + normalized_value * self.rect.width)
                cursor_rect = pygame.Rect(cursor_x - 5, self.rect.y - 5, 10, self.rect.height + 10)
                pygame.draw.rect(window, BLACK, cursor_rect)

            text_surface = font.render(f"{translate_text(self.text, current_language)}: {self.value}", True, BLACK)  # Translate text
            text_rect = text_surface.get_rect(topleft=(self.rect.right + 10, self.rect.y))
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

        def update_value(self, new_value):
            # Met à jour la valeur du curseur en fonction de la position du clic
            normalized_position = (new_value - self.rect.x) / self.rect.width
            self.value = round(self.min_value + normalized_position * (self.max_value - self.min_value))

        def get_value(self):
            # Return the current value of the slider
            return self.value

    # Liste de langues pour le menu déroulant
    # List of language options for the dropdown menu
    language_options = ["en", "fr", "es", "de", "it", "pt"]
    current_language = "en"  # Default language


    # Création des boutons
    start_button = Button(300, 300, 200, 50, "Start")
    settings_button = Button(300, 400, 200, 50, "Settings")
    instruction_button = Button(300, 500, 200, 50, "Instructions")
    back_button = Button(300, 500, 200, 50, "Back")
    singleplayer_button = Button(300, 300, 200, 50, "Singleplayer")
    multiplayer_button = Button(300, 400, 200, 50, "Multiplayer")
    easy_button = Button(300, 200, 200, 50, "Easy")
    hard_button = Button(300, 300, 200, 50, "Hard")
    impossible_button = Button(300, 400, 200, 50, "Impossible")
    help_button = Button(200, 200, 200, 30, "Send a message")
    translation_button = Button(200, 250, 200, 30, "Translate")

    # Création d'une boîte de texte pour les instructions avec des paragraphes
    instructions_text_box = TextBox(50, 50, 700, 400, """
    Age of War is an epic strategy game where you defend your base
    and conquer the enemy through five ages,from the Stone Age 
    to modern civilization.

    Game Highlights:
    - Battle across Stone, Castle, Renaissance, Modern, and Future ages.
    - Choose your difficulty level.
    - Defend with stones and sticks in the Stone Age and evolve.
    - Build turrets, deploy units, and strategically use special attacks.
    - Monitor the health bar; if it reaches zero, you lose.
    - Earn money and experience to unlock 16 different units.
    - Control the game with the left mouse button and toolbar.

    Features:
    - Engaging warfare across ages.
    - 16 units and 15 turrets.
    - Addictive and strategic gameplay.
    """)

    # Création des cases à cocher dans les paramètres
    checkbox1 = Checkbox(200, 50, 20, 20, "Low")
    checkbox2 = Checkbox(330, 50, 20, 20, "High")

    # Création de deux zones de texte pour les options Low et High dans les paramètres
    low_text_box = TextBox(230, 50, 50, 30, "Low")
    high_text_box = TextBox(360, 50, 50, 30, "High")
    video_text_box = TextBox(10, 50, 50, 30, "VIDEO SETTINGS")
    sfx_text_box = TextBox(10, 150, 50, 30, "SFX")
    music_text_box = TextBox(10, 100, 50, 30, "MUSIC")
    help_text_box = TextBox(10, 210, 50, 30, "HELP")
    language_text_box = TextBox(10, 260, 50, 30, "LANGUAGE")

    # Création du curseur (slider) dans les paramètres
    slider = Slider(200, 150, 200, 20, 0, 100, 50, "SFX")
    slider2 = Slider(200, 100, 200, 20, 0, 100, 50, "Music")

    # Boucle de jeu
    running = True
    menu_screen = True
    mode_screen = False
    instruction_screen = False
    settings_screen = False
    level_screen = False

    current_language = "English"  # Default language

    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_screen:
                    if start_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = True
                        print("Start button clicked")
                    elif singleplayer_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = False
                        level_screen = True
                    elif instruction_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        instruction_screen = True
                    elif settings_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        settings_screen = True
                elif mode_screen:
                    if singleplayer_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = False
                        level_screen = True
                        print("Singleplayer button clicked")
                    elif multiplayer_button.is_clicked(pygame.mouse.get_pos()):
                        print("Multiplayer button clicked")
                    elif back_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        instruction_screen = False
                        settings_screen = False
                elif level_screen:
                    if easy_button.is_clicked(pygame.mouse.get_pos()):
                        print("Easy button clicked")
                    elif hard_button.is_clicked(pygame.mouse.get_pos()):
                        print("Hard button clicked")
                    elif impossible_button.is_clicked(pygame.mouse.get_pos()):
                        print("Impossible button clicked")
                    elif back_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        mode_screen = False
                        level_screen = False
                elif instruction_screen or settings_screen:
                    if back_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        instruction_screen = False
                        settings_screen = False
                    elif checkbox1.is_clicked(pygame.mouse.get_pos()):
                        checkbox1.toggle()
                        print("Checkbox 1 toggled")
                    elif checkbox2.is_clicked(pygame.mouse.get_pos()):
                        checkbox2.toggle()
                        print("Checkbox 2 toggled")
                    elif slider.is_clicked(pygame.mouse.get_pos()):
                        # Met à jour la valeur du curseur en fonction de la position du clic
                        slider.update_value(pygame.mouse.get_pos()[0])
                    # Inside the loop where the slider is being updated
                    elif slider2.is_clicked(pygame.mouse.get_pos()):
                        slider2.update_value(pygame.mouse.get_pos()[0])
                        music_volume = slider2.get_value() * 0.01  
                        pygame.mixer.music.set_volume(music_volume)
                    if help_button.is_clicked(pygame.mouse.get_pos()):
                        # Open email client with pre-filled message
                        email_url = "mailto:clovis.kouoi@supinfo.com;paul.mareschi@supinfo.com;adlane.benouhalima@supinfo.com;elias.moussa-osman@supinfo.com?subject=Help Request&body=" 
                        webbrowser.open(email_url)
                    elif translation_button.is_clicked(pygame.mouse.get_pos()):
                        dest_language_code = language_options[1]  # Default to French
                        # Translate the interface elements to the selected language
                        translated_start_button = translate_text("Start", dest_language_code)
                        translated_settings_button = translate_text("Settings", dest_language_code)
                        translated_instruction_button = translate_text("Instructions", dest_language_code)
                        # Update the button texts with translations
                        start_button.text = translated_start_button
                        settings_button.text = translated_settings_button
                        instruction_button.text = translated_instruction_button
                        current_language = dest_language_code  # Update current language

                        # To get the index of the current language
                    current_language_index = language_options.index(current_language)

        # Effacer l'écran
        window.fill(BLACK) 

        # Dessiner les éléments de l'interface utilisateur en fonction de l'écran actuel et de la langue sélectionnée
        if instruction_screen:
            instructions_text_box.draw()
            

        if settings_screen:
            checkbox1.draw()
            checkbox2.draw()
            low_text_box.draw()
            high_text_box.draw()
            video_text_box.draw()
            sfx_text_box.draw()
            music_text_box.draw()
            language_text_box.draw()
            slider.draw()
            slider2.draw()
            help_button.draw() 
            help_text_box.draw()
            translation_button.draw()

        if menu_screen:
            start_button.draw()
            settings_button.draw()
            instruction_button.draw()
        elif mode_screen :
            singleplayer_button.draw()
            multiplayer_button.draw()
            back_button.draw()
        elif level_screen :
            easy_button.draw()
            hard_button.draw()
            impossible_button.draw()
            back_button.draw()
        elif instruction_screen or settings_screen:
            back_button.draw()

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter le jeu
    pygame.quit()

# Appeler la fonction menu pour démarrer le menu
menu()
