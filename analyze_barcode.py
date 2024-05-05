from PIL import Image
from pyzbar.pyzbar import decode

def analyze_barcode(image_path):
    # Ouvrir l'image avec PIL
    pil_image = Image.open(image_path)

    # Décoder tous les codes-barres présents dans l'image
    decoded_objects = decode(pil_image)

    if decoded_objects:
        # Si des codes-barres sont détectés, retourne une liste de résultats
        return [obj.data.decode("utf-8") for obj in decoded_objects]
    else:
        # Si aucun code-barres n'est détecté, retourne un message indiquant cela
        return "Aucun code-barres détecté dans l'image."
