class Displayer:
    """ This class contains all methods to presents
        the informations based on what we get from
        our Model module
    """

    @staticmethod
    def _get_input():
        try:
            response = int(input('Sélectionnez une option du menu : '))
        except ValueError:
            response = 99
        return response

    @classmethod
    def main_menu(cls):
        """ Starting menu of the application
        """
        print("############################################################")
        print("###               Use Datas Open Food Fact               ###")
        print("############################################################")
        print("### 1. Quel aliment souhaitez-vous remplacer ?           ###")
        print("### 2. Retrouver mes aliments substitués.                ###")
        print("### 3. Quitter l'application.                            ###")
        print("############################################################")
        return cls._get_input()