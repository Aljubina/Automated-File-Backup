import os         #operating system
import shutil     #copying operation
import datetime
import schedule
import time 

#define source : thing that we wanna backup
#define destination directory 
source_dir = "C:/Users/hp/Pictures/Screenshots"
destination_dir = "C:/Users/hp/Pictures/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()    #gives us current date
    dest_dir = os.path.join(dest, str(today))  #combining the current date with destination directory--> inside of Backups directory we will have new directory -> Backups/09-07-25

    try:
        shutil.copytree(source, dest_dir)   #copying from folder backups to destinaion direc
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

#scheduling a task of backup everyday at 12:22am
schedule.every().day.at("00:32").do(lambda: copy_folder_to_directory(source_dir, destination_dir))  # do calls lambda , lambda calls copy_folder_to_directory()

#same thing
#def l():
#       copy_folder_to_directory()

while True:
    schedule.run_pending()
    time.sleep(60)

