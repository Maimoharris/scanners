import os
from colorama import Fore, Back, Style
#Dracular's Recon Tool

print(Fore.GREEN+"This Tool Is written by Vlad Harrris Dracula")
print(Fore.GREEN+"This is a tool that help you in active scan of your target network")
def scan(ip):
    print(Fore.YELLOW+f"Performing nmap scan on {ip}")
    os.system(f"nmap -sV -A {ip}")
    print(Fore.YELLOW+f"Performing dirb scan on {ip}")
    os.system(f"dirb {ip}")
    print(Fore.RED+f"Performing nslookup on {ip}")
    os.system(f"nslookup {ip}")
    print(Fore.CYAN+f"Performing whois on {ip}")
    os.system(f"whois {ip}")
    print(Fore.MAGENTA+f"Performing nikto scan on {ip}")
    os.system(f"nikto -h {ip}")
    print(Fore.RED+f"Performing nikto ssl scan on {ip}")
    os.system(f"nikto -h {ip} -ssl")
    print(Fore.LIGHTBLUE_EX+(f"Perfoming DNS Enumerarion on {ip}"))
    os.system(f"dnsenum {ip}")
scan(input("Enter Your IP or Host Adddress:"))
