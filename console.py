from controller import Controller
from api_data import Data
from sql_setup import Sqlconnection
from sqlalchemy.orm import sessionmaker
from sql_setup import Sqlconnection
from base import Base , Product, Category, Store, History
from base import Base
import config
import sys 

class App:

    def __init__(self):

        self.controller = Controller()
        self.api_data = Data()
        self.api_data.categories
        self.sql_setup = Sqlconnection()
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.menu_substitute = None
    
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

    def input_product_detail(self,liste,validator):

        """give the detail of the selected product"""

        elements = [
                    " ID: "
                    +str(i[6])
                    +" : "+
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
        if self.menu_selectable == True:
            elements = [f"{i+1}: {element}" for i, element in enumerate(elements)]
            elements.append("\n>>> ")
            message = "\n".join(elements)
            while True:
                self.choice = input(message)
                if validator(liste, self.choice):
                    return liste [int(self.choice)-1]
                print(
                  "Choix non valide, veuillez choisir une des entrées proposées!"
                )
        else:
            elements.append("\n============================= Appuyer sur Entrer ============================")
            message = "\n".join(elements)
        self.choice = input(message)
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

        self.menu_selectable = False

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
            validator=self.is_valid,

        )
        self.sub_menu_product_substitute()
        
       
    def sub_menu_product_substitute(self):

        """show the substitute product"""
        self.menu_substitute = True
        self.menu_selectable = False
        
        
        print("\n SELECTION DE PRODUITS AVEC UN NUTRISCORE PLUS FAIBLE: \n")
        self.controller.get_product_substitute()
        self.choice = self.input_product_detail(
            self.controller.product_list,
            validator=self.is_valid,
        )

        self.sub_menu_history()

    def sub_menu_history(self):
        
        self.menu_selectable = False

        self.choice = self.input(
            config.HISTORY,
            validator=self.is_valid,
        )

        if self.choice == config.HISTORY[0]:
            self.controller.save_history()
            self.sub_menu_history()
        elif self.choice == config.HISTORY[1]:
            self.controller.show_history()
            self.input_product_detail(
                self.controller.history_result,
                validator=self.is_valid
            )
            self.sub_menu_history()
        elif self.choice == config.HISTORY[2]:
            self.menu_categories()
        elif self.choice == config.HISTORY[3]:
            quit

    
        

        