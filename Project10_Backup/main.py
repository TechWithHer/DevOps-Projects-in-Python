import os
from time import sleep
import datetime
import shutil

print("For backup, you will be providing the path of the source and type of compressed file you want")
sleep(3)
print("The options of backup files are: ZIP, TAR.ZIP, and TAR.BZ2 you can choose else we will choose the default i.e ZIP")
sleep(2)
print("We will give you the option to name the backup file, else we will name it by default")
print("Lets begin")

#if the user selects the naming option, this function will run.
def naming_backup(backup_name):
    return backup_name

#selecting file_type and making the backup using backup_name by default or by backup_name selected by the user
def make_backup(source, destination, backup_name):
    while (source.exists()):
        if file_type == "1" or ((file_type != "2") or (file_type != "3")):
            print("Using the default file type (ZIP) to generate a backup")
            today = datetime.date.today()
            backup_name = os.path.join(destination,f"backup_{today}.tar.gz") #giving the complete path of the backup
            shutil.make_archive(backup_name, 'ZIP', source) #The actual backup is being generated
        elif file_type == "2":
            backup_name = os.path.join(destination,f"backup_{backup_name}.TAR.BZ2") #giving the complete path of the backup
            shutil.make_archive(backup_name, 'TAR.ZIP', source) #The actual backup is being generated
        elif file_type == "3":
            backup_name = os.path.join(destination,f"backup_{backup_name}.TAR.BZ2") #giving the complete path of the backup
            shutil.make_archive(backup_name, 'TAR.BZ2', source) #The actual backup is being generated
    
    print(f"Backup Done. The File Name is {backup_name}")



source = input("Please enter the Source Path")
destination = "/Users/apple/Desktop/TechWithHer/DevOps-Projects-in-Python/Project10_Backup/backup_folder"
#asking the user to enter the type of backup file
file_type = input("Enter the type of compressed file you want to create: 1 - ZIP, 2 - TAR.ZIP , 3 - TAR.BZ2, choose 1 or 2 or 3")
while True:
    naming_option = input("Do you want to name the folder yourself? (Y/N): ").strip().lower()
    backup_name = naming_backup(backup_name)

    if naming_option == "y":
        name = input("Enter the name of the folder: ")
        # You can now use `name` as needed
        make_backup(source, destination,backup_name)
        break
    elif naming_option == "n":
        print("Using the system to generate the name")
        make_backup(source, destination,backup_name)  # make sure `source` is defined
        break
    else:
        print("Invalid input. Please enter Y or N.")








