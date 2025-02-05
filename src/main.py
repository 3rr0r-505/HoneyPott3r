##################################################
# Note: main.py is not completed!
# Note: implement after completing modules! 
##################################################

# importing libraries
import os
import sys
import time
import json
import datetime
# from tools import nmapScan, niktoScan, msfScan, openVASScan
# from modules import (
#     detectHoneypot, codeInjection, dataLeakage, 
#     denialOfService, logsEvasion, privEsc, revExploit, tarBomb
# )
from utils import mongoLoader

# Check if the script is run as root (UID 0)
# if os.geteuid() != 0:
#     print("[!] This script must be run as root. Please use 'sudo'.")
#     sys.exit(1)

# ASCII Banner
BANNER = r"""
#####################################################################################################
##     __  __                                      ____              __     __     _____           ##
##    / / / /  ____     ____     ___     __  __   / __ \   ____     / /_   / /_   |__  /   _____   ##
##   / /_/ /  / __ \   / __ \   / _ \   / / / /  / /_/ /  / __ \   / __/  / __/    /_ <   / ___/   ##
##  / __  /  / /_/ /  / / / /  /  __/  / /_/ /  / ____/  / /_/ /  / /_   / /_    ___/ /  / /       ## 
## /_/ /_/   \____/  /_/ /_/   \___/   \__, /  /_/       \____/   \__/   \__/   /____/  /_/        ##
##                                    /____/                                                       ## 
#####################################################################################################                                
"""

# Menu 
MENU = r"""
[#] Welcome to HoneyPott3r! developed by 5pyd3r!!
[#] Here's the list of operations.

[!] Scans:
[1] Nmap scan
[2] Nikto scan
[3] OpenVAS scan
[4] Metasploit scan

[!] Attacks:
[1] Honeypot Detection
[2] Code Injection
[3] Data Leakage
[4] Denial of Service
[5] Evading Logs
[6] Service Crash
[7] Reverse Exploitation
[8] Privilege Escalation

[!] Commands:
[1] To Start the Scan use 'start'
[2] To run the Scan use 'scan'
[3] To reset the credentials use 'reset'
[4] To Exit use 'exit'
"""

# Get the absolute path of the directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Ensure config is inside src/
config_dir = os.path.join(BASE_DIR, "configs")
os.makedirs(config_dir, exist_ok=True)
config_path = os.path.join(config_dir, "config.json")

def get_timestamp():
    """Returns a timestamp string for folder naming."""
    return datetime.datetime.now().strftime("%Y-%m-%d::%H:%M:%S")

def user_input(prompt):
    """Handles user input with proper formatting"""
    return input(f"HoneyPott3r > {prompt}: ").strip().lower()

def main():
    print(BANNER)  # Show banner initially
    print(MENU)  # Show menu initially
    
    while True:
        command = user_input("Enter your command")

        # Start the test
        if command == "start": # Always show menu after each scan
            
            # Take user inputs for test parameters
            test_name = user_input("Set the test name")
            honeypot_type = user_input("Set the honeypot type")
            user_input("::Set the honeypot credentials (press enter):")
            ipv4 = user_input("Set the honeypot ipv4 address [if not available, type 'null']")
            port_no = user_input("Set the honeypot port no [if not available, type 'null']")
            uname = user_input("Set the honeypot username [if not available, type 'null']")
            passwd = user_input("Set the honeypot password [if not available, type 'null']")
            link = user_input("Set the honeypot http-link [if not available, type 'null']")

            config_data = {
                "test_name": test_name,
                "honeypot_type": honeypot_type,
                "honeypot_creds": {
                    "ip": ipv4,
                    "ports": port_no,
                    "username": uname,
                    "password": passwd,
                    "http-link": link
                }
            }
            os.makedirs("config", exist_ok=True)
            with open(config_path, "w") as config_file:
                json.dump(config_data, config_file, indent=4)

            print("\n[*] Testing initiated.....\n")
            time.sleep(2)

        # Initiating Scans
        elif command == "scan":
            print("\n[*] Running Scans and Attacks...\n")

            # # Run scanning tools
            # nmap_scan.nmap()
            # openvas_scan.openvas()
            # nikto_scan.nikto()
            # metasploit_exploit.msf()

            # # Run attack modules
            # detection = detectHoneypot()
            # detection_result = detection.detect() 
            # privilege_escalation.privilegeEscalation()
            # code_injection.codeInjection()
            # data_leakage.dataLeakage() 
            # reverse_exploit.reverseExploit() 
            # service_crash.serviceCrash() 
            # dos_attack.dos() 
            # evading_logs.logsEvade()
            
            # [!] report format
            report_data = {
                "name": test_name,
                "Date&Time": get_timestamp(),
                "used creds": 
                {
                    "ipv4": ipv4,
                    "port": port_no,
                    "username": uname,
                    "password": passwd,
                    "http-link": link
                },
                "scans": 
                {
                    "nmap_scan": "<nmap-report>",
                    "openVAS_scan": "<openVAS-report>",
                    "nikto_scan": "<nikto-report>",
                    "msf_scan": ["cve-1","cve-2","cve-3","cve-4"]
                },
                "attacks":
                {
                    "honeypot_detection": "detection_result",  
                    "code_injection": "codeInjection_result",       
                    "data_leakage": "dataLeakage_result",
                    "evading_logs": "logEvasion_result",         
                    "reverse_exploitation": "revExploit_result", 
                    "service_crash": "tarBomb_result",       
                    "dos_attack": "dos_result",           
                    "privilege_escalation": "privEsc_result"
                }
            }
            
            # Create an instance of MongoLoader
            mongo_loader = mongoLoader()
            # Uploading report data to MongoDB using the MongoLoader class
            mongo_loader.upload(report_data)
            
            time.sleep(2)
            print("\n[+] Testing complete!\n")
            time.sleep(2)
            print(MENU) 

        # Reset the Credentials
        elif command == "reset":
            print("[!] Resetting credentials...")
            if os.path.exists(config_path):
                os.remove(config_path)
                print("[+] Credentials have been reset.\n")
            else:
                print("[!] No existing credentials to reset.\n")

        # Exit the loop and terminate the script
        elif command == "exit":
            print("[!] Exiting HoneyPott3r...")
            break  

        else:
            print("[!] Invalid command. Please try again.")

if __name__ == "__main__":
    main()
