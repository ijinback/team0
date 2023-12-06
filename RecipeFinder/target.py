import os
import requests
from dotenv import load_dotenv

load_dotenv()

TARGET_KEY = os.getenv("TARGET_KEY") # Remember .env file!

def get_product(product):
    url = "https://api.redcircleapi.com/request"
    params = {
        'api_key': TARGET_KEY,
        'type': 'search',
        #String, the product/ingredient being searched for
        'search_term': product,
        #Order of products being displayed
        'sort_by': 'best_seller'
    }
    response = requests.get(url=url, params=params)
    return response.json()
