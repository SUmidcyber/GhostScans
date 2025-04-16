import subprocess
from .all_ip import AllScans

class MySQLenumerations(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    
    def mysql_enumrations(self):
        subprocess.run(["nmap", "-p 3306", "--script", "mysql-enum.nse", self.target_ip])
    
    def mysql_related(self):
        subprocess.run(["nmap", "-p 3306", "--script", "mysql-empty-password.nse", self.target_ip])

    """
    def mysql_empty_password_nse(self):
        subprocess.run(["nmap", "-p 3306", "--script", "mysql-brute.nse", "--script-args", "userdb=<userlist>", "passdb=<passlist>", self.target_ip])

            Bu komut, MySQL sunucusunun kök kullanici için boş bir parolaya sahip olup olmadiğini kontrol etmek için mysql-empty-password.nse betiğini kullanir.

    """

    def mysql_empty_password_nse(self):
        subprocess.run(["nmap", "-p 3306", "--script", "mysql-brute.nse", "--script-args", "userdb=<userlist>", "passdb=<passlist>", self.target_ip])

    def mysql_brute_force(self):
        subprocess.run(["nmap", "-p 3306", "--script", "mysql-info.nse", self.target_ip])