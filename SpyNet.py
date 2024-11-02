import os
import sys
import socket
import time
import json
import nmap
from getmac import get_mac_address
##Loading screen
def Loading():
    print("Loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]",\
                  "[■■■■□□□□□□]", "[■■■■■□□□□□]", \
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",\
                      "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(1.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
#The end Of Loading screen
#This function to clear the screen
def clearscreen():
    os.system("clear")

nocolor = "\033[0;37;10m"
azul = "\033[0;34;10m"
amarillo = "\033[1;33;10m"

#Main Menu class with the Banar and the choice of the first begin
class MainMenu:
    def Baner(self):
        baner = (azul + r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """).strip()
        print(baner)
        
        print( "****************************************")

    def Explain(self):
        print(amarillo + r"""THIS PROJECT UNDER  *GNU LICENSE*
IF THERE IS ANY ISSUE PLEASE CONTENT WITH US ON:
spynet4sc@gmail.com
READ MORE ON https://github.com/hotdeth/SpyNet 
****************************************      
""")
     
#Ask the user to Run or exit or show the requirements
    def choice(self):
        UserChoice = input(nocolor + """1-Run program
2-Show the requirement 
3-Exit
Input:""")
        return UserChoice
    def choice2(self):
        choice2 = input(nocolor + """1-Port checkout
2-Network Discover
Input:""")
        return choice2










class Discover:
   
    def __init__(self):
        self.ip = ''

    
    
    def get_mac_address(self,IP=''):
        mac = get_mac_address()

    def get_oui(self,mac):
        mac = mac[0:8]
        mac = mac.replace(':','-').upper()

        with open('oui.json') as oui_list:
            try:
                data = json.load(oui_list)
                return(data[mac])
            except:
                return("No match")





    def NetworkScan(self):
        ip = input("Your ip address(press enter to detect automaticlly):")
        self.ip = ip
        if len(self.ip) == 0:
            network = socket.gethostbyname(socket.gethostname())
            network = network + '/24'
        else:
            network = self.ip + '/24'

        print("Scanning Please Wait!")
        nm = nmap.PortScanner()
        Loading()
        nm.scan(hosts=network,arguments='-sn')
        host_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
        print("")
        n = 0
       
        print("HOST_NUMBER:    IP_ADD:                 MAC_ADD:                 OUI:")
        for host,status in host_list:
            mac = get_mac_address(ip=host,network_request=True)
           
            if mac is None:
                mac = get_mac_address()
                OUI = "YOUR DEVICE"
        
            OUI = self.get_oui(mac)

            print(f"Host:{n+1}\t\t{host}\t\tMAC:{mac}\t {OUI}")
            n +=1

         


class Port:
    pass



class Run:
    def __init__(self):
        self.menu = MainMenu()
        self.port = Port()
        self.Discover = Discover()




    def Start(self):
        self.menu.Baner()
        self.menu.Explain()
        
        choice = self.menu.choice()


        if choice == '1':
            clearscreen()
            self.menu.Baner()
            choice2 = self.menu.choice2()
            if choice2 == '1':
                #port checkout 
                pass
            elif choice2 == '2':
               self.Discover.NetworkScan()
              
            


        elif choice == '2':
            clearscreen()
            self.menu.Baner()
            #self.Show_file_content()
        elif choice == '3':
            self.exit()
        else:
            self.exit()
    #def Show_file_content(self):
        pass
    def exit(self):
        print(azul + "-----------------------------")
        print(azul + "Thank you for use SpyNet")
        print(azul + "See you late")    
User = Run()
User.Start()

