##################################################
# Note: main.py is not completed!
# Note: implement after completing modules! 
##################################################

#!/usr/bin/env python3

# importing libraries
import os
import sys
import time
import json
import datetime
from modules import detectHoneypot
from modules import revExploit
from modules import privEsc
from modules import DenialOfService
from modules import serviceCrash
from modules import logEvasion
from tools import msfScan
from tools import Scanners
# from tools import nmapScan, niktoScan, msfScan, openVASScan
# from modules import (
#     detectHoneypot, codeInjection, dataLeakage,
#     denialOfService, logsEvasion, privEsc, revExploit, tarBomb
# )
from utils import mongoLoader
from utils import Logger

# Check if the script is run as root (UID 0)
if os.geteuid() != 0:
    print("[!] This script requires sudo/root privileges. Restarting with sudo...")
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

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

            # os.makedirs("config", exist_ok=True)
            with open(config_path, "w") as config_file:
                json.dump(config_data, config_file, indent=4)

            print("\n[*] Testing initiated.....\n")
            time.sleep(2)

        # Initiating Scans
        elif command == "scan":
            logger = Logger()
            logger.start_logging() 

            with open(config_path, "r") as config_file:
                config_data = json.load(config_file)

            print("[*] Honeypot details:")
            print(f"\tTest name: {config_data["test_name"]}")       # Access test_name
            print(f"\tTimeStamp: {get_timestamp()}")       # Access test_name
            print(f"\tHoneypot prtocol: {config_data["honeypot_type"].upper()}")   # Access honeypot_type
            print(f"\tipV4: {config_data["honeypot_creds"]["ip"]}")         # Access IP address
            print(f"\tPort no: {config_data["honeypot_creds"]["ports"]}")      # Access ports
            print(f"\tSSH Username: {config_data["honeypot_creds"]["username"]}")   # Access username
            print(f"\tSSH Password: {config_data["honeypot_creds"]["password"]}")   # Access password
            print(f"\tHTTP-link: {config_data["honeypot_creds"]["http-link"]}")  # Access HTTP link
            print(f"\n[*] Running Scans and Attacks...\n")
            start_time = time.time()

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #       Run attack modules
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print("==================================")
            print("[+] Executing Attack Modules")
            print("==================================\n")
            # ================Honeypot Detection==================
            print("\n====================Honeypot Detection====================\n")
            detection = detectHoneypot()
            detection_result = detection.detect()
            print(detection_result)
            # ================Code Injection======================
            # print("\n====================Code Injection====================\n")
            # code_injection.codeInjection()
            # ================Data Leakage========================
            # print("\n====================Data Leakage====================\n")
            # data_leakage.dataLeakage()
            # ======================Log Evasion=======================
            print("\n====================Log Evasion====================\n")
            try:
                duration = float(input("[+] Enter log flood duration (in minutes): "))
                if duration <= 0:
                    print("[!] Invalid duration! Enter a positive number.")
                    sys.exit(1)
            except ValueError:
                print("[!] Invalid input! Please enter a number.")
                sys.exit(1)
            evader =  logEvasion(duration)
            evader_result = evader.evade()
            print("[+] here's the result of log evasion Attack:")
            print(evader_result)
            # ================Reverse Exploitation================
            # print("\n====================Reverse Exploitation====================\n")
            # exploit = revExploit()
            # revExplt_result = exploit.explt() # this is a list
            # print("\n\n")
            # print("[+] here's the result of Reverse Exploitation:")
            # print(revExplt_result)
            # print("\n\n")
            # print(type(revExplt_result))
            # ======================Service Crash=====================
            # print("\n====================Service Crash====================\n")
            # try:
            #     duration = int(input("[+] How long U wanna down service(in minutes): "))
            #     if duration <= 0:
            #         print("[!] Invalid duration! Enter a positive number.")
            #         sys.exit(1)
            # except ValueError:
            #     print("[!] Invalid input! Please enter a number.")
            #     sys.exit(1)
            # crusher = serviceCrash(duration)
            # crash_result = crusher.crash()
            # print("[+] here's the result of Service Crash Attack:")
            # print(crash_result)
            # ================Denial of Service Attack==============
            print("\n====================Denial of Service====================\n")
            try:
                duration = int(input("[+] How long U wanna run DOS (in minutes): "))
                if duration <= 0:
                    print("[!] Invalid duration! Enter a positive number.")
                    sys.exit(1)
            except ValueError:
                print("[!] Invalid input! Please enter a number.")
                sys.exit(1)
            dos = DenialOfService(duration)
            dos_result  = dos.attack()
            print("[+] here's the result of DoS Attack:")
            print(dos_result)
            # ================Privilege Escalation================
            print("\n====================Privilege Escalation====================\n")
            privChker = privEsc()
            privEsc_result = privChker.scanImage()
            print("\n\n[+]Privilege Escalation final report:")
            print(privEsc_result)
            print(f"\nCVE count: {len(privEsc_result)}")
            print(type(privEsc_result))
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================
            
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #       Run scanning tools
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print("==================================")
            print("[+] Executing Scanning Modules")
            print("==================================\n")
            # ================Scanning using Nmap, Nikto & WPscan=====================================
            try:
                nikto_duration = float(input("[+] how long U wanna run nikto scan (in minutes): "))
                wpscan_duration = float(input("[+] how long U wanna run WPscan (in minutes): "))
                if nikto_duration <= 0 or wpscan_duration <= 0:
                    print("[!] Invalid duration! Enter a positive number.")
                    sys.exit(1)
            except ValueError:
                print("[!] Invalid input! Please enter a number.")
                sys.exit(1)
            scanner = Scanners(nikto_duration,wpscan_duration)  # Create an instance of Scanners
            scan_results = scanner.scan()  # Start scanning based on honeypot type

            # Store results in separate variables
            nmap_result = None
            nikto_result = None
            wpscan_result = None

            if isinstance(scan_results, tuple):
                if len(scan_results) == 2:  # If only nmap and nikto run
                    nmap_result, nikto_result = scan_results
                elif len(scan_results) == 3:  # If all three scans run
                    nmap_result, nikto_result, wpscan_result = scan_results
            else:
                nmap_result = scan_results  # If only nmap runs

            # Print results
            print("\n\n\n[+] Scan Results:")
            if nmap_result:
                print("\n[+] Nmap Result:\n", nmap_result)
            if nikto_result:
                print("\n[+] Nikto Result:\n", nikto_result)
            if wpscan_result:
                print("\n[+] WPScan Result:\n", wpscan_result)
            # ==================Metasploit Scan================================
            msfModules = msfScan()
            msf_result = msfModules.msfScan(privEsc_result) # this is a list 
            print("\n\n")
            print("[+] here's the result of msf modules:")
            print(msf_result)
            print("\n\n\n")
            print(type(msf_result))
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #       Making report to upload
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
                    "nmap_scan": nmap_result,
                    "nikto_scan": nikto_result,
                    "wp_scan": wpscan_result,
                    "msf_scan": msf_result,
                    "openVAS_scan": "<openVAS-report>"
                },
                "attacks":
                {
                    "honeypot_detection": detection_result,  
                    "code_injection": "codeInjection_result",       
                    "data_leakage": "dataLeakage_result",
                    "evading_logs": evader_result,         
                    "reverse_exploitation": "revExploit_result", 
                    "service_crash": "tarBomb_result",       
                    "dos_attack": dos_result,           
                    "privilege_escalation": privEsc_result
                }
            }
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================
            # ====================#@!&*%?====================#@!&*%?===================#@!&*%?====================

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #       Running utils
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Create an instance of MongoLoader
            mongo_loader = mongoLoader()
            # Uploading report data to MongoDB using the MongoLoader class
            mongo_loader.upload(report_data)
            
            time.sleep(2)
            print("\n[+] Testing complete!\n")
            end_time = time.time()  # End timer
            duration = end_time - start_time  # Calculate duration
            minutes, seconds = divmod(duration, 60)
            print(f"[+] Execution time: {int(minutes)} min {seconds:.2f} sec")
            logger.stop_logging()
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
