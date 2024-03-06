import shutil 
import os 
import datetime
 

class Backup:
    
    def __init__(self,source_dir,destination_dir):
        self.source_directory=source_dir
        self.destination_directory=destination_dir
        pass
    
    def backup_files(self):
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y")
        backup_dir=os.path.join(self.destination_directory,f"backup_file_{timestamp}")
        # os.makedirs(backup_dir)
        for root,src,files in os.walk(self.source_directory):
            for file in files:
                src_path=os.path.join(root,file)
                dest_path=os.path.join(backup_dir,os.path.relpath(src_path,self.source_directory))
                os.makedirs(os.path.dirname(dest_path),exist_ok=True)
                shutil.copy(src_path,dest_path)
                print(f"Copied {src_path} to {dest_path}")