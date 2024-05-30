from googletrans import Translator

# Transmate.py

def translate_text(text, dest):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

