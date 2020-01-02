
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

    def get_product(self):

        field = 'category_name'
        
        products = (self.session.query(Category.category_name,Product.product_name, Product.nutriscore_fr)
                    .filter(getattr(Category, field)== self.value)
                    .order_by(asc(Product.nutriscore_fr))
                    .join(Product).limit(10))
        for product in products:
            print(product.product_name,product.nutriscore_fr)
            


       
        
