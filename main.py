from sql_setup import Sqlconnection
from api_data import Data
from console import App
from controller import Controller

class Openff:

    def __init__(self):
        
        self.sql_setup = Sqlconnection()
        self.api_data = Data()
        self.console = App()
        self.controller = Controller()
    
def main():

    openff = Openff()
    if openff.sql_setup.table_check() == False:
        openff.sql_setup.table_initializing()
        openff.api_data.get_products_from_france()
    openff.console.start()
    openff.console.sub_menu()
   
    
if __name__ == '__main__':
    main()