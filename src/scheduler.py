import schedule
import time
import shutil

def print_hello():
    print("Hello, world!")

def backup_files():
    source_directory = "C:\\Users\\FIRDOUSE FATIMAH\\Desktop\\source_dir"  # Specify the directory you want to back up
    backup_directory = "C:\\Users\\FIRDOUSE FATIMAH\\Desktop\\backup_dir"  # Specify the backup destination directory

    try:
        shutil.copytree(source_directory, backup_directory)
        print("Backup completed successfully!")
    except Exception as e:
        print("Error during backup:", e)

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(print_hello)

# Schedule the backup task to run every day at 10:00 AM
schedule.every().day.at("12:56").do(backup_files)

# Run the scheduler loop to execute tasks
while True:
    schedule.run_pending()
    time.sleep(1)
