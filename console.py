from controller import Controller
from api_data import Data
import sys 

class App:

    def __init__(self):

        self.controller = Controller()
        self.api_data = Data()
       

    def is_valid_category(self,liste, choice):
        
        if self.choice.isdigit() and 0 < int(choice):
            return True
        return False

    def input(self, liste, validator):

        elements = [f"{i+1}: {element}" for i, element in enumerate(liste)]
        elements.append("\n>>> ")
        message = "\n".join(elements)
    

        while True:
            self.choice = input(message)
            if validator(liste, self.choice):
                return liste[int(self.choice)-1]
            print(
                "Choix non valide, veuillez choisir une des entrées propoées!"
            )
    def show_product(self,liste):

        elements = [" PRODUCT: "+
                    i[2]
                    +" MARQUE: "+
                    i[1]
                    for i in liste]
        elements = [f"{i+1}:" for i, element in enumerate(liste)]
        message = "\n".join(elements)
        self.choice = input(message)
        return liste

    def show_product_detail(self,liste):

        elements = [
                    " PRODUIT: "+
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
                    for i in liste]

        message = "\n".join(elements)
        self.choice = input(message)
        return liste

    def start(self):

        self.choice = self.input(
            self.api_data.categories,
            validator=self.is_valid_category,
        )
        

        if self.choice in self.api_data.categories:
            self.controller.value = self.choice
            self.controller.get_product()

    def sub_menu(self):

        self.choice = self.input(
            self.controller.product_list,
            validator=self.is_valid_category
            
        )
        self.controller.value = self.choice
        self.controller.get_product_detail()
        
        self.choice = self.show_product_detail(
            self.controller.product_detail,
        )
    
    def substitute(self):
        pass