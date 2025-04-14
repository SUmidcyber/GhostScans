import subprocess
from .all_ip import AllScans

class WafDetection(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def http_waf_detect(self):
        subprocess.run(["nmap", "-p80", "--script=http-waf-detect", self.target_ip])
    
    def http_waf_fingerprint(self):
        subprocess.run(["nmap", "-p80", "--script=http-waf-fingerprint", self.target_ip])
    
    def http_waf_detect_aggro(self):
        subprocess.run(["nmap", "-p80", "--script=http-waf-detect", "--script-args=http-waf-detect.aggro", self.target_ip])
