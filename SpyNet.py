import os
import sys
import socket
import time
import json
import nmap
from getmac import get_mac_address
from port import *

##loading screen
def loading():
    """This function for the loading screen"""
    print("loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]",\
                  "[■■■■□□□□□□]", "[■■■■■□□□□□]", \
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",\
                      "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(1.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
#The end Of loading screen
#This function to clear the screen
def clearscreen():
    """this function for the clear screen"""
    os.system("clear")
NOCOLOR = "\033[0;37;10m"
AZUL = "\033[0;34;10m"
AMAR = "\033[1;33;10m"
#Main Menu class with the Banar and the choice of the first begin
class MainMenu:
    """class for main menu options and choices"""
    def baner(self):
        """for the baner display"""
        baner = (AZUL + r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """).strip()
        print(baner)
        
        print( "****************************************")

    def explain(self):
        """method for the emails and some of these thing"""
        print(AMAR + r"""THIS PROJECT UNDER  *GNU LICENSE*
IF THERE IS ANY ISSUE PLEASE CONTENT WITH US ON:
spynet4sc@gmail.com
READ MORE ON https://github.com/hotdeth/SpyNet 
****************************************      
""")
     
#Ask the user to Run or exit or show the requirements
    def choice(self):
        """method for show of options"""
        userchoice = input(NOCOLOR + """1-Run program
2-Show the requirement 
3-Exit
Input:""")
        return userchoice
    def choice2(self):
        "method for the second ask"
        choice2 = input(NOCOLOR + """1-Port checkout
2-Network Discover
Input:""")
        return choice2
class Discover:
    """this class for the net discover"""
    def __init__(self):
        self.ip = ''
    def get_oui(self,mac):
        """this method to get the oui"""
        mac = mac[0:8]
        mac = mac.replace(':','-').upper()

        with open('oui.json',encoding='utf-8') as oui_list:
            try:
                data = json.load(oui_list)
                return(data[mac])
            except:
                return("No match")
    def networkscan(self):
        """this method for scan the network hosts"""
        ip = input("Your ip address(press enter to detect automaticlly):")
        self.ip = ip
        if len(self.ip) == 0:
            network = socket.gethostbyname(socket.gethostname())
            network = network + '/24'
        else:
            network = self.ip + '/24'

        print("Scanning Please Wait!")
        nm = nmap.PortScanner()
        loading()
        nm.scan(hosts=network,arguments='-sn')
        host_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
        print("")
        n = 0
       
        print("HOST_NUMBER:    IP_ADD:                 MAC_ADD:                 OUI:")
        for host, status in host_list:
            mac = get_mac_address(ip=host,network_request=True)
           
            if mac is None:
                mac = get_mac_address()
                oui = "YOUR DEVICE"
        
            oui = self.get_oui(mac)

            print(f"Host:{n+1}\t\t{host}\t\tMAC:{mac}\t {oui}")
            n +=1

class Run:
    """this class for run the program بالترتيب"""
    def __init__(self):
        self.menu = MainMenu()
        self.port = ''
        self.discover = Discover()
    def start(self):
        """this method for start the program"""
        self.menu.baner()
        self.menu.explain()  
        choice = self.menu.choice()
        if choice == '1':
            clearscreen()
            self.menu.baner()
            choice2 = self.menu.choice2()
            if choice2 == '1':
                ip_address , port_range = user()
                scanner = Port(ip_address , port_range)
                scanner.scan()


                #port checkout 
            elif choice2 == '2':
               self.discover.networkscan()
        elif choice == '2':
            clearscreen()
            self.menu.baner()
            #self.Show_file_content()
        elif choice == '3':
            self.exit()
        else:
            self.exit()
    #def Show_file_content(self):
    def exit(self):
        """this method to show the exit lines"""
        print(AZUL + "-----------------------------")
        print(AZUL + "Thank you for use SpyNet")
        print(AZUL + "See you late")    


User = Run()
User.start()


