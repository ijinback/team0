import os
import requests
from dotenv import load_dotenv

load_dotenv()

#.env file containing API Key 
SPOON_API_KEY = os.getenv("SPOON_API_KEY")

def get_recipe(ingredients, api_key):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        #NOTE: considering between having API key as a parameter entered when making request, or coding it into request automatically 
        "apiKey": api_key, 
        #String of ingredients, separated by commas
        "ingredients": ingredients,
        #Number of recipes to return after each search
        "number": 3
    }
    response = requests.get(url=url, params=params)
    return response.json()

