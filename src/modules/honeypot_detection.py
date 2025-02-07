import os
import subprocess
import socket
import json
import yaml
from pathlib import Path

class detectHoneypot:
    def __init__(self):
        self.config = self.load_config()
        self.signatures = self.load_signatures()

    def load_config(self):
        """Loads honeypot configuration from config.json."""
        config_path = Path(__file__).parent.parent / "configs" / "config.json"
        with open(config_path, "r") as file:
            return json.load(file)

    def load_signatures(self):
        """Loads honeypot detection signatures from signatures.yaml."""
        signature_path = Path(__file__).parent.parent / "configs" / "signatures.yaml"
        with open(signature_path, "r") as file:
            return yaml.safe_load(file)

    import subprocess

    def run_nc(self, command):
        """Executes a Netcat (nc) command and returns the output."""
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=5)
            return result.stdout.strip()  # Ensure output is captured properly
        except subprocess.TimeoutExpired:
            return "[!] Netcat command timed out."
        except Exception as e:
            return f"[!] Error running Netcat: {e}"


    def detect_cowrie(self, ip, port):
        """Detects Cowrie SSH honeypot by checking SSH banners via Netcat."""
        command = f'echo -e "\\n" | nc -w 5 -v {ip} {port}'
        response = self.run_nc(command)

        print(f"[*] Full Cowrie Response:\n{response}")  # Debugging print

        # Extract only the second line (SSH banner)
        response_lines = response.split("\n")
        if len(response_lines) > 1:
            ssh_banner = response_lines[1].strip()
        else:
            return False  # No valid SSH banner received

        print(f"[*] Extracted SSH Banner: {ssh_banner}")  # Debugging print

        for entry in self.signatures.get("2222", []):
            for step in entry.get("steps", []):
                if step.get("output") and step["output"].strip() == ssh_banner:
                    return True  # Cowrie detected
        return False



    def detect_conpot(self, ip, port):
        """Detects Conpot HTTP honeypot by sending a predefined HTTP request via Netcat."""
        command = f'echo -e "GET /index.html HTTP/1.1\\n\\n" | nc -v {ip} {port}'
        response = self.run_nc(command)

        print(f"[*] Conpot Response:\n{response}")  # Debugging print

        for entry in self.signatures.get("8800", []):
            for step in entry.get("steps", []):
                if step.get("output") and step["output"] in response:
                    return True  # Conpot detected
        return False

    def detect(self):
        """Main function to detect Cowrie (SSH) and Conpot (HTTP) honeypots using Netcat."""
        hp_type = self.config["honeypot_type"].lower()
        creds = self.config["honeypot_creds"]
        ip = creds["ip"]
        port = creds["ports"]

        if hp_type == "ssh":
            result = self.detect_cowrie(ip, port)
        elif hp_type == "http":
            result = self.detect_conpot(ip, port)
        else:
            result = False

        return "[*] Honeypot detected!" if result else "[*] No honeypot detected."

