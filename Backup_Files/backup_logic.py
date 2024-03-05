import shutil 
import os 
import datetime
 

class Backup:
    
    def __init__(self,source_dir,destination_dir):
        self.source_directory=source_dir
        self.destination_directory=destination_dir
        pass
    
    def backup_files(self):
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y | %H:%M")
        backup_dir=os.path.join(self.destination_directory,f"backup_file__{timestamp}")
        