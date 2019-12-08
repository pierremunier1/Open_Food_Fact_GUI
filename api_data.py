import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product

class Data:

    def __init__(self):

    
        self.sql_setup = Sqlconnection()
        self.product_name = []
        
    def get_products_from_france(self):

        Session = sessionmaker(bind=self.sql_setup.engine)
        session = Session()
        
        params = {
        "page" : 1,
        "page_size" : 10,
        "json" : 1,
        "search_terms" : "Lindt",
        "search_tag" : "brands"
        }
        res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params = params)
        
        result = res.json()

        self.products = result["products"]

        for product in self.products:
            product_name = product["product_name"]
            nutriscore = product["nutrition_grade_fr"]
            categories = product["categories"]
            quantity = product["quantity"]
            stores = product["stores"]
            code = product["code"]
            url = product["url"]
        
            p1 = Product(id=code,
                        product_name=product_name,
                        #category_id=5,
                        category_name=categories,
                        nutriscore=nutriscore, 
                        quantity=quantity, 
                        stores=stores,
                        product_url=url)
            
            session.add(p1)
        print("injection des données...ok")
        session.commit()
           
          

    

        

      



       
            

       