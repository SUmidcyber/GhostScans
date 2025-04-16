import subprocess
from .all_ip import AllScans

class SMBenumerations(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def smb_p445(self): # PORT 445 Scan SMB
        subprocess.run(["nmap", "-p445", "—", "script", "smb-protocols", self.target_ip])

    def smb_p139(self): # PORT 139 Scan SMB
        subprocess.run(["nmap", "-p139", "—", "script", "smb-protocols", self.target_ip])
    
    def smb_two_ports(self): # Port Her ikisini taramak SMB
        subprocess.run(["nmap", "-sC", "-p", "139,445", "-sV", self.target_ip])
    
    def smb_deep_scan_ports(self):
        subprocess.run(["sudo", "nmap", "-sU", "-sS", "--script", "smb-enum-users.nse", "-p", "U:137,T:139", self.target_ip])



"""

     SMB protokolü, varsailan olarak 139 ve 445 numarali TCP portlarini kullanir.
        Burada kulanici isdedigi PORT sece bilecek veya Her iki protu beraber taraya bilecekdir
            Daha derinlemesine SMB Scans dedigimizde bunun icin derin SCRIPT yazmam gerek 
                sudo nmap -sU -sS --script smb-enum-users.nse -p U:137,T:139 <host>

"""
    