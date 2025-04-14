import subprocess
from core.all_ip import AllScans
from core.protocol import ProtocolScans
from core.waf_detection import WafDetection
from core.ssh_enumerations import SSHenumerations

def show_menu():
    print("""
    1) All Scans            6) SMB Enumerations
    2) Protocol Scans       7) HTTP Enumerations
    3) Waf Detection        8) DNS Scans
    4) SSH Enumeration      9) Scans Delay
    5) MySql                10) Parallelism
    q) Quit
    """)

def protocol_submenu():
    print("""
    Protocol Scan Options:
    1) TCP Scan
    2) UDP Scan
    3) ICMP Ping
    4) ARP Scan
    5) Ping Scan
    6) OS Detection
    7) Stealth Scan
    8) FIN Scanning
    9) XMAS Scanning
    b) Back to Main Menu
    """)

def ssh_submenu():
    print("""
    SSH Enumeration Options:
    1) SSH Brute
    2) SSH2 Enum Algos
    3) SSH Run
    4) SSHV1
    b) Back to Main Menu
    """)

def main():
    try:
        scanner = AllScans()  # Bu artık kullanıcıdan otomatik IP isteyecek
        
        while True:
            print("\n" + "="*50)
            print(f"Current Target: {scanner.target_ip}")
            print("="*50)
            
            show_menu()
            choice = input("Select an option (1-10, q to quit): ").strip().lower()
            log_choice = input("Do you want to log the output? (y/n): ").strip().lower()
            
            if choice == '1':
                run_scan(scanner.all_port, log_choice, "all_ports.log")
            elif choice == '2':
                handle_protocol_scans(scanner.target_ip, log_choice)
            elif choice == '3':
                run_scan(waf_detections, log_choice, "waf.log", scanner.target_ip)
            elif choice == '4':
                ssh_enumeration(scanner.target_ip, log_choice)
            elif choice == 'q':
                break
            else:
                print("Invalid choice! Please try again.")
    
    except Exception as e:
        print(f"\nError: {e}")

def handle_protocol_scans(target, log_choice):
    protocol_scanner = ProtocolScans(target)
    while True:
        protocol_submenu()
        choice = input("Protocol choice (1-9, b to back): ").strip().lower()
        
        if choice == '1':
            run_scan(protocol_scanner.tcp_scan, log_choice, "packages.log")
        elif choice == '2':
            run_scan(protocol_scanner.udp_scan, log_choice, "packages.log")
        elif choice == '3':
            run_scan(protocol_scanner.icmp_scan, log_choice, "packages.log")
        elif choice == '4':
            run_scan(protocol_scanner.arp_scan, log_choice, "packages.log")
        elif choice == '5':
            run_scan(protocol_scanner.ping_scan, log_choice, "packages.log")
        elif choice =='6':
            run_scan(protocol_scanner.os_detection, log_choice, "packages.log")
        elif choice == '7':
            run_scan(protocol_scanner.stealth_scan, log_choice, "packages.log")
        elif choice == '8':
            run_scan(protocol_scanner.fin_scanning, log_choice, "packages.log")
        elif choice == '9':
            run_scan(protocol_scanner.xmas_scanning, log_choice, "packages.log")
        elif choice == 'b':
            break
        else:
            print("Invalid protocol choice!")

def waf_detections(target):
    waf_scanner = WafDetection(target)
    waf_scanner.http_waf_detect()
    waf_scanner.http_waf_fingerprint()
    waf_scanner.http_waf_detect_aggro()

def ssh_enumeration(target, log_choice):
    ssh_scans = SSHenumerations(target)
    while True:
        ssh_submenu()
        choice = input("SSH Enumeration choice (1-5, b to back): ").strip().lower()
        if choice == '1':
            run_scan(ssh_scans.ssh_brute, log_choice, "ssh_enumeration.log")
        elif choice == '2':
            run_scan(ssh_scans.ssh2_enum_algos, log_choice, "ssh_enumeration.log")
        elif choice == '3':
            run_scan(ssh_scans.ssh_run, log_choice, "ssh_enumeration.log")
        elif choice == '4':
            run_scan(ssh_scans.sshv1, log_choice, "ssh_enumeration.log")
        elif choice == 'b':
            break
        else: 
            print("Invalid SSH Choice!")

def run_scan(scan_method, log_choice, log_file, *args):
    if log_choice == 'y':
        with open(log_file, "w") as file:
            result = subprocess.run(scan_method(*args), stdout=file, stderr=file)
    else:
        result = subprocess.run(scan_method(*args))
    
    if result is None:
        raise ValueError("Scan method returned None, which is not iterable.")

if __name__ == "__main__":
    main()
