import winreg as reg
import sys

# Get the path to the Python executable dynamically
python_exe = sys.executable

# Define paths to your scripts
context_menu_script_path = r"D:\Quentin\Documents\projects\LocalSVNLink\dist\contextMenu.exe"
link_handler_script_path = r"D:\Quentin\Documents\projects\LocalSVNLink\dist\linkHandler.exe"

# Define the command to run for context menu
context_command = f'"{context_menu_script_path}" "%1"'

# Define the command to run for the link handler
link_handler_command = f'"{link_handler_script_path}" "%1"'

# Key paths for context menu
key_path = r"*\shell\GenerateSVNLink"
command_key_path = key_path + r"\command"

# Key paths for link handler
protocol_key_path = r"lsl"
protocol_command_key_path = protocol_key_path + r"\shell\open\command"

try:
    # Add context menu entry
    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(reg_key, "", reg.REG_SZ, "Generate SVN Link")
    reg.CloseKey(reg_key)

    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)
    reg.SetValue(reg_key, "", reg.REG_SZ, context_command)
    reg.CloseKey(reg_key)

    # Register link handler
    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, protocol_key_path)
    reg.SetValue(reg_key, "", reg.REG_SZ, "URL:lsl Protocol")
    reg.SetValueEx(reg_key, "URL Protocol", 0, reg.REG_SZ, "")
    reg.CloseKey(reg_key)

    reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, protocol_command_key_path)
    reg.SetValue(reg_key, "", reg.REG_SZ, link_handler_command)
    reg.CloseKey(reg_key)

    print("Context menu entry and link handler added successfully.")

except PermissionError:
    print("Permission denied. Try running this script as an administrator.")

except Exception as e:
    print(f"An error occurred: {e}")
