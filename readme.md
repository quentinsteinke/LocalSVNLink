# Building from source
## Requirements
- [Python 3.11+](https://www.python.org/downloads/)

## Installation
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Run `pyinstaller --onefile linkHandler.py`
4. run `pyinstaller --onefile contextMenu.py`
5. Add the `linkHandler.exe` and `contextMenu.exe` to the Registry
    - `HKEY_CLASSES_ROOT\*\shell\open\command` with value `"C:\Path\To\Your\Executable\linkHandler.exe" "%1"`
    - `HKEY_CLASSES_ROOT\Directory\shell\Link Handler\command` with value `C:\path\to\linkHandler.exe "%1"`


[something](lsl://something)
