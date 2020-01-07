import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store

class Data:

    def __init__(self):
    
        self.sql_setup = Sqlconnection()
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.categories = ["pizza","pates","pates à tartiner","sauces"]
        self.stores = ["Casino","Carrefour","Monoprix","Naturalia"]

    def get_products_from_france(self):
        
        
        for store,category in zip(self.stores,self.categories):

            params = {
            "action" : "process",
            "tagtype_0" : "categories",
            "tag_contains_0" : "contains",
            "tag_0" : category,
            "tagtype_1" : "countries",
            "tag_contains_1" : "contains",
            "tag_1" : "france",
            "tagtype_2" : "stores",
            "tag_contains_2" : "contains",
            "tag_2": store,
            "page" : 1,
            "page_size" : 50,
            "json" : 1,
            }

            res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params = params)

            self.result = res.json()
            self.products = self.result['products']

            for product in self.products:
                
                self.products = [product.update(stores=store,
                                                categories=category) for product in self.result['products']]

                if not all(tag in product for tag in ('nutrition_grade_fr',
                                                    'quantity',
                                                    'url',
                                                    'brands',
                                                    'categories',
                                                    'code',
                                                    'product_name',
                                                    'stores')):
                                                    continue
                elif len(product['quantity']) == 0:
                    continue
                elif len(product['nutrition_grade_fr']) == 0:
                    continue
                elif len(product['stores'])== 0:
                    continue
            
                code = product['code']
                product_name = product['product_name']
                category_name = product['categories']
                nutriscore = product['nutrition_grade_fr']
                brands = product['brands']
                quantity = product['quantity']
                url = product['url']
                store_name = product['stores']

                c1 = Category(id=code,
                            category_name=category_name)
                        
                p1 = Product(id=code,
                            product_name=product_name,
                            brands = brands,
                            category = c1,
                            nutriscore_fr=nutriscore, 
                            quantity=quantity, 
                            product_url=url)

                p3 = Store(id=code,
                        store_name=store_name)
                p1.stores.append(p3)
                            
                self.session.add(p1)
            print("injection des données...ok")
            self.session.commit()


        
            
            

              
            
            