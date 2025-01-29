import os
import time
from utils.logger import log_event
from tools import nmap_scan, nikto_scan, metasploit_exploit, openvas_scan
from modules import (
    honeypot_detection, privilege_escalation, code_injection, 
    data_leakage, reverse_exploitation, service_crash, dos_attack, evading_logs
)

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
RESULTS_DIR = "results"

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

def user_input(prompt):
    """Handles user input with proper formatting"""
    return input(f"HoneyPott3r > {prompt}: ").strip()

def run_scan(scan_module, log_file):
    """Runs a scan and logs results"""
    log_event(f"Running {scan_module.__name__}...")
    results = scan_module.run()
    with open(f"{RESULTS_DIR}/{log_file}", "a") as f:
        f.write(results + "\n")
    log_event(f"{scan_module.__name__} completed.")

def run_attack(attack_module, log_file):
    """Runs an attack and logs results"""
    log_event(f"Executing attack module: {attack_module.__name__}...")
    results = attack_module.run()
    with open(f"{RESULTS_DIR}/{log_file}", "a") as f:
        f.write(results + "\n")
    log_event(f"{attack_module.__name__} completed.")

def main():
    print(BANNER)
    
    # Take user inputs
    test_name = user_input("Set the test name")
    honeypot_type = user_input("Set the honeypot type")
    honeypot_creds = user_input("Set the honeypot credentials")

    log_event(f"Test: {test_name} | Honeypot: {honeypot_type} | Credentials: {honeypot_creds}")
    
    print("\n[*] Testing initiated.....\n")
    time.sleep(2)

    # Run scanning tools
    run_scan(nmap_scan, "scan_results.log")
    run_scan(nikto_scan, "scan_results.log")
    run_scan(metasploit_exploit, "attack_exploits.log")
    run_scan(openvas_scan, "scan_results.log")

    # Run attack modules
    attack_modules = [
        honeypot_detection, privilege_escalation, code_injection, 
        data_leakage, reverse_exploitation, service_crash, dos_attack, evading_logs
    ]
    
    for attack in attack_modules:
        run_attack(attack, "attack_exploits.log")

    print("\n[+] Testing complete. Results stored in the results directory.")

if __name__ == "__main__":
    main()
