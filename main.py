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
    openff.console.welcome()
   
    
if __name__ == '__main__':
    main()

    