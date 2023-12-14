from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
from flask_cors import cross_origin


app = Flask(__name__)
CORS(app)

# Spoonacular API key
SPOON_API_KEY = 'd1dea6315e7941dd9ce6d6924f4f00d0'
# Target API key 
TARGET_API_KEY = 'D30EF50D4B06453384B60194C7EEAC5F'

#Spoonacular API Request
@app.route('/recipes', methods=['GET'])
#@cross_origin()
def get_recipes():
    ingredients = request.args.get('ingredients')
    
    # Make a request to Spoonacular API
    response = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOON_API_KEY}&ingredients={ingredients}')
    
    if response.status_code == 200:
        recipes = response.json()
        return (jsonify(recipes))  
    else:
        return jsonify({"error": "Error fetching recipes"})

#Target API request
@app.route('/getproduct', methods=['GET'])
#@cross_origin()
def search_products():
    api_key = 'TARGET_API_KEY'
    search_term = request.args.get('term')  # Get the search term from frontend?

    # Make a request to RedCircle API
    redcircle_url = f'https://api.redcircle.com/v1/products?search={search_term}'
    headers = {
        'api_key': {api_key},
        'type': 'search'
    }
    try:
        response = requests.get(redcircle_url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx or 5xx)

        return jsonify(response.json())  # Return the API response as JSON
    except requests.RequestException as e:
        return jsonify({'error': str(e)})  # Return an error message in JSON format
    
if __name__ == '__main__':
    app.run(debug=True)
