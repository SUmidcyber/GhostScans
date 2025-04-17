import subprocess
from .all_ip import AllScans

class ScanDelay(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def tcp_syn_scan(self): # TCP SYN Scan ama gecikmeli tarar
        subprocess.run(["nmap", "-sS", "--scan-delay", "500ms", self.target_ip])

    def hide_scans(self): # Tesbit edilmeden portlarin acik olub olmadina bakar ama yavas tarar ( daha az iz birakir)
        subprocess.run(["nmap", "-sS", "-T1", "--scan-delay", "1s", self.target_ip])

    def firewall_port_scan(self): # Firewall arkasindan port tarar ve tesbit eder
        subprocess.run(["nmap", "-sA", "--scan-delay", "800ms", self.target_ip])

    def firewall_ips_bypass(self): # Firewall/IPS atlarmak icin rasgale gecikmeli tarama
        subprocess.run(["nmap", "-sS", "--scan-delay", "500ms", "--max-scan-delay", "1500ms", self.target_ip])

    def speed_is_angry_scans(self): # Saniyede 30 packet gonderir IDS daha az dikatini ceker
        subprocess.run(["nmap", "-sS", "--max-rate", "30", self.target_ip])
    
    def service_and_versiyon(self): # Service ve Version tarar Acik portlari ogrenmek icin:
        subprocess.run(["nmap", "-sS", "-sV", "--scan-delay", "700ms", self.target_ip])