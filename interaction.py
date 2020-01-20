from sqlalchemy import exc
from colorama import Fore, Style
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from sql_setup import Sqlconnection
from base import Product, Category, Store, History
from api_data import Data


class Interaction:
    def __init__(self):

        self.api_data = Data()
        self.sql_setup = Sqlconnection()
        Session = sessionmaker(bind=self.sql_setup.engine)
        self.session = Session()
        self.value = None
        self.value_2 = None

    def insert_product(self, product):

        """check if produit exist in table history"""

        try:
            products = History(id=product)
            self.session.add(products)
            self.session.commit()
        except exc.IntegrityError:
            self.session.rollback()
            print(
                Fore.LIGHTRED_EX +
                "\n Produit(s) déjà présent(s) \n"
                + Style.RESET_ALL
            )
        else:
            self.session.commit()
            print(
                Fore.LIGHTGREEN_EX +
                "\n Produit(s) sauvegardé(s) \n"
                + Style.RESET_ALL
            )

    def get_product(self):

        """show selectable product list"""

        field = "category_name"
        self.product_list = []

        products = (
            self.session.query(
                Category.category_name,
                Product.product_name,
                Product.quantity,
                Product.nutriscore_fr,
                Product.product_url,
                Product.brands,
                Product.id,
            )
            .filter(getattr(Category, field) == self.value)
            .order_by(asc(Product.nutriscore_fr))
            .join(Product)
            .limit(20)
        )

        for product in products:
            self.product_list.append(product)

    def get_product_detail(self):

        """show the product detail"""

        field = "id"
        self.product_detail = []

        products = (
            self.session.query(
                Store.store_name,
                Product.product_name,
                Product.quantity,
                Product.nutriscore_fr,
                Product.product_url,
                Product.brands,
                Product.id,
            )
            .join(Store.products)
            .filter(getattr(Product, field) == self.value)
            .limit(1)
        )

        for product in products:
            self.product_detail.append(product)

    def get_product_substitute(self):

        """find the product substitute"""

        field = "category_name"
        field_2 = "nutriscore_fr"
        self.product_list = []
        nutriscore = "a"

        products = (
            self.session.query(
                Store.store_name,
                Product.product_name,
                Product.quantity,
                Product.nutriscore_fr,
                Product.product_url,
                Product.brands,
                Product.id,
                Category.category_name,
            )
            .filter(getattr(Category, field) == self.value_2)
            .filter(getattr(Product, field_2) == nutriscore)
            .order_by(asc(Product.nutriscore_fr))
            .join(Product)
            .limit(1)
        )

        for product in products:
            self.product_list.append(product)

    def save_history(self):

        """save the substitute product and the original
            in the history table"""

        for product in self.product_detail:
            self.insert_product(product[6])
            for product in self.product_list:
                self.insert_product(product[6])

    def show_history(self):

        """show the saved product into the history table"""

        self.history_result = []

        products = (
            self.session.query(
                Store.store_name,
                Product.product_name,
                Product.quantity,
                Product.nutriscore_fr,
                Product.product_url,
                Product.brands,
                History.id,
                Category.category_name,
            )
            .join(Product, Product.id == History.id)
            .join(Store, Store.id == History.id)
            .join(Category, Category.id == History.id)
            .order_by(asc(Category.category_name))
            .order_by(asc(Product.nutriscore_fr))
        )

        for history in products:
            self.history_result.append(history)

    def delete_history(self):

        """delete products in history table"""

        self.session.query(History).delete()
        self.session.commit()
