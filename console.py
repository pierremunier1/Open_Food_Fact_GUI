from controller import Controller
import sys #this allows you to use the sys.exit command to quit/logout of the application


class App:

    def __init__(self):

        self.controller = Controller()


    def menu(self):
        print("************MAIN MENU**************")
        #time.sleep(1)
        print()

        choice = input("""
                        A: Select category
                        B: Choice a substitute product
                        C: Search product
                        D: Save search
                        Q: Quit/Log Out

                        Please enter your choice: """)

        if choice == "A" or choice =="a":
            choice = input("""
                              A: Pizza
                              B: Sauces
                              C: Pates à Tartiner
                              D: Pates

                        Please enter your choice: """)

        if choice == "A" or choice =="a":
            self.controller.value = 'pizza'
            self.controller.get_product()
        elif choice == "B" or choice =="b":
            self.controller.value = 'Sauces'
            self.controller.get_product()
        elif choice=="D" or choice=="d":
            pass
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("You must only select either A,B,C, or D.")
            print("Please try again")
            pass
    
