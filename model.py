from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
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
                database=self.db_infos_db))
        self.engine.connect()
        self.metadata = MetaData(self.engine)
        print('connected to database: ' + str(self.engine))


    def table_setup(self):

        """check if table exist and create if not"""

        table_exist = self.engine.dialect.has_table(self.engine, self.variable_tablename)
        print('Table "{}" exists: {}'.format(self.variable_tablename, table_exist))

            
        table = Table(self.variable_tablename, self.metadata,
                Column('user_id', Integer),
                Column('first_name', String(150)),
                Column('last_name', String(150)),
                Column('last_TEST', String(150)),    
                schema=self.db_infos_db)
    
        if table_exist == True:
            table.drop(self.engine)

        table.create(self.engine)