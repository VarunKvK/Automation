from backup_logic import Backup

def main():
    source="C:\Users\Admin\Downloads\Telegram Desktop"
    destination=""
    backup=Backup(source_dir=source)
    backup.backup_files()
    
if __name__=="__main__":
    main()
    