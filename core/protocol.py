import subprocess
from .all_ip import AllScans  # AllScans sınıfından miras al
class ProtocolScans(AllScans):  # BU SINIF TANIMLI MI?
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def tcp_scan(self):
        subprocess.run(["nmap", "-sT", self.target_ip])
    def udp_scan(self):
        subprocess.run(["nmap", "-PU", self.target_ip])
    def icmp_scan(self):
        subprocess.run(["nmap", "-PE", self.target_ip])
    def arp_scan(self):
        subprocess.run(["nmap", "-sP", self.target_ip])
    def ping_scan(self):
        subprocess.run(["nmap", "-PO", self.target_ip])
    def os_detection(self):
        subprocess.run(["nmap", "-O", self.target_ip])
    def stealth_scan(self):
        subprocess.run(["nmap","-sS", self.target_ip])
    def fin_scanning(self):
        subprocess.run(["nmap", "-sF", self.target_ip])
    def xmas_scanning(self):
        subprocess.run(["nmap","-sX", self.target_ip])
