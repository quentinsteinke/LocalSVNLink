import os
import sys
import json
import pyperclip

# Load and parse the settings JSON file
with open('svn_settings.json', 'r') as f:
    settings = json.load(f)
    possible_roots = settings['repo_roots']

# Get the full path of the selected asset
selected_file = sys.argv[1]

# Identify the correct SVN root
svn_root = None
for root in possible_roots:
    if selected_file.startswith(root):
        svn_root = root
        break

if not svn_root:
    print("Selected file is not in any known SVN repo root!")
    sys.exit(1)

# Determine the relative path
relative_path = os.path.relpath(selected_file, svn_root)

# Create the custom link
link = f"mysvn://open?path={relative_path}"

# Copy the link to clipboard
pyperclip.copy(link)
