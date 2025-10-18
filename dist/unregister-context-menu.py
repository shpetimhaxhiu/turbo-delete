import winreg

# Registry keys to remove for different selection types
registry_entries = [
    # Single directory selection
    (R'Directory\shell\turbo-delete\command', R'Directory\shell\turbo-delete'),
    # Multiple file/folder selection
    (R'AllFileSystemObjects\shell\turbo-delete\command', R'AllFileSystemObjects\shell\turbo-delete'),
    # Background context menu (right-click in empty space)
    (R'Directory\Background\shell\turbo-delete\command', R'Directory\Background\shell\turbo-delete'),
]

for command_key, shell_key in registry_entries:
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, command_key)
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, shell_key)
    except FileNotFoundError:
        # Key doesn't exist, continue
        pass
