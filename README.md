# HoneyPot3r - Python Honeypot Project

## Project Overview
This project simulates a variety of network services (such as HTTP, SSH, FTP, MySQL, etc.) to create a honeypot. The purpose of this honeypot is to attract and log unauthorized access attempts, helping you monitor and analyze malicious traffic across different protocols.

## Table of Contents
- [Project Overview](#project-overview)
- [Services Simulated](#services-simulated)
- [Libraries Used](#libraries-used)
- [Project File Structure](#project-file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Services Simulated
This honeypot simulates the following protocols:

1. **http**: Standard protocol for transferring web pages and web application data.  
2. **ssh**: Secure protocol for remote login and command execution.  
3. **https**: Encrypted version of HTTP for secure web communication.  
4. **ftp**: Protocol for transferring files between systems.  
5. **smb**: Protocol for file and printer sharing over a network.  
6. **dns**: Protocol for translating domain names to IP addresses.  
7. **rdp**: Protocol for remote desktop access to Windows machines.  
8. **mysql**: Protocol for interacting with MySQL databases.  
9. **postgres**: Protocol for accessing PostgreSQL databases.  
10. **smtp**: Protocol for sending email messages.  
11. **telnet**: Protocol for remote login without encryption.  
12. **pop3**: Protocol for retrieving emails from a server.  
13. **imap**: Protocol for accessing and managing emails on a server.  
14. **ldap**: Protocol for accessing directory services like user information.  
15. **redis**: Protocol for accessing the Redis in-memory data structure store.  
16. **ntp**: Protocol for synchronizing system clocks over a network.  
17. **snmp**: Protocol for monitoring and managing network devices.  
18. **irc**: Protocol for real-time text messaging in chatrooms.  
19. **elastic**: Protocol for interacting with Elasticsearch search and analytics engine.  
20. **vnc**: Protocol for graphical remote desktop sharing.  
21. **socks5**: Protocol for routing network packets through a proxy server.  
22. **sip**: Protocol for initiating and managing VoIP communications.  
23. **dhcp**: Protocol for automatic assignment of IP addresses.  
24. **memcache**: Protocol for caching and retrieving data in memory.  
25. **mssql**: Protocol for interacting with Microsoft SQL Server databases.  
26. **oracle**: Protocol for accessing Oracle databases.  
27. **httpproxy**: Protocol for intermediary HTTP communication.  
28. **pjl**: Protocol for managing print jobs and printers.  
29. **ipp**: Protocol for managing print jobs over IP networks.

## Libraries Used
This project uses the following Python libraries for simulating services:

- **http**: `Flask`
- **ssh**: `paramiko`
- **https**: `Flask`, `ssl`
- **ftp**: `pyftpdlib`
- **smb**: `smbprotocol`
- **dns**: `dnslib`
- **rdp**: `FreeRDP` or `python-xrdp`
- **mysql**: `PyMySQL` or `MySQLdb`
- **postgres**: `psycopg2`
- **smtp**: `smtplib`
- **telnet**: `telnetlib`
- **pop3**: `poplib`
- **imap**: `imaplib`
- **ldap**: `ldap3`
- **redis**: `redis-py`
- **ntp**: `ntplib`
- **snmp**: `pysnmp`
- **irc**: `irc`
- **elastic**: `elasticsearch`
- **vnc**: `vncdotool` or `PyVNC`
- **socks5**: `PySocks`
- **sip**: `Twisted` or `pjsip`
- **dhcp**: `dhcpd`
- **memcache**: `pymemcache`
- **mssql**: `pyodbc`
- **oracle**: `cx_Oracle`
- **httpproxy**: `mitmproxy` or `http.server`
- **pjl**: `pycups`
- **ipp**: `pyipp`

## Project File Structure
```
honeypot_project/
│
├── README.md                # Project description and setup instructions
├── requirements.txt         # List of dependencies
│
├── honeypot/                 # Main directory for honeypot services
│   ├── __init__.py          # Initialization file for the package
│   ├── core.py              # Core logic for starting and managing protocols
│   ├── logger.py            # Logger module for logging traffic and attacks
│   ├── config.py            # Configuration file (IP ranges, ports, etc.)
│   ├── services/            # Directory for each simulated service
│   │   ├── http_service.py  # Simulates HTTP service using Flask
│   │   ├── ssh_service.py   # Simulates SSH service using paramiko
│   │   ├── https_service.py # Simulates HTTPS service using Flask and ssl
│   │   ├── ftp_service.py   # Simulates FTP service using pyftpdlib
│   │   ├── smb_service.py   # Simulates SMB service using smbprotocol
│   │   ├── dns_service.py   # Simulates DNS service using dnslib
│   │   ├── rdp_service.py   # Simulates RDP service
│   │   ├── mysql_service.py # Simulates MySQL service using PyMySQL
│   │   ├── postgres_service.py # Simulates PostgreSQL service using psycopg2
│   │   ├── smtp_service.py  # Simulates SMTP service using smtplib
│   │   ├── telnet_service.py # Simulates Telnet service using telnetlib
│   │   ├── pop3_service.py  # Simulates POP3 service using poplib
│   │   ├── imap_service.py  # Simulates IMAP service using imaplib
│   │   ├── ldap_service.py  # Simulates LDAP service using ldap3
│   │   ├── redis_service.py # Simulates Redis service using redis-py
│   │   ├── ntp_service.py   # Simulates NTP service using ntplib
│   │   ├── snmp_service.py  # Simulates SNMP service using pysnmp
│   │   ├── irc_service.py   # Simulates IRC service using irc
│   │   ├── elastic_service.py # Simulates ElasticSearch service
│   │   ├── vnc_service.py   # Simulates VNC service using vncdotool
│   │   ├── socks5_service.py # Simulates SOCKS5 service using PySocks
│   │   ├── sip_service.py   # Simulates SIP service using Twisted or pjsip
│   │   ├── dhcp_service.py  # Simulates DHCP service
│   │   ├── memcache_service.py # Simulates Memcached service using pymemcache
│   │   ├── mssql_service.py  # Simulates MSSQL service using pyodbc
│   │   ├── oracle_service.py # Simulates Oracle DB service using cx_Oracle
│   │   ├── httpproxy_service.py # Simulates HTTP Proxy service using mitmproxy
│   │   ├── pjl_service.py   # Simulates PJL service
│   │   ├── ipp_service.py   # Simulates IPP service using pyipp
│
├── logs/                    # Directory to store log files
│   ├── access_logs/         # Logs for incoming access
│   ├── attack_logs/         # Logs for detected attack attempts
│
├── database/                # Directory to store database (e.g., MongoDB or SQLite)
│   ├── honeypot_data.db     # Database file (if using SQLite) or connection details
│
└── scripts/                  # Utility scripts for managing and starting services
    ├── start_services.py    # Script to start all honeypot services
    ├── stop_services.py     # Script to stop all honeypot services
    ├── monitor_traffic.py   # Script to analyze traffic and detect attacks
    ├── attack_alerts.py     # Script to send alerts for detected attacks

```


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/honeypot_project.git
   ```
   ```
   cd honeypot_project
   ```
2. Install dependencies:
  ```bash
    pip install -r requirements.txt
  ```

## Usage
- Start all honeypot services:
```
  python scripts/start_services.py
```
- Monitor traffic and detect attacks:
```
python scripts/monitor_traffic.py
```
- Stop all honeypot services:
```
python scripts/stop_services.py
```

## License
This project is licensed under the [MIT License](https://github.com/3rr0r-505/HoneyPot3r/blob/main/LICENSE) - see the LICENSE file for details.


