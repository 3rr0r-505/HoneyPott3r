# HoneyPott3r - Python Honeypot Project

## Project Overview
HoneyPott3r is a Python-based honeypot that simulates various network services (e.g., HTTP, SSH, FTP, MySQL) to attract and log unauthorized access attempts. It enables monitoring and analysis of malicious traffic across multiple protocols, providing valuable insights for cybersecurity research.


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/3rr0r-505/HoneyPott3r.git
   ```
   ```
   cd HoneyPott3r
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
---
## Note
⚠️ For detailed project structure, visit the [PotStruct.md](https://github.com/3rr0r-505/HoneyPott3r/edit/main/PotStruct.md)

⚙️ This Project is under development.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.

## License
This project is licensed under the [MIT License](https://github.com/3rr0r-505/HoneyPot3r/blob/main/LICENSE) - see the LICENSE file for details.


