# Wi-Fi Password Viewer (Windows)

A small Python script that lists the Wi-Fi profiles saved on a Windows computer and displays the details of the selected profile. If Windows allows access to the key, it will appear in plain text in the output.

> Use this only on your own computer or with the owner's explicit permission. A displayed Wi-Fi key is sensitive information: do not publish it or share screenshots containing it.

## How it works

The script uses `netsh`, a network utility built into Windows:

1. It retrieves the list of saved Wi-Fi profiles.
2. It displays the detected profiles and asks you to select one by number.
3. It displays the selected profile's details using `key=clear`. This may reveal the saved password.

The script recognizes profile labels in English and French. Access to the key depends on your Windows permissions and system configuration.

## Requirements

- Windows with `netsh` available.
- Python 3.7 or newer.
- At least one Wi-Fi profile saved on the computer.

No external Python dependencies are required.

## Usage

Open PowerShell or Command Prompt in the script's folder, then run:

```powershell
python passwd_viewer.py
```

Choose the number for the profile you want. The results will appear in the console. If the key is not displayed, try reopening the terminal with the required permissions and check that the profile is saved on this computer.

## Security and privacy

- Do not use this script to view Wi-Fi profiles saved on someone else's device without permission.
- Never publish command output, screenshots, or logs that contain a Wi-Fi key.
- If you share the repository, share only the source code, never any recovered passwords.
- If you later add examples or real screenshots, remove all sensitive information first and consider using a private repository.

## Limitations

- This script is designed for Windows and will not work as-is on Linux or macOS.
- It displays the information available for the selected profile and does not change network settings.
- Entering something other than a number may cause the script to stop with an error. Choose a number shown in the list.

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for the full text.
