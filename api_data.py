import requests
from sqlalchemy.orm import relationship, sessionmaker


class Data:

    def __init__(self):

        self.products = []
     
    
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
       
        self.products.append(result["products"])

        for product in self.products:
            self.products.append(product("product_name"))
            print(self.products)
        
        

   
        

        
