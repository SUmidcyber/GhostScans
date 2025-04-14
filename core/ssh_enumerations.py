import subprocess
from .all_ip import AllScans

class SSHenumerations(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def ssh_brute(self):
        subprocess.run(["nmap", "-p22", "--script", "ssh-brute", "--script-args", "userdb=users.lst,passdb=pass.lst,ssh-brute.timeout=4s", self.target_ip])
    
    def ssh2_enum_algos(self):
        subprocess.run(["nmap", "--script", "ssh2-enum-algos", self.target_ip])
    
    def ssh_run(self):
        subprocess.run([
            "nmap", 
            "-p22", 
            "--script=ssh-run", 
            "--script-args=ssh-run.cmd='ls -l /',ssh-run.username='myusername',ssh-run.password='mypassword'", 
            self.target_ip
        ])
    
    def sshv1(self):
        subprocess.run(["nmap", "--script sshv1", self.target_ip])
    
