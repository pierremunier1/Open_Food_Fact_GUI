from sql_setup import Sqlconnection
from api_data import Data
from console import App
from interaction import Interaction


class Openff:
    """class launch application in the terminal."""

    def __init__(self):
        """initializing variables."""
        self.sql_setup = Sqlconnection()
        self.api_data = Data()
        self.console = App()
        self.interaction = Interaction()


def main():
    """function launch the application."""
    openff = Openff()
    openff.console.welcome()


if __name__ == "__main__":
    main()
