from colorama import Fore, Back, Style
import os

#This function to clear the screen
def Clear_Screen():
    os.system("cls")


#Main Menu class with the Banar and the choice of the first begin
class MainMenu:
    def Baner(self):
        baner = (Fore.RED+ r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """)
        print(baner)
        print(Style.RESET_ALL)
        
        print( "****************************************")

    def Explain(self):
        print(r"""THIS PROJECT UNDER  *GNU LICENSE*
IF THERE IS ANY ISSUE PLEASE CONTENT WITH US ON:
spynet4sc@gmail.com
READ MORE ON https://github.com/hotdeth/SpyNet 
****************************************      
""")
     
#Ask the user to Run or exit or show the requirements
    def choice(self):
        UserChoice = input("""1-Run program
2-Show the requirement 
3-Exit
Input:""")
        return UserChoice
    def choice2(self):
        choice2 = input("""1-Port checkout
2-Network Discover
Input:""")
        return choice2
#This class for the Discover Method only 









class Discover:
    pass




class Port:
    pass



class Run:
    def __init__(self):
        self.menu = MainMenu()
        self.discover = Discover()
        self.port = Port()




    def Start(self):
        self.menu.Baner()
        self.menu.Explain()
        
        choice = self.menu.choice()


        if choice == '1':
            Clear_Screen()
            self.menu.Baner()
            choice2 = self.menu.choice2()
            if choice2 == '1':
                #port checkout 
                pass
            elif choice2 == '2':
                #Discover
                pass
            


        elif choice == '2':
            Clear_Screen()
            self.menu.Baner()
            self.Show_file_content()
    
        elif choice == '3':
            self.exit()
        else:
            self.exit()




    def Show_file_content(self):
        pass




    def exit(self):
        print(Fore.GREEN + "//\\//\\//\\//\\//\\//\\//\\")
        print(Fore.GREEN + "Thank you for use SpyNet")
        print(Fore.GREEN + "See you late")
        print(Style.RESET_ALL)
    




user = Run()
user.Start()






