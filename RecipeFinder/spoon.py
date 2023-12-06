import os
import requests
from dotenv import load_dotenv

load_dotenv()
print("Hello")
SPOON_API_KEY = os.getenv("SPOON_API_KEY") # Remember .env file!

def get_recipe(ingredients, api_key):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": api_key, 
        #String of ingredients, separated by commas
        "ingredients": ingredients,
        #Number of recipes to return after each search
        "number": 3
    }
    response = requests.get(url=url, params=params)
    return response.json()

"""test = get_recipe("flour, apples, eggs", SPOON_API_KEY)
print(test)"""