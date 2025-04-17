import subprocess
from .all_ip import AllScans

class DNService(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)

    def dns_service(self):
        subprocess.run(["nmap", "--script=dns-service-discovery", "-p 5353", self.target_ip])