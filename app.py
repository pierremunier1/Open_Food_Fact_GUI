from model import Sqlconnection

class Openff:

    def __init__(self):
        
        self.model = Sqlconnection()
  

def main():

    openff = Openff()
    openff.model.connection_setup()
    openff.model.table_setup()
    
    

if __name__ == '__main__':
    main()