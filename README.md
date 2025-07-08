# Automated-File-Backup

This Python script automatically creates a daily backup of a specific folder (like Screenshots) to a designated backup location with the current date.

# 📌 Features

- Automatically copies a folder to a backup directory.

- Creates a new dated folder for each backup (e.g., Backups/2025-07-09).

- Runs daily at a scheduled time using the schedule library.

- Simple and customizable for other folders.

# 📁 Default Configuration

- Source Folder: C:/Users/hp/Pictures/Screenshots

- Destination Folder: C:/Users/hp/Pictures/Backups

- Time: Scheduled for 12:32 AM every day

- You can change these paths and time as needed in the script.

# 🛠️ Requirements
- Python 3.x

# Required libraries:

- os

- shutil

- datetime

- schedule

- time

- Install schedule if it's not already installed:  pip install schedule

# 🚀 How to Use

- Clone the repository or copy the script.

- Edit the source_dir, destination_dir, and scheduled time if needed.

- Run the script: python auto_backup.py
- 
Keep the script running (e.g., on a terminal or background process), and it will back up the folder every day at the scheduled time.

# 🧠 How It Works

- Uses shutil.copytree() to copy the entire contents of the source folder.

- The script runs an infinite loop that checks every minute if it’s time to back up.

- A new backup folder is created with today’s date under the destination directory.

# 💡 Example Backup Path

- C:/Users/hp/Pictures/Backups/2025-07-09/

# ⚠️ Notes

- If a backup folder for today's date already exists, the script will skip creating it again.

- Make sure the script is kept running (or set it up as a background task on your OS).
