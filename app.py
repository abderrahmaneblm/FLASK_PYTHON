from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product_info', methods=['POST'])
def product_info():
    barcode = request.form['barcode']
    api_url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    
    response = requests.get(api_url)
    data = response.json()

    if 'product' in data:
        produit = data['product']
        allergens = produit['allergens']
        if allergens=="":
            allergens="None"
        name_prod = produit['generic_name']
        liste_confirme_pour = produit['data_quality_warnings_tags']
        processed_list = [element.replace('-', ' ').replace(':', ' ').replace('en', '') for element in liste_confirme_pour]
        liste_confirme_pour = ', '.join(processed_list)
        prod_image=produit['selected_images']['front']['display']['en']
        neg=produit['nutriscore']['2023']['data']['negative_nutrients']
        neg = ', '.join(neg)
        pos=produit['nutriscore']['2023']['data']['positive_nutrients']
        pos = ', '.join(pos)
        return render_template('product_info.html', barcode=barcode, name_prod=name_prod, allergens=allergens, warnings=liste_confirme_pour,prod_image=prod_image,pos=pos, neg=neg)
    else:
        return render_template('product_info.html', barcode=barcode, not_found=True)

if __name__ == '__main__':
    app.run(debug=True)
