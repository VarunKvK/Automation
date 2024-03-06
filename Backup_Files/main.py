from backup_logic import Backup

def main():
    # source=r"C:\Users\Admin\Downloads\Telegram Desktop"
    # destination=r"I:\WorkByVarun\BackupFiles"
    source =input("Enter the directory which you want to copy: ")
    destination =input("Enter the directory where you want to paste: ")
    backup=Backup(source_dir=source,destination_dir=destination)
    backup.backup_files()
    
if __name__=="__main__":
    main()
    