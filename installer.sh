#!/bin/bash

# Installation script for honeypott3r
# add the shebang (#!/usr/bin/env python3) to the main script (main.py) since it is the entry point. Other module files don't need it.

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (use sudo)."
    exit 1
fi

echo "[*] Installing HoneyPott3r..."

# Set the installation directory
INSTALL_DIR="/opt/honeypott3r"

# Create the installation directory
mkdir -p "$INSTALL_DIR"

# Copy all files to the installation directory
cp -r ./* "$INSTALL_DIR"

# Ensure the main script is executable
chmod +x "$INSTALL_DIR/main.py"

# Create a symlink in /usr/local/bin to make it globally accessible
ln -sf "$INSTALL_DIR/main.py" /usr/local/bin/honeypott3r

# Install Python dependencies
if [ -f "$INSTALL_DIR/requirements.txt" ]; then
    echo "[*] Installing Python dependencies..."
    python3 -m pip install -q -r "$INSTALL_DIR/requirements.txt"
fi

# Check for required tools
echo "[*] Checking required tools..."
MISSING_TOOLS=()

for tool in nmap msfconsole nikto openvas; do
    if ! command -v "$tool" &> /dev/null; then
        MISSING_TOOLS+=("$tool")
    fi
done

if [ ${#MISSING_TOOLS[@]} -ne 0 ]; then
    echo "[!] Warning: The following tools are not installed:"
    for tool in "${MISSING_TOOLS[@]}"; do
        echo "  - $tool"
    done
else
    echo "[*] All required tools are installed."
fi

echo "[*] HoneyPott3r has been installed successfully!"
echo "[*] You can now run the tool using the command: sudo honeypott3r"
