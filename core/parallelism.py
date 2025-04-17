import subprocess
from .all_ip import AllScans

class Parallelisms(AllScans):
    def __init__(self, target_ip=None):
        super().__init__(target_ip)
    def silent_scans(self): 
        subprocess.run(["nmap", "-sS", "--min-parallelism", "1", self.target_ip])
        """
        
        IDS/IPS tarafindan daha zor yakalanmasi < Ayni anda 1 baglanti gonterir >
        
        
        """
    def speed_scans(self):
        subprocess.run(["nmap", "-sS", "--max-parallelism", "100", self.target_ip])

        """
        
        Ayni anda 100 yakin port tarar 
        Kotu yani Yakalanmasi daha kolaydir
        
        
        """
    
    def parallelism_and_scansdelay(self):
        subprocess.run(["nmap", "-sS", "--min-parallelism", "10", "--scan-delay", "500ms", self.target_ip])

        """

        Ayni anda 10 baglanti gonderir < Her bir baglanti arasinda 500ms beklemesi var>  (Degise bilirsin!!)

        
        """

    def version_scans(self):
        subprocess.run(["nmap", "-sV", "--min-parallelism", "5", self.target_ip])

        """
        
        Service ve version taramasi yapar daha hizli tarar ama hedef sistem tarafindan fark edile bilir

        
        """
    def parallelism_and_maxrate(self):
        subprocess.run(["nmap", "-sS", "--min-parallelism", "10", "--max-rate", "50", self.target_ip])

        """
        
        Ayni anda en az 10 baglanti gonderir
        ama saniyede en fazla 50 packet gonderir
        Gizlilik ve hiz arasinda denge kurar :)
        
        """
