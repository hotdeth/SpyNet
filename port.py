# yes yes it's looks similar but don't worry i put my own touched
import nmap
import ipaddress
import time
class Port:
    def __init__(self, ip_address, port_range):
        self.ip_address = ip_address
        self.port_range = port_range
        self.scanner = nmap.PortScanner()

    def scan(self):
        print(f"Scanning IP : {self.ip_address} , with range : {self.port_range}")
        self.scanner.scan(self.ip_address, self.port_range)
        self.display_result()  
    def display_result(self):
        resutl = self.scanner[self.ip_address]

        if "tcp" in resutl:
            for port in resutl["tcp"]:
                state = resutl["tcp"][port]["state"]
                print(f'Port {port} : {state}')
                time.sleep(0.7)
        else:
            print("No ports found in the range")

def user():
    while True:
        try:
            ip_address = input("Enter an IP address to you want to scan: ")
            ip = ipaddress.ip_address(ip_address)
            print(f"Valid IP address : {ip}")
            break
        except ValueError:
            print("You entered an Invalid IP address , chick and try again")

    port_range = input("Enter the port range you want to scan (ex:20-60) :")
    return ip_address, port_range
