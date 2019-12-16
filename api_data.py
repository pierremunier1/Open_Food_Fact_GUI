import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store

class Data:

    def __init__(self):
    
        self.sql_setup = Sqlconnection()
        self.categories = ["pizza","pates","pates à tartiner","sauces"]
        
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.nutriscore = []

    def get_products_from_france(self):
        
        for categories in self.categories:

                params = {

                
                "action" : "process",
                "tagtype_0" : "categories",
                "tag_contains_0" : "contains",
                "tag_0" : categories,
                "tagtype_1" : "countries",
                "tag_contains_1" : "contains",
                "tag_1" : "france",
                "page" : 1,
                "page_size" : 100,
                "json" : 1,

                }
                res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params = params)
                
                result = res.json()

                self.products = result["products"]
                
                product = self.products


                for product in self.products:

                    product_name = product["product_name"]
                    nutriscore = product["nutrition_grade_fr"]
                    category_name = product["categories"]
                    brands = product["brands"]
                    quantity = product["quantity"]
                    #stores_names = product["stores"]
                    code = product["code"]
                    url = product["url"]

                

                    c1 = Category(id=code,
                                category_name=category_name)

                    p1 = Product(id=code,
                                brands=brands,
                                product_name=product_name,
                                category = c1,
                                nutriscore_fr=nutriscore, 
                                quantity=quantity, 
                                product_url=url)
                    
                    #for store in stores_names.split():
                        #p3 = Store(id=code,
                                #store_name=store)
                        #p1.stores.append(p3)
                                

                    self.session.add(p1)
                print("injection des données...ok")
                self.session.commit()

          

    

    

      



       
            

       