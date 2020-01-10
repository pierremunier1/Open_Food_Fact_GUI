
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, desc , asc
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store, History
from api_data import Data
from prettytable import PrettyTable

class Controller:

    def __init__(self):

        self.api_data = Data()
        self.sql_setup = Sqlconnection()
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.value = None
        self.value_2 = None
        self.base = Product()

    def get_product(self):

        """show selectable product list"""

        field = 'category_name'
        self.product_list = []
        
        products = (self.session.query(Category.category_name,
                                        Product.brands,
                                        Product.product_name,
                                        Product.id, 
                                        Product.nutriscore_fr)
                                        .filter(getattr(Category, field)== self.value)
                                        .order_by(asc(Product.nutriscore_fr))
                                        .join(Product).limit(20))
        products = [" ID: "
                    +str(i[3])
                    +" : "
                    +i[2]
                    +" NUTRISCORE: "
                    +i[4].upper()
                    +" MARQUE: "
                    +i[1]
                    
                    for i in products]
                
        for product in products:
            self.product_list.append(product)

    def get_product_detail(self):

        """show the product detail"""

        field = 'id'
        self.product_detail = []

        products = (self.session.query(Store.store_name,
                                        Product.product_name,
                                        Product.quantity,
                                        Product.nutriscore_fr,
                                        Product.product_url,
                                        Product.brands,
                                        Product.id,
                                        )
                                        .join(Store.products)
                                        .filter(getattr(Product, field)== self.value)
                                        .limit(20))
                
        for product in products:
            self.product_detail.append(product)

    def get_product_substitute(self):
       
        """find the product substitute"""

        field = 'category_name'
        field_2 = 'nutriscore_fr'
        nutriscore = 'A'
        self.product_list = []
        self.history = []
        
        products = (self.session.query(Store.store_name,
                                        Product.product_name,
                                        Product.quantity,
                                        Product.nutriscore_fr,
                                        Product.product_url,
                                        Product.brands,
                                        Category.category_name,
                                        Product.id,
                                        )
                                        .filter(getattr(Category, field)== self.value_2)
                                        .filter(getattr(Product, field_2)== nutriscore)
                                        .order_by(asc(Product.nutriscore_fr))
                                        .join(Product).limit(3))
        
        products = [" ID: "+
                    str(i[7])
                    +" PRODUIT: "+
                    i[1]
                    +" MARQUE: "+
                    i[5]
                    +" NUTRISCORE: "+
                    i[3].upper()
                    +" QUANTITÉ: "+
                    i[2]
                    +" MAGASIN: "+
                    i[0]
                    +" URL: "+
                    i[4]
                    for i in products]

        for product in products:
            self.product_list.append(product)
            self.save_history()
    
    def save_history(self):

            pass