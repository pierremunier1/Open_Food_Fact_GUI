import requests
from sql_setup import Sqlconnection


class data:

    def __init__(self):

        self.sql_setup = Sqlconnection()
        

    
    def get_products_from_france(self):

        params = {
        "page" : 1,
        "page_size" : 10,
        "json" : 1,
        "search_terms" : "Lindt",
        "search_tag" : "brands"
        }
        res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params = params)
        
        result = res.json()
       
        products = result["products"]

        for product in products:
            print(product["product_name"]) 

        

        
