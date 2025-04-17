# GhostScans

A command-line utility designed to simplify network scanning and enumeration tasks through an intuitive menu-driven interface.

## Features

- Multiple scanning options (TCP, UDP, ICMP, ARP, etc.)
- Service enumeration (SSH, SMB, HTTP, DNS, MySQL)
- WAF detection and OS fingerprinting
- Scan timing control (delayed scans, parallel scans)
- User-friendly menu system

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SUmidcyber/GhostScans.git

## Navigate to the project directory:
    cd GhostScans

## Install required dependencies (if any):
    pip install -r requirements.txt

# Usage

## Run the tool with:
   
    chmod +x main.py
    python main.py

## Main Menu Options
   
    1) All Scans            6) SMB Enumerations
    2) Protocol Scans       7) HTTP Enumerations
    3) Waf Detection        8) DNS Service Scans
    4) SSH Enumeration      9) Scans Delay
    5) MySql                10) Parallelism
    q) Quit

## Submenus
    Protocol Scans: TCP, UDP, ICMP, ARP scans and OS detection

    SSH Enumeration: SSH brute force, algorithm enumeration

    SMB Enumerations: Port 445/139 scans and deep SMB scanning

    Scans Delay: Timed scan options and firewall evasion

    Parallelism: Parallel scanning and fast scan options