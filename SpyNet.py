class MainMenu:
    def Begin(self):
        baner = (r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """)
        print(baner)
        print("****************************************")
        print(r"""THIS PROJECT UNDER  *GNU LICENSE*
IF THERE IS ANY ISSUE PLEASE CONTENT WITH US ON:
spynet4sc@gmail.com
READ MORE ON https://github.com/hotdeth/SpyNet 
****************************************      
""")

    def choice(self):
        UserChoice = input("""1-Run program
2-Show the requirement 
3-Exit
Input:""")
        return UserChoice
    


class Discover:
    pass


class Port:
    pass



class Run:
    pass


x = MainMenu()
x.Begin()
x.choice()












