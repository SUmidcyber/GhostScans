import subprocess
import json
import time
from core.all_ip import AllScans
from core.protocol import ProtocolScans
from core.waf_detection import WafDetection
from core.ssh_enumerations import SSHenumerations
from core.mysql import MySQLenumerations
from core.smb_enumerations import SMBenumerations



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
def smb_submenu():
    print("""
    SMB Enumerations Options PORT Scan:
    1) PORT 445
    2) PORT 139
    3) Scan Both Ports
    4) Deep Scans (SMB)
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
                run_scan_with_progress(scanner.all_port, log_choice, "all_ports.json")
            elif choice == '2':
                handle_protocol_scans(scanner.target_ip, log_choice)
            elif choice == '3':
                run_scan_with_progress(waf_detections, log_choice, "waf.json", scanner.target_ip)
            elif choice == '4':
                ssh_enumeration(scanner.target_ip, log_choice)
            elif choice == '5':
                run_scan_with_progress(mysql_detections, log_choice, "mysql.json", scanner.target_ip)
            elif choice == '6':
                smb_enumerations(scanner.target_ip, log_choice)
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
            run_scan_with_progress(protocol_scanner.tcp_scan, log_choice, "packages.json")
        elif choice == '2':
            run_scan_with_progress(protocol_scanner.udp_scan, log_choice, "packages.json")
        elif choice == '3':
            run_scan_with_progress(protocol_scanner.icmp_scan, log_choice, "packages.json")
        elif choice == '4':
            run_scan_with_progress(protocol_scanner.arp_scan, log_choice, "packages.json")
        elif choice == '5':
            run_scan_with_progress(protocol_scanner.ping_scan, log_choice, "packages.json")
        elif choice =='6':
            run_scan_with_progress(protocol_scanner.os_detection, log_choice, "packages.json")
        elif choice == '7':
            run_scan_with_progress(protocol_scanner.stealth_scan, log_choice, "packages.json")
        elif choice == '8':
            run_scan_with_progress(protocol_scanner.fin_scanning, log_choice, "packages.json")
        elif choice == '9':
            run_scan_with_progress(protocol_scanner.xmas_scanning, log_choice, "packages.json")
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
            run_scan_with_progress(ssh_scans.ssh_brute, log_choice, "ssh_enumeration.json")
        elif choice == '2':
            run_scan_with_progress(ssh_scans.ssh2_enum_algos, log_choice, "ssh_enumeration.json")
        elif choice == '3':
            run_scan_with_progress(ssh_scans.ssh_run, log_choice, "ssh_enumeration.json")
        elif choice == '4':
            run_scan_with_progress(ssh_scans.sshv1, log_choice, "ssh_enumeration.json")
        elif choice == 'b':
            break
        else: 
            print("Invalid SSH Choice!")

def mysql_detections(target):
    # MYSQL Detections tarama + BrutForce 
    mysql_scaner = MySQLenumerations(target)
    mysql_scaner.mysql_enumrations()
    mysql_scaner.mysql_related()
    mysql_scaner.mysql_empty_password_nse()
    mysql_scaner.mysql_brute_force()

def smb_enumerations(target, log_choice):
    smb_scans = SMBenumerations(target)
    while True:
        smb_submenu()
        choice = input("Port Options (1-3 , b to back): ").strip().lower()
        if choice == '1':
            run_scan_with_progress(smb_scans.smb_p445, log_choice, "smb_port445.json")
        elif choice == '2':
            run_scan_with_progress(smb_scans.smb_p139, log_choice, "smb_port139.json")
        elif choice == '3':
            run_scan_with_progress(smb_scans.smb_two_ports, log_choice, "smb_two_scans_port.json")
        elif choice == '4':
            run_scan_with_progress(smb_scans.smb_deep_scan_ports, log_choice, "smb_deep_scans.json")
        elif choice == 'b':
            break
        else:
            print("Invalid Options SMB CHOICE!")


def run_scan_with_progress(scan_method, log_choice, log_file, *args):
    try:
        scan_command = scan_method(*args)
        if log_choice == 'y':
            with open(log_file, "w") as file:
                process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                total_lines = 100  # Örnek olarak toplam satır sayısını belirleyin
                log_data = []
                for i, line in enumerate(process.stdout):
                    log_data.append({"line": line.decode().strip()})
                    progress = (i + 1) / total_lines * 100
                    print_progress_bar(progress)
                    time.sleep(0.1)  # İlerleme göstergesini güncellemek için kısa bir bekleme süresi
                json.dump(log_data, file, indent=4)
        else:
            process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            total_lines = 100  # Örnek olarak toplam satır sayısını belirleyin
            for i, line in enumerate(process.stdout):
                print(line.decode())
                progress = (i + 1) / total_lines * 100
                print_progress_bar(progress)
                time.sleep(0.1)  # İlerleme göstergesini güncellemek için kısa bir bekleme süresi
        
        process.wait()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, scan_command)
    except Exception as e:
        print(f"Error during scan: {e}")

def print_progress_bar(progress, bar_length=50):
    block = int(bar_length * progress / 100)
    bar = "█" * block + "-" * (bar_length - block)
    print(f"\rProgress: |{bar}| {progress:.2f}%", end="")

if __name__ == "__main__":
    main()
