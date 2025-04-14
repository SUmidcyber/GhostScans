import subprocess
import re

class AllScans:
    def __init__(self, target_ip=None):
        while True:
            self.target_ip = target_ip or input("Target IP/Hostname: ").strip()
            if self._validate_ip():
                break
            print("Invalid IP address format! Please try again.")
            target_ip = None
    
    def _validate_ip(self):
        ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        hostname_pattern = r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
        return re.match(ip_pattern, self.target_ip) or re.match(hostname_pattern, self.target_ip)
    
    def all_port(self):
        subprocess.run(["nmap", "-p-", self.target_ip])
    
    def script_vuln(self):
        subprocess.run(["nmap", "-Pn", "--script", "vuln", self.target_ip])
    
    def ssh_service_authentication(self, username="pentest"):
        subprocess.run([
            "nmap",
            "--script", "ssh-auth-methods",
            "--script-args", f"ssh.user={username}",
            "-p", "22",
            self.target_ip
        ])
    
    def waf_detect(self):
        subprocess.run(["nmap", "--script", "http-waf-detect", "-p", "80,443", self.target_ip])
    
    def smb_enum(self):
        subprocess.run(["nmap", "--script", "smb-enum-shares", "-p", "445", self.target_ip])
    
    def service_scan(self):
        subprocess.run(["nmap", "-sV", self.target_ip])
    
    def http_enum(self):
        subprocess.run(["nmap", "--script", "http-enum", "-p", "80,443", self.target_ip])
    
    def dns_scan(self):
        subprocess.run(["nmap", "--script", "dns-brute", self.target_ip])