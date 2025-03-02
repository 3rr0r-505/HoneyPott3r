# HoneyPott3r - Python Honeypot Vulnerability Scanner Project
**HoneyPott3r** is a tool designed to identify and analyze vulnerabilities in popular honeypot frameworks. It leverages integrated Kali Linux tools and custom attack vectors to simulate real-world threats, enabling researchers and security teams to test the resilience of their honeypots effectively.

---

## Project File Structure
Here's an overview of the main project directory and its structure:
```
HoneyPott3r/src/  
│  
├── main.py                     # Main entry point for the tool   
│  
├── tools/                      # External tools & scripts  
│   ├── scanners.py             # Script for Nmap, Nikto, and WPScan vulnerability scanning  
│   └── msf_scan.py             # Script to find Metasploit modules related to vulnerabilities  
│  
├── modules/                    # Core attack modules  
│   ├── honeypot_detection.py   # Honeypot fingerprinting techniques  
│   ├── code_injection.py       # Code injection attack methods  
│   ├── data_leakage.py         # Exploitation techniques for data leakage  
│   ├── privilege_escalation.py # Techniques for privilege escalation  
│   ├── reverse_exploitation.py # Methods to exploit honeypots in reverse  
│   ├── dos_attack.py           # DoS attack simulation methods  
│   └── evading_logs.py         # Techniques for log evasion  
│  
├── config/                     # Configuration files for tools and modules  
│   ├── honeypots.yaml          # Repository links for known honeypots  
│   ├── injection-cmd.yaml      # Code injection commands & expected responses  
│   ├── leakage-cmd.yaml        # Data leakage commands & expected responses  
│   └── signatures.yaml         # Signatures to detect honeypots  
│  
├── dashboard/                  # Web-based dashboard for viewing scan reports  
│   ├── dashboard.py            # Flask script to run the dashboard server  
│   └── templates/              # HTML templates for rendering dashboard pages  
│       ├── index.html          # Template for listing all scan reports  
│       ├── dashboard.html      # Template for displaying a summary view of a report  
│       └── report.html         # Template for viewing the complete details of a report  
│  
└── utils/                      # Helper functions & utilities  
    ├── logger.py               # Logging functionality  
    ├── mongo_loader.py         # Script to load reports into MongoDB  
    └── config_loader.py        # Script to load configuration files  

```
---

## Project Workflow
Here’s the workflow of your tool:
```
Start Tool
   ↓
Get User Input (Target IP/Range)
   ↓
Network Scanning (e.g., Nmap, OpenVAS)
   ↓
Analyze Responses for Honeypot Indicators
   ↓
   ├── Detect Common Honeypot Frameworks (e.g., Cowrie, Dionaea)
   │       ↓
   │   Match Honeypot Signatures (Banners, Ports, Behaviors)
   ↓
Simulate Attacks
   ├── Code Injection → Analyze Logs/Responses
   ├── DoS/Service Crash → Observe Honeypot Behavior
   ├── Privilege Escalation → Check Response to Exploits
   ├── Reverse Exploitation → Honeypot Weakness Test
   └── Log Evasion → Verify if Logs Are Manipulated
   ↓
Generate Results
   ├── Detected Honeypots
   ├── Attack Success/Failure Reports
   └── Exploited Vulnerabilities
   ↓
Store Results in Logs/Reports
   ↓
End Tool
```
---

## Supported Honeypots and Protocols
Here’s the list of honeypots for testing this project:

| **Honeypot**  | **Supported Protocols**            | **Purpose**                                                                | **Repository**                                            |
|---------------|------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------|
| **Cowrie**    | SSH, Telnet                        | Emulates SSH/Telnet to capture brute force attacks.                        | [GitHub Link](https://github.com/cowrie/cowrie)           |
| **Kippo**     | SSH                                | Simulates a medium-interaction SSH server for attack logging and analysis. | [GitHub Link](https://github.com/desaster/kippo)          |
| **Glastopf**  | HTTP                               | Emulates vulnerable web servers to capture attack patterns.                | [GitHub Link](https://github.com/mushorg/glastopf)        |
| **Dionaea**   | SMB, HTTP, FTP, TFTP, MSSQL, MySQL | Catches malware and collects samples for analysis.                         | [GitHub Link](https://github.com/DinoTools/dionaea)       |
| **Conpot**    | Modbus, SNMP, BACnet, HTTP, FTP    | Emulates SCADA/ICS systems for industrial protocols.                       | [GitHub Link](https://github.com/mushorg/conpot)          |
| **Wordpot**   | HTTP (WordPress)                   | Emulates WordPress installations for CMS-specific attacks.                 | [GitHub Link](https://github.com/gbrindisi/wordpot)       |
| **T-Pot**     | Multi (Cowrie, Dionaea, etc.)      | Multi-honeypot platform for various protocols.                             | [GitHub Link](https://github.com/telekom-security/tpotce) |
| **Honeyd**    | TCP, UDP, ICMP                     | Simulates multiple hosts and services on a network.                        | [GitHub Link](https://github.com/DataSoft/Honeyd)         |

---

## Project Features
Here’s the list of features for this project:

| **Category**              | **Feature**                     | **Description**                                                                                     |
|---------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------|
| **Detection**             | Honeypot Detection              | Identifies and fingerprints honeypots deployed in the network.                                      |
| **Scanning**              | Vulnerability Scanning          | Integrates tools like Nmap, Nikto, Metasploit, and OpenVAS to find vulnerabilities.                 |
| **Exploitation**          |                                 |                                                                                                     |
|   1                       | Code Injection Attacks          | Simulates injection attacks (e.g., SQL, Command) to evaluate honeypot defenses.                     |
|   2                       | Data Leakage Exploitation       | Attempts to extract sensitive information stored in the honeypot.                                   |
|   3                       | Reverse Exploitation            | Uses the honeypot’s own vulnerabilities to launch counterattacks.                                   |
|   4                       | Service Crashing                | Exploits weaknesses to crash specific services in the honeypot.                                     |
|   5                       | Privilege Escalation            | Tests for vulnerabilities that allow unauthorized access to higher privilege levels.                |
| **Simulation**            | DoS Attack Simulation           | Simulates denial-of-service attacks to test the resilience of the honeypot.                         |
| **Stealth**               | Log Evasion Techniques          | Implements methods to bypass or manipulate honeypot logging mechanisms.                             |
| **Configuration**         | Customizable Configurations     | Allows easy configuration of scan settings and attack parameters using YAML files.                  |
| **Reporting**             | Integrated Reporting            | Logs results of scans, exploits, and generates a detailed final report for analysis.                |
| **Tool Integration**      | Multi-Tool Integration          | Seamlessly integrates external tools like Nmap, Metasploit, Nikto, and OpenVAS for enhanced testing.|
| **Usability**             |                                 |                                                                                                     |
|   1                       | User-Friendly Interface         | Centralized `main.py` script to manage all operations with a simple CLI or menu interface.          |
|   2                       | Modular Design                  | Organized file structure for easy scalability and maintenance.                                      |

---
