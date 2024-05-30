from googletrans import Translator

translator = Translator()

def translate_menu(menu, dest_languages):
    translations = []
    for item in menu:
        item_translations = []
        for dest in dest_languages:
            translation = translator.translate(item, dest=dest)
            item_translations.append(translation.text)
        translations.append(item_translations)
    return translations


""" menu = ["Hello, how are you?", "What would you like to order?", "Please wait for your food."]
additional_languages = ["en", "es", "fr", "de", "it", "pt"]
result = translate_menu(menu, additional_languages)
print(result) """