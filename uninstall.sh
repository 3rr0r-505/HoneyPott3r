#!/bin/bash

# Uninstallation script for HoneyPott3r

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (use sudo)."
    exit 1
fi

echo "[*] Uninstalling HoneyPott3r..."

# Set the installation directory
INSTALL_DIR="/opt/honeypott3r"

# Remove the installation directory and its contents
if [ -d "$INSTALL_DIR" ]; then
    echo "[*] Removing $INSTALL_DIR..."
    rm -rf "$INSTALL_DIR"
else
    echo "[!] Installation directory not found, skipping removal."
fi

# Remove the symlink from /usr/local/bin
if [ -L "/usr/local/bin/honeypott3r" ]; then
    echo "[*] Removing symlink from /usr/local/bin..."
    rm -f "/usr/local/bin/honeypott3r"
else
    echo "[!] Symlink not found, skipping removal."
fi

# Inform the user about optional removals
echo -e "\n[!] Optional Cleanup Steps:"
echo "[>] System Tools to remove: netcat trivy bandit safety nmap nikto wpscan msfconsole mongoDB docker"

echo -e "\n[*] HoneyPott3r has been uninstalled successfully!"
