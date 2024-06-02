import time
import pygame
from googletrans import Translator
import webbrowser

def menu():
    pygame.init()

    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Game Menu")

    try:
        background_image = pygame.image.load("game/tempImages/menu.jpg")
        background_image = pygame.transform.scale(background_image, (window_width, window_height))
    except Exception as e:
        print(f"Error loading background image: {e}")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.Font(None, 28)
    translator = Translator()

    def translate_text(text, dest_language):
        try:
            translation = translator.translate(text, dest=dest_language)
            if translation is not None and translation.text is not None:  # Check if translation is successful
                return translation.text
            else:
                return text  # Return the original text if translation is unsuccessful
        except Exception as e:
            print(f"Error translating text: {e}")
            time.sleep(1)
            return text


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
            text_surface = font.render(translate_text(self.text, current_language), True, BLACK)
            text_rect = text_surface.get_rect(topleft=(self.rect.right + 10, self.rect.y))
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

        def toggle(self):
            self.checked = not self.checked

    class TextBox:
        def __init__(self, x, y, width, height, text, language="en"):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.language = language
            self.font = pygame.font.Font(None, 28)
            self.render_text()

        def update_text(self, new_text):
            self.text = new_text
            self.render_text()

        def update_language(self, language):
            self.language = language
            self.render_text()

        def render_text(self):
            translated_text = translate_text(self.text, self.language)
            lines = translated_text.split('\n')
            line_height = self.font.get_linesize()
            self.text_surfaces = [self.font.render(line, True, WHITE) for line in lines]
            self.text_rects = [text_surface.get_rect(topleft=(self.rect.x, self.rect.y + i * line_height)) for i, text_surface in enumerate(self.text_surfaces)]

        def draw(self):
            pygame.draw.rect(window, BLACK, self.rect)
            for i in range(min(len(self.text_surfaces), self.rect.height // self.font.get_linesize())):
                window.blit(self.text_surfaces[i], self.text_rects[i])

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
            range_ = self.max_value - self.min_value
            if range_ != 0:
                normalized_value = (self.value - self.min_value) / range_
                cursor_x = int(self.rect.x + normalized_value * self.rect.width)
                cursor_rect = pygame.Rect(cursor_x - 5, self.rect.y - 5, 10, self.rect.height + 10)
                pygame.draw.rect(window, BLACK, cursor_rect)
            text_surface = font.render(f"{translate_text(self.text, current_language)}: {self.value}", True, BLACK)
            text_rect = text_surface.get_rect(topleft=(self.rect.right + 10, self.rect.y))
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

        def update_value(self, new_value):
            normalized_position = (new_value - self.rect.x) / self.rect.width
            self.value = round(self.min_value + normalized_position * (self.max_value - self.min_value))

        def get_value(self):
            return self.value
        
    
    class Input:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text

        def draw(self):
            pygame.draw.rect(window, WHITE, self.rect)
            text_surface = font.render(self.text, True, BLACK)
            text_rect = text_surface.get_rect(center=self.rect.center)
            window.blit(text_surface, text_rect)

        def is_clicked(self, pos):
            # When the input box is clicked, the text should be editable
            return self.rect.collidepoint(pos) and self.text == ""
        
        def update_text(self, new_text):
            self.text = new_text

        def get_text(self):
            return self.text

    language_options = ["en", "fr", "es", "de", "it", "pt"]
    current_language = "en"
    desired_language_index = 0 

    start_button = Button(300, 300, 200, 50, "Start")
    settings_button = Button(300, 400, 200, 50, "Settings")
    instruction_button = Button(300, 500, 200, 50, "Instructions")
    return_button = Button(300, 500, 200, 50, "Return")
    singleplayer_button = Button(300, 300, 200, 50, "Singleplayer")
    multiplayer_button = Button(300, 400, 200, 50, "Multiplayer")
    easy_button = Button(300, 100, 200, 50, "Easy")
    medium_button = Button(300, 200, 200, 50, "Medium")
    difficult_button = Button(300, 300, 200, 50, "Difficult")
    impossible_button = Button(300, 400, 200, 50, "Impossible")
    help_button = Button(200, 200, 200, 30, "Send a message")
    translation_button = Button(200, 250, 200, 30, "Translate")
    create_game_button = Button(300, 300, 200, 50, "Create Game")
    join_game_button = Button(300, 400, 200, 50, "Join Game")
    join_confirm_button = Button(300, 400, 200, 50, "Confirm")

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
    """, current_language)

    checkbox1 = Checkbox(200, 50, 20, 20, "Low")
    checkbox2 = Checkbox(330, 50, 20, 20, "High")

    low_text_box = TextBox(230, 50, 50, 30, "Low")
    high_text_box = TextBox(360, 50, 50, 30, "High")
    video_text_box = TextBox(10, 50, 50, 30, "VIDEO SETTINGS")
    sfx_text_box = TextBox(10, 150, 50, 30, "SFX")
    music_text_box = TextBox(10, 100, 50, 30, "MUSIC")
    help_text_box = TextBox(10, 210, 50, 30, "HELP")
    language_text_box = TextBox(10, 260, 50, 30, "LANGUAGE")
    join_text_box = TextBox(10, 300, 50, 30, "JOIN GAME")

    slider = Slider(200, 150, 200, 20, 0, 100, 50, "SFX")
    slider2 = Slider(200, 100, 200, 20, 0, 100, 50, "Music")

    # Input box for joining a game
    join_input_box = Input(300, 300, 200, 50, "Enter game code")

    running = True
    menu_screen = True
    mode_screen = False
    instruction_screen = False
    settings_screen = False
    level_screen = False
    multiplayer = False
    join_screen = False

    current_language = "en"

    def update_button_texts(language):
        start_button.text = translate_text("Start", language)
        settings_button.text = translate_text("Settings", language)
        instruction_button.text = translate_text("Instructions", language)
        return_button.text = translate_text("Return", language)
        singleplayer_button.text = translate_text("Singleplayer", language)
        multiplayer_button.text = translate_text("Multiplayer", language)
        easy_button.text = translate_text("Easy", language)
        medium_button.text = translate_text("Medium", language)
        difficult_button.text = translate_text("Difficult", language)
        impossible_button.text = translate_text("Impossible", language)
        instructions_text_box.update_language(language)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_screen:
                    if start_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = True
                    elif settings_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        settings_screen = True
                    elif instruction_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        instruction_screen = True
                elif mode_screen:
                    if singleplayer_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = False
                        level_screen = True
                    elif multiplayer_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = False
                        mode_screen = False
                        multiplayer = True
                    elif return_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        mode_screen = False
                elif multiplayer:
                    if return_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        multiplayer = False
                    elif create_game_button.is_clicked(pygame.mouse.get_pos()):
                        print("Create game button clicked")
                        pygame.quit()
                        return "multiplayer"
                    elif join_game_button.is_clicked(pygame.mouse.get_pos()):
                        print("Join game button clicked")
                        multiplayer = False
                        join_screen = True
                elif join_screen:
                    if join_confirm_button.is_clicked(pygame.mouse.get_pos()):
                        # Take the input from the text box and join the game
                        print("Join confirm button clicked")
                        idGameJoin = int(input("Enter the game code: "))
                        pygame.quit()
                        return idGameJoin
                elif level_screen:
                    if easy_button.is_clicked(pygame.mouse.get_pos()):
                        print("Easy button clicked")
                        pygame.quit()
                        return "easy"
                    elif medium_button.is_clicked(pygame.mouse.get_pos()):
                        print("Medium button clicked")
                        pygame.quit()
                        return "medium"
                    elif difficult_button.is_clicked(pygame.mouse.get_pos()):
                        print("Difficult button clicked")
                        pygame.quit()
                        return "difficult"
                    elif impossible_button.is_clicked(pygame.mouse.get_pos()):
                        print("Impossible button clicked")
                        pygame.quit()
                        return "impossible"
                    elif return_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        level_screen = False
                elif instruction_screen or settings_screen:
                    if return_button.is_clicked(pygame.mouse.get_pos()):
                        menu_screen = True
                        instruction_screen = False
                        settings_screen = False
                    elif checkbox1.is_clicked(pygame.mouse.get_pos()):
                        checkbox1.toggle()
                    elif checkbox2.is_clicked(pygame.mouse.get_pos()):
                        checkbox2.toggle()
                    elif slider.is_clicked(pygame.mouse.get_pos()):
                        slider.update_value(pygame.mouse.get_pos()[0])
                    elif slider2.is_clicked(pygame.mouse.get_pos()):
                        slider2.update_value(pygame.mouse.get_pos()[0])
                        music_volume = slider2.get_value() * 0.01
                        pygame.mixer.music.set_volume(music_volume)
                    elif help_button.is_clicked(pygame.mouse.get_pos()):
                        email_url = "mailto:clovis.kouoi@supinfo.com;paul.mareschi@supinfo.com;adlane.benouhalima@supinfo.com;elias.moussa-osman@supinfo.com?subject=Help Request&body="
                        webbrowser.open(email_url)
                    elif translation_button.is_clicked(pygame.mouse.get_pos()):
                        desired_language_index = (desired_language_index + 1) % len(language_options)
                        dest_language_code = language_options[desired_language_index]
                        update_button_texts(dest_language_code)
                        current_language = dest_language_code
                        

        window.fill(BLACK)
        window.blit(background_image, (0, 0))

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
        elif mode_screen:
            singleplayer_button.draw()
            multiplayer_button.draw()
            return_button.draw()
        elif level_screen:
            easy_button.draw()
            medium_button.draw()
            difficult_button.draw()
            impossible_button.draw()
            return_button.draw()
        elif instruction_screen or settings_screen:
            return_button.draw()
        elif multiplayer:
            create_game_button.draw()
            join_game_button.draw()
            return_button.draw()
        elif join_screen:
            join_text_box.draw()
            join_input_box.draw()
            join_confirm_button.draw()
            return_button.draw()

        pygame.display.flip()

    pygame.quit()# quit game

# menu()
