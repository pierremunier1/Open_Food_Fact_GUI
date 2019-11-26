from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api_data import Data
import config
from base import Base


class Sqlconnection:

    def __init__(self):
        
        self.variable_table_product = config.TABLE_PRODUCT
        self.variable_table_category = config.TABLE_CATEGORY
        self.db_infos_user = config.USER
        self.db_infos_pwd = config.PWD
        self.db_infos_db = config.DB
        self.api_data = Data()
        
        

        
        
    def connection_setup(self):
        
        """connection to database"""
        
        self.engine = create_engine('mysql+mysqlconnector://{username}:{password}@localhost/{database}'.format(
                username=self.db_infos_user,
                password=self.db_infos_pwd,
                database=self.db_infos_db,
                ))

        self.session = sessionmaker(bind=self.engine)
        self.engine.connect()
        self.metadata = MetaData(self.engine)
        print('-> Connected to database: ' + str(self.engine))

    def table_check(self):

        """check if table exist and create if not"""

        table_exist = self.engine.dialect.has_table(self.engine, self.variable_table_product)
        print('-> Table "{}" exists: {}'.format(self.variable_table_product, table_exist))

        table_exist = self.engine.dialect.has_table(self.engine, self.variable_table_category)
        print('-> Table "{}" exists: {}'.format(self.variable_table_category, table_exist))

        if table_exist == True:
            Base.metadata.drop_all(self.engine)
        

    def table_initializing(self):

      

        # 2 - generate database schema
    
        Base.metadata.create_all(self.engine)
    
        # 3 - create a new session
        self.session = self.session()

        print(self.api_data.products)

        # 10 - commit and close session
        #self.session.commit()
        self.session.close()




        


        

      