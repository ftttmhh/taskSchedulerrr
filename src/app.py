import tkinter as tk
from tkinter import filedialog
import shutil

def backup_files():
    source_directory = source_entry.get()
    backup_directory = backup_entry.get()

    try:
        shutil.copytree(source_directory, backup_directory)
        status_label.config(text="Backup completed successfully!")
    except Exception as e:
        status_label.config(text=f"Error during backup: {e}")

# Create the main application window
root = tk.Tk()
root.title("Task Scheduler")

# Source directory label and entry
source_label = tk.Label(root, text="Source Directory:")
source_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)

# Backup directory label and entry
backup_label = tk.Label(root, text="Backup Directory:")
backup_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
backup_entry = tk.Entry(root, width=50)
backup_entry.grid(row=1, column=1, padx=5, pady=5)

# Backup button
backup_button = tk.Button(root, text="Backup Files", command=backup_files)
backup_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
