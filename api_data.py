import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store

class Data:

    def __init__(self):

    
        self.sql_setup = Sqlconnection()
        self.categories = ["pizza","pates","pates à tartiner"]
        self.page = [1,2,3,4]

    def get_products_from_france(self):

        Session = sessionmaker(bind=self.sql_setup.engine)
        session = Session()
        
        for categories in self.categories:
            
            for page in self.page:

                params = {

                
                "action" : "process",
                "tagtype_0" : "categories",
                "tag_contains_0" : "contains",
                "tag_0" : categories,
                "tagtype_1" : "countries",
                "tag_contains_1" : "contains",
                "tag_1" : "france",
                "page" : page,
                "page_size" : 10,
                "json" : 1,

                }
                res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params = params)
                
                result = res.json()

                self.products = result["products"]

                for product in self.products:
                    product_name = product["product_name"]
                    nutriscore = product["nutrition_grade_fr"]
                    category_name = product["categories"]
                    quantity = product["quantity"]
                    brands = product["brands"]
                    store_name = product["stores"]
                    code = product["code"]
                    url = product["url"]
                
                    p1 = Product(id=code,
                                brands=brands,
                                product_name=product_name,
                                category_name=category_name,
                                nutriscore=nutriscore, 
                                quantity=quantity, 
                                store_name=store_name,
                                product_url=url)

                    p2 = Category(id=code,
                                category_name=category_name,
                                product_name=product_name)
                    
                    p3 = Store(id=code,
                                category_name=category_name,
                                product_name=product_name,
                                store_name=store_name)

                    session.add(p1)
                    session.add(p2)
                    session.add(p3)
                
                
        print("injection des données...ok")
        session.commit()
           
          

    

        

      



       
            

       