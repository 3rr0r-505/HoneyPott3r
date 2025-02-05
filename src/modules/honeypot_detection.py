import os
import paramiko
import requests
import socket
import json
import yaml

class detectHoneypot:
    def __init__(self):
        self.config = self.load_config()
        self.signatures = self.load_signatures()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configs", "config.json")
        with open(config_path, "r") as file:
            return json.load(file)

    def load_signatures(self):
        signature_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configs", "signatures.yaml")
        with open(signature_path, "r") as file:
            return yaml.safe_load(file)

    def detect_ssh_honeypot(self, ip, port, username, password):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, port=port, username=username, password=password, timeout=5)
            client.close()
            return False
        except paramiko.ssh_exception.AuthenticationException:
            return False
        except Exception:
            try:
                with socket.create_connection((ip, port), timeout=5) as sock:
                    banner = sock.recv(1024).decode(errors='ignore')
                    for entry in self.signatures.get(str(port), []):
                        if entry['output'] in banner:
                            return True
            except Exception:
                return True
            return False

    def detect_http_honeypot(self, http_link):
        try:
            response = requests.get(http_link, timeout=5)
            for port, details in self.signatures.items():
                for entry in details:
                    if entry['output'] in response.text:
                        return True
            return False
        except requests.exceptions.RequestException:
            return True

    def detect(self):
        hp_type = self.config["honeypot_type"].lower()
        creds = self.config["honeypot_creds"]
        
        if hp_type == "ssh":
            result = self.detect_ssh_honeypot(creds["ip"], creds["ports"], creds["username"], creds["password"])
        elif hp_type == "http":
            result = self.detect_http_honeypot(creds["http-link"])
        else:
            result = False
        
        return "[*] Honeypot detected successfully" if result else "[*] Honeypot detection failed"
