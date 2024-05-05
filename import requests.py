import requests

barcode = "5449000214911"
api_url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

response = requests.get(api_url)
data = response.json()

if 'product' in data:
    produit = data['product']
    
    # Reste du code pour extraire les informations
    liste_mots_cles = produit['_keywords']
    allergens = produit['allergens']
    name_prod = produit['generic_name']
    liste_confirme_pour = produit['data_quality_warnings_tags']
    a=produit['selected_images']
    k=produit['nutriscore']
    """2021-data-energy
    fiber
    cheese
    water
    proteins
    sodium
    sugars
    nutriscore-2023-data-negatif_nutrients && positive_nutrients"""
    neg=produit['nutriscore']['2023']['data']['negative_nutrients']
    b=a['front']
    c=b['display']
    prod_image=c['en']
    processed_list = [element.replace('-', ' ').replace(':', ' ').replace('en', '') for element in liste_confirme_pour]
    text_string = ', '.join(processed_list)
    if allergens=="":
        allergens="None"
    print(neg)
else:
    print(f"Le code-barres {barcode} n'a pas été trouvé dans la base de données.")
