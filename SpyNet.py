from colorama import Fore, Back, Style
import os

#This function to clear the screen
def Clear_Screen():
    os.system("cls")


#Main Menu class with the Banar and the choice of the first begin
class MainMenu:
    def Begin(self):
        baner = (Fore.RED+ r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """)
        print(baner)
        print(Style.RESET_ALL)
        
        print( "****************************************")
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
        if UserChoice == '1':
            Clear_Screen()
        return UserChoice
    

#This class for the Discover Method only 
class Discover:
    pass




class Port:
    pass



class Run:
    pass


x = MainMenu()
x.Begin()
x.choice()












