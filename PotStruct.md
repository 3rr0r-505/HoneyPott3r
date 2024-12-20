# HoneyPott3r - Python Honeypot Project

HoneyPott3r is a Python-based honeypot that simulates various network services (e.g., HTTP, SSH, FTP, MySQL) to attract and log unauthorized access attempts. It enables monitoring and analysis of malicious traffic across multiple protocols, providing valuable insights for cybersecurity research.

## Services Simulated
This honeypot simulates the following protocols:
| Service    | Ports                    | Details                                                  |
|------------|--------------------------|----------------------------------------------------------|
| http       | 80                       | Standard protocol for transferring web pages and data.   |
| ssh        | 22                       | Secure protocol for remote login and command execution.  |
| https      | 443                      | Encrypted version of HTTP for secure web communication.  |
| ftp        | 21 (control), 20 (data)  | Protocol for transferring files between systems.         |
| smb        | 445, 137-139             | Protocol for file and printer sharing over a network.    |
| dns        | 53                       | Protocol for translating domain names to IP addresses.   |
| rdp        | 3389                     | Protocol for remote desktop access to Windows machines.  |
| mysql      | 3306                     | Protocol for interacting with MySQL databases.           |
| postgres   | 5432                     | Protocol for accessing PostgreSQL databases.             |
| smtp       | 25, 587 (TLS), 465 (SSL) | Protocol for sending email messages.                     |
| telnet     | 23                       | Protocol for remote login without encryption.            |
| pop3       | 110, 995 (SSL)           | Protocol for retrieving emails from a server.            |
| imap       | 143, 993 (SSL)           | Protocol for accessing and managing emails on a server.  |
| ldap       | 389, 636 (SSL)           | Protocol for accessing directory services.               |
| redis      | 6379                     | Protocol for accessing Redis in-memory data store.       |
| ntp        | 123                      | Protocol for synchronizing system clocks over a network. |
| snmp       | 161 (query), 162 (trap)  | Protocol for monitoring and managing network devices.    |
| irc        | 6667, 6697 (SSL)         | Protocol for real-time text messaging in chatrooms.      |
| elastic    | 9200, 9300               | Protocol for interacting with Elasticsearch.             |
| vnc        | 5900                     | Protocol for graphical remote desktop sharing.           |
| socks5     | 1080                     | Protocol for routing network packets through a proxy.    |
| sip        | 5060 (UDP), 5061 (TLS)   | Protocol for initiating and managing VoIP calls.         |
| dhcp       | 67 (server), 68 (client) | Protocol for automatic IP address assignment.            |
| memcache   | 11211                    | Protocol for caching and retrieving data in memory.      |
| mssql      | 1433                     | Protocol for interacting with Microsoft SQL databases.   |
| oracle     | 1521                     | Protocol for accessing Oracle databases.                 |
| httpproxy  | 8080, 3128               | Protocol for intermediary HTTP communication.            |
| pjl        | 9100                     | Protocol for managing print jobs and printers.           |
| ipp        | 631                      | Protocol for managing print jobs over IP networks.       |

## Libraries Used
This project uses the following Python libraries for simulating services:
| Service    | Library                         |
|------------|---------------------------------|
| http       | `Flask`, `http.server`          |
| ssh        | `paramiko`, `asyncssh`          |
| https      | `Flask`, `ssl`                  |
| ftp        | `pyftpdlib`                     |
| smb        | `pysmb`, `impacket`             |
| dns        | `dnslib`, `pydns`               |
| rdp        | `rdpy`, `pyRDP`                 |
| mysql      | `pymysql`                       |
| postgres   | `psycopg2`                      |
| smtp       | `smtpd`, `aiosmtpd`             |
| telnet     | `telnetlib`                     |
| pop3       | `poplib`                        |
| imap       | `imaplib`                       |
| ldap       | `ldap3`                         |
| redis      | `redis`                         |
| ntp        | `ntplib`                        |
| snmp       | `pysnmp`                        |
| irc        | `irc`, `pydle`                  |
| elastic    | `elasticsearch`                 |
| vnc        | `vncproxy`, `PyVNC`             |
| socks5     | `pysocks`                       |
| sip        | `pysip`, `sipy`                 |
| dhcp       | `scapy`                         |
| memcache   | `pymemcache`                    |
| mssql      | `pymssql`                       |
| oracle     | `cx_Oracle`                     |
| httpproxy  | `proxy.py`, `mitmproxy`         |
| pjl        | `pjl`                           |
| ipp        | `pyipp`                         |


## Project File Structure
The project is organized in a way that makes it easy to extend and manage services. 
Here's an overview of the main project directory and its structure:
```
honeypott3r/
│
├── README.md                    # Project description and setup instructions
├── requirements.txt             # List of dependencies
│
├── honeypots/                    # Main directory for honeypot services
│   ├── __init__.py              # Initialization file for the package
│   ├── core.py                  # Core logic for starting and managing protocols
│   ├── logger.py                # Logger module for logging traffic and attacks
│   ├── config.py                # Configuration file (IP ranges, ports, etc.)
│   ├── services/                # Directory for each simulated service
│   │   ├── http_service.py      # Simulates HTTP service using Flask
│   │   ├── ssh_service.py       # Simulates SSH service using paramiko
│   │   ├── https_service.py     # Simulates HTTPS service using Flask and ssl
│   │   ├── ftp_service.py       # Simulates FTP service using pyftpdlib
│   │   ├── smb_service.py       # Simulates SMB service using smbprotocol
│   │   ├── dns_service.py       # Simulates DNS service using dnslib
│   │   ├── rdp_service.py       # Simulates RDP service
│   │   ├── mysql_service.py     # Simulates MySQL service using PyMySQL
│   │   ├── postgres_service.py  # Simulates PostgreSQL service using psycopg2
│   │   ├── smtp_service.py      # Simulates SMTP service using smtplib
│   │   ├── telnet_service.py    # Simulates Telnet service using telnetlib
│   │   ├── pop3_service.py      # Simulates POP3 service using poplib
│   │   ├── imap_service.py      # Simulates IMAP service using imaplib
│   │   ├── ldap_service.py      # Simulates LDAP service using ldap3
│   │   ├── redis_service.py     # Simulates Redis service using redis-py
│   │   ├── ntp_service.py       # Simulates NTP service using ntplib
│   │   ├── snmp_service.py      # Simulates SNMP service using pysnmp
│   │   ├── irc_service.py       # Simulates IRC service using irc
│   │   ├── elastic_service.py   # Simulates ElasticSearch service
│   │   ├── vnc_service.py       # Simulates VNC service using vncdotool
│   │   ├── socks5_service.py    # Simulates SOCKS5 service using PySocks
│   │   ├── sip_service.py       # Simulates SIP service using Twisted or pjsip
│   │   ├── dhcp_service.py      # Simulates DHCP service
│   │   ├── memcache_service.py  # Simulates Memcached service using pymemcache
│   │   ├── mssql_service.py     # Simulates MSSQL service using pyodbc
│   │   ├── oracle_service.py    # Simulates Oracle DB service using cx_Oracle
│   │   ├── httpproxy_service.py # Simulates HTTP Proxy service using mitmproxy
│   │   ├── pjl_service.py       # Simulates PJL service
│   │   ├── ipp_service.py       # Simulates IPP service using pyipp
│
├── logs/                    # Directory to store log files
│   ├── access_logs/         # Logs for incoming access
│   ├── attack_logs/         # Logs for detected attack attempts
│
├── database/                # Directory to store database (e.g., MongoDB or SQLite)
│   ├── honeypot_data.db     # Database file (if using SQLite) or connection details
│
└── scripts/                 # Utility scripts for managing and starting services
    ├── start_services.py    # Script to start all honeypot services
    ├── stop_services.py     # Script to stop all honeypot services
    ├── monitor_traffic.py   # Script to analyze traffic and detect attacks
    ├── attack_alerts.py     # Script to send alerts for detected attacks

```

