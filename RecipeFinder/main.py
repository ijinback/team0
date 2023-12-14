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

@app.route('/editedrecipes', methods=['GET'])
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
    
if __name__ == '__main__':
    app.run(debug=True)
