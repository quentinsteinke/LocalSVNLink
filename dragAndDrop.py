import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import sys
import subprocess

# Paths to your scripts
CONTEXT_MENU_SCRIPT_PATH = r"C:\Users\Quentin Steinke\Documents\ScriptProjects\LocalSVNLink\contextMenu.py"
LINK_HANDLER_SCRIPT_PATH = r"C:\Users\Quentin Steinke\Documents\ScriptProjects\LocalSVNLink\linkHandler.py"

def on_drop(event):
    file_path = event.data.strip()
    # Handle the file
    subprocess.run([sys.executable, CONTEXT_MENU_SCRIPT_PATH, file_path])

def handle_link():
    link = link_entry.get()
    if link.startswith("lsl://"):
        # Handle the link
        subprocess.run([sys.executable, LINK_HANDLER_SCRIPT_PATH, link])

root = TkinterDnD.Tk()
root.title("SVN Helper")
root.geometry("300x200")  # Adjust size as needed

label = tk.Label(root, text="Drag & Drop Files or Paste Links")
label.pack(pady=10)

# Text entry for link
link_entry = tk.Entry(root, width=40)
link_entry.pack(pady=10)

# Button to process link
process_button = tk.Button(root, text="Process Link", command=handle_link)
process_button.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
