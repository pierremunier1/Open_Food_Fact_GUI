import requests


class data:
    
    def get_products_from_france(self):

        params = {
        "page" : 1,
        "page_size" : 1000
        }
        result = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params = params)
        print(result)
       
