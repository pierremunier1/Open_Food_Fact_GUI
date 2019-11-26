from sql_setup import Sqlconnection
from api_data import Data

class Openff:

    def __init__(self):
        
        self.sql_setup = Sqlconnection()
        self.api_data = Data()
    

  

def main():

    openff = Openff()
    openff.sql_setup.connection_setup()
    openff.sql_setup.table_check()
    openff.sql_setup.table_initializing()
    openff.api_data.get_products_from_france()
    
    
if __name__ == '__main__':
    main()