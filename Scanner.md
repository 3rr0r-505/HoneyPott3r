# HoneyPott3r - Python Honeypot Project

## Project File Structure
Here's an overview of the main project directory and its structure:
```
honeypot-vuln-scanner/
│
├── README.md                  # Project Overview & Setup
├── requirements.txt           # List of Python dependencies
├── tools/                      # External tools & scripts
│   ├── nmap_scan.py            # Nmap scanning scripts
│   ├── nikto_scan.py           # Nikto vulnerability scanning script
│   ├── metasploit_exploit.py   # Metasploit exploit automation
│   └── openvas_scan.py         # OpenVAS vulnerability scanner script
│
├── modules/                    # Core attack modules
│   ├── honeypot_detection.py   # Honeypot fingerprinting
│   ├── privilege_escalation.py # Privilege escalation techniques
│   ├── code_injection.py       # Code injection attacks
│   ├── data_leakage.py         # Data leakage exploitation
│   ├── reverse_exploitation.py # Reverse exploitation of honeypots
│   ├── service_crash.py        # Service crashing exploits
│   ├── dos_attack.py           # DoS attack simulation
│   └── evading_logs.py         # Log evasion techniques
│
├── config/                     # Configurations for tools and modules
│   ├── nmap_config.yaml        # Nmap scanning options
│   ├── metasploit_config.yaml  # Metasploit configuration
│   └── openvas_config.yaml     # OpenVAS scan settings
│
├── results/                    # Logs and reports of scans and attacks
│   ├── scan_results.log        # Logs of vulnerability scan results
│   ├── attack_exploits.log     # Logs of exploit attempts
│   └── final_report.txt        # Final report for the honeypot
│
└── utils/                      # Helper functions & utilities
    ├── logger.py               # Logging functionality
    ├── network_utils.py        # Network-related utilities (e.g., port scan, ping)
    └── config_loader.py        # Load configuration files
```

## Supported Honeypots and Protocols

| **Honeypot**  | **Supported Protocols**       | **Purpose**                                              | **Repository**                                  |
|---------------|------------------------------|----------------------------------------------------------|------------------------------------------------|
| **Cowrie**    | SSH, Telnet                  | Emulates SSH/Telnet to capture brute force attacks.      | <a href="https://github.com/cowrie/cowrie" target="_blank">GitHub Link</a> |
| **Dionaea**   | SMB, HTTP, FTP, TFTP, MSSQL, MySQL | Catches malware and collects samples for analysis.       | <a href="https://github.com/DinoTools/dionaea" target="_blank">GitHub Link</a> |
| **Honeyd**    | TCP, UDP, ICMP               | Simulates multiple hosts and services on a network.      | <a href="https://github.com/DataSoft/Honeyd" target="_blank">GitHub Link</a> |
| **Glastopf**  | HTTP                         | Emulates vulnerable web servers to capture attack patterns. | <a href="https://github.com/mushorg/glastopf" target="_blank">GitHub Link</a> |
| **Conpot**    | Modbus, SNMP, BACnet, HTTP, FTP | Emulates SCADA/ICS systems for industrial protocols.     | <a href="https://github.com/mushorg/conpot" target="_blank">GitHub Link</a> |
| **T-Pot**     | Multi (Cowrie, Dionaea, etc.) | Multi-honeypot platform for various protocols.           | <a href="https://github.com/telekom-security/tpotce" target="_blank">GitHub Link</a> |
| **Wordpot**   | HTTP (WordPress)             | Emulates WordPress installations for CMS-specific attacks. | <a href="https://github.com/gbrindisi/wordpot" target="_blank">GitHub Link</a> |

---
