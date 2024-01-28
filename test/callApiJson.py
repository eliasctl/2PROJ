import requests

url = "http://localhost:3001/image/7"

response = requests.get(url)
# #print(response.status_code)
# #print(response.json())
listResult = response.json()

# # affiche l'image en base64

# print(listResult[0]['image']['data'])
# # affiche l'image en base64
# #print(listResult.id)

# #ouvre une page et affiche l'image
# import base64
# import io
# from PIL import Image
# image = Image.open(io.BytesIO(base64.b64decode(listResult[0]['image']['data'][0])))
# image.show()

# im = Image.open(io.BytesIO(base64.b64decode(listResult[0]['image']['data'][0])))
# im.save('image.png', 'PNG')

from PIL import Image
import array
import os

def save_blob_as_png(blob, output_path):
    # Convertir la liste de bytes en tableau d'entiers non signés 8 bits (uint8)
    data = array.array('B', blob).tobytes()

    # Créer une image à partir des données
    image = Image.frombytes('RGB', (len(blob) // 3, 1), data)

    # Enregistrer l'image au format PNG
    image.save(output_path, format='PNG')


# Remplacez le chemin avec le chemin complet vers le dossier Téléchargements sur votre système Mac
telechargements_path = os.path.expanduser("~/Downloads")

# Exemple de blob (remplacez-le par votre propre blob)
exemple_blob = listResult[0]['image']['data']

# Chemin complet du fichier de sortie
output_file_path = os.path.join(telechargements_path, "image_output.png")

# Appel de la fonction pour enregistrer l'image
save_blob_as_png(exemple_blob, output_file_path)

print(f"L'image a été enregistrée avec succès à l'emplacement : {output_file_path}")
