import subprocess
from .all_ip import AllScans

class HTTPenumrations(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def http_enums(self):
        subprocess.run(["nmap", "-sV", "--script=http-enum", self.target_ip])

    """
        HTTP ENUMS ORNEK CIKTI

                80/tcp open  http    syn-ack
                | http-enum:
                |   /icons/: Icons and images
                |   /images/: Icons and images
                |   /robots.txt: Robots file
                |   /sw/auth/login.aspx: Citrix WebTop
                |   /images/outlook.jpg: Outlook Web Access
                |   /nfservlets/servlet/SPSRouterServlet/: netForensics
                |_  /nfservlets/servlet/SPSRouterServlet/: netForensics
    
    """
    def http_methods(self):
        subprocess.run(["nmap", "--script", "http-methods", self.target_ip])

        """
        
            IP ilgili olan sayfada METHOTS nedir se bize gostermesi
        
        
        """
