import os
import sys
import json
import subprocess

# Load and parse the settings JSON file
with open('svn_settings.json', 'r') as f:
    settings = json.load(f)
    possible_roots = settings['repo_roots']

# Parse the custom link to get the relative path
link = sys.argv[1]
relative_path = link.split('=')[1]

# Identify the correct SVN root
svn_root = None
for root in possible_roots:
    if os.path.exists(os.path.join(root, '.svn')):
        svn_root = root
        break

if not svn_root:
    print("No valid SVN repo root found!")
    sys.exit(1)

# Combine SVN root with relative path
full_path = os.path.join(svn_root, relative_path)

full_path = full_path.replace('/', '\\')

# Open the asset with the default application
subprocess.run(['explorer', '/select,', full_path])
