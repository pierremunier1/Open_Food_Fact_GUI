
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, desc , asc
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store
from api_data import Data
from prettytable import PrettyTable

class Controller:

    def __init__(self):

        self.api_data = Data()
        self.sql_setup = Sqlconnection()
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.value = None
        self.base = Product()

    def get_product(self):

        field = 'category_name'
        self.product_list = []
        

        products = (self.session.query(Category.category_name,
                                        Product.brands,
                                        Product.product_name, 
                                        Product.nutriscore_fr)
                                        .filter(getattr(Category, field)== self.value)
                                        .order_by(asc(Product.nutriscore_fr))
                                        .join(Product).limit(10))
        products = [i[2]for i in products]
                
        for product in products:
            self.product_list.append(product)

    def get_product_detail(self):

        field = 'product_name'
        self.product_detail = []

        products = (self.session.query(Store.store_name,
                                        Product.product_name,
                                        Product.quantity,
                                        Product.nutriscore_fr,
                                        Product.product_url,
                                        Product.brands,
                                        )
                                        .join(Store.products)
                                        .filter(getattr(Product, field)== self.value)
                                        .limit(10))
                
        for product in products:
            self.product_detail.append(product)

    def get_product_substitute(self):

        field = 'category_name'
        self.product_nutriscore = []

        products = (self.session.query(Category.category_name,
                                        Store.store_name,
                                        Product.product_name,
                                        Product.quantity,
                                        Product.nutriscore_fr,
                                        Product.product_url,
                                        Product.brands,
                                        )
                                        .join(Store.products)
                                        #.join(Product)
                                        .filter(getattr(Category, field)== self.value)
                                        #.order_by(asc(Product.nutriscore_fr))
                                        #.filter(Product.nutriscore_fr== self.nutriscore)
                                        .limit(10))
                                        
                
        for product in products:
            self.product_nutriscore.append(product)
            print(self.product_nutriscore)
            