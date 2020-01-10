from controller import Controller
from api_data import Data
from sql_setup import Sqlconnection
import config
import sys 

class App:

    def __init__(self):

        self.controller = Controller()
        self.api_data = Data()
        self.api_data.categories
        self.sql_setup = Sqlconnection()
    
    def is_valid(self,liste, choice):
        
        if self.choice.isdigit() and 0 < int(choice) <= len(liste):
            return True
        return False

    def input(self, liste, validator):

        """return the selectable products items list"""

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

    def input_product_detail(self,liste):

        """give the detail of the selected product"""

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
        self.choice =input(message)
        return liste

    def welcome(self):

        """update datas at the launch if necessary"""

        print("Voulez-vous mettre à jour les données produits?")

        self.choice = self.input(
            config.WELCOME,
            validator=self.is_valid,
            )
        if self.choice == "Oui":
            self.sql_setup.table_initializing()
            print("Mise à jour des données OpenFoodFact...")
            self.api_data.get_products_from_france()
            print("injection des données OK")
            self.menu_categories()
        else:
            self.menu_categories()

    def menu_categories(self):

        """show products category"""

        self.choice = self.input(
            self.api_data.categories,
            validator=self.is_valid,
        )
        self.sub_menu_products()

    def sub_menu_products(self):

        """show the product list after the category list
           selected"""

        if self.choice in self.api_data.categories:
                            self.controller.value = self.choice
                            self.controller.value_2 = self.choice
                            self.controller.get_product()

        self.choice = self.input(
            self.controller.product_list,
            validator=self.is_valid,
            
        )
        self.sub_menu_product_detail()      


    def sub_menu_product_detail(self):

        """show the product detail"""

        self.controller.value = self.choice.split()[1]
        self.controller.get_product_detail()
        print("\n DETAIL PRODUIT: \n")
        self.choice = self.input_product_detail(
            self.controller.product_detail,
        )
        self.sub_menu_product_substitute()
       
    def sub_menu_product_substitute(self):

        """show the substitute product"""
        
        self.controller.get_product_substitute()
        print("\n SELECTION DE PRODUITS AVEC UN NUTRISCORE PLUS FAIBLE: \n")
        self.choice = self.input(
            self.controller.product_list,
            validator=self.is_valid,
        )
        self.controller.value = self.choice.split()[1]
        self.controller.history.append(self.choice)
        print(self.controller.history)
    