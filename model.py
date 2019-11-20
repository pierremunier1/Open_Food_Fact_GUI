from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy_utils import database_exists, create_database
import config

class Sqlconnection:

    def __init__(self):
        
        self.variable_tablename = config.TABLE_PRODUCT
        self.db_infos_user = config.USER
        self.db_infos_pwd = config.PWD
        self.db_infos_db = config.DB
        
    def connection_setup(self):
        
        """connection to database"""
        
        self.engine = create_engine('mysql+mysqlconnector://{username}:{password}@localhost/{database}'.format(
                username=self.db_infos_user,
                password=self.db_infos_pwd,
                database=self.db_infos_db,
                ))

        if not database_exists(self.engine.url):
            print('-> Database not found..')
            create_database(self.engine.url)
            print('-> Database succesfully created')
        
        self.engine.connect()
        self.metadata = MetaData(self.engine)
        print('-> Connected to database: ' + str(self.engine))

    def table_setup(self):

        """check if table exist and create if not"""

        table_exist = self.engine.dialect.has_table(self.engine, self.variable_tablename)
        print('-> Table "{}" exists: {}'.format(self.variable_tablename, table_exist))

            
        product = Table(self.variable_tablename, self.metadata,
                Column('id', Integer),
                Column('product_name', String(150)),
                Column('ingredient', String(150)),
                Column('nutriscore', String(1)),    
                schema=self.db_infos_db)
    
        if table_exist == True:
            product.drop(self.engine)
            print('-> Delete existing table..')

        product.create(self.engine)
        print('-> Table succesfully created!')