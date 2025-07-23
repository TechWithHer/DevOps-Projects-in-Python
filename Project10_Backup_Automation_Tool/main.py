import shutil
import datetime
import os
from time import sleep
from pathlib import Path
#Ask for the source
#Ask for the File Type
#Ask for the File Name ELSE Generaate the file name  
#Generate BACKUP using File Type and Name 

def naming_func(naming_option):
    if naming_option != 0:
        return naming_option
    else: 
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"_backup_{today}"



def generate_backup(SOURCE, DESTINATION, FILE_TYPE, backup_name):
    if not SOURCE.exists():
        print("INVALID SOURCE PATH, PROGRAM TERMINATED")
        exit()

    backup_path = os.path.join(DESTINATION, backup_name)

    if FILE_TYPE == "1":
        shutil.make_archive(backup_path, 'zip', root_dir=str(SOURCE))
    elif FILE_TYPE == "2":
        shutil.make_archive(backup_path, 'gztar', root_dir=str(SOURCE))
    elif FILE_TYPE == "3":
        shutil.make_archive(backup_path, 'bztar', root_dir=str(SOURCE))
    else:
        print("Invalid file type. Using ZIP by default.")
        shutil.make_archive(backup_path, 'zip', root_dir=str(SOURCE))

    print(f"✅ Backup done: {backup_path}.{FILE_TYPE}")



SOURCE = Path(input("Please enter the Source Path- \n"))
DESTINATION = "/Users/apple/Desktop/TechWithHer/DevOps-Projects-in-Python/Project10_Backup_Automation_Tool/backup_folder"
FILE_TYPE = input("Please enter the FILE_TYPE (ZIP(1), TAR.ZIP(2) OR TAR.BZ2(3)) for BACKUP_FILE: ")
naming_option = input("Please enter the name of the new backup file else write '0' ").strip().lower()
backup_name = naming_func(naming_option)
generate_backup(SOURCE, DESTINATION, FILE_TYPE, backup_name)
