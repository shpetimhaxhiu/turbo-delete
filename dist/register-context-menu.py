import winreg
import os

appdata_dir = os.getenv('APPDATA') + r'\turbo-delete\bin\td.exe'

# Registry keys for different selection types
registry_entries = [
    # Single directory selection
    (R'Directory\shell\turbo-delete', R'Directory\shell\turbo-delete\command', Rf'"{appdata_dir}" "%1"'),
    # Multiple file/folder selection
    (R'AllFileSystemObjects\shell\turbo-delete', R'AllFileSystemObjects\shell\turbo-delete\command', Rf'"{appdata_dir}" "%*"'),
    # Background context menu (right-click in empty space)
    (R'Directory\Background\shell\turbo-delete', R'Directory\Background\shell\turbo-delete\command', Rf'"{appdata_dir}" "%V"'),
]

for shell_key, command_key_path, command in registry_entries:
    # Create shell key
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, shell_key)
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path)
    
    # Set display name
    shell_key_handle = winreg.OpenKey(
        winreg.HKEY_CLASSES_ROOT, shell_key, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(shell_key_handle, '', 0, winreg.REG_SZ, 'Turbo Delete')
    shell_key_handle.Close()
    
    # Set command
    command_key_handle = winreg.OpenKey(
        winreg.HKEY_CLASSES_ROOT, command_key_path, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(command_key_handle, '', 0, winreg.REG_SZ, command)
    command_key_handle.Close()
