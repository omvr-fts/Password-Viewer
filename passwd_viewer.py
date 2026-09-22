import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

def main():
    profiles = subprocess.check_output(
        "netsh wlan show profiles",
        shell=True,
        encoding="utf-8",
        errors="replace"
    )

    names = []

    for line in profiles.splitlines():
        if ":" not in line:
            continue

        left, right = line.split(":", 1)

        if (
            "All User Profile" in left
            or "Profil Tous les utilisateurs" in left
        ):
            name = right.strip()

            if name:
                names.append(name)

    if not names:
        print("Aucun profil WiFi trouvé.")
        return

    print("\nProfils WiFi trouvés:\n")

    for i, name in enumerate(names, 1):
        print(f"[{i}] {name}")

    ch = int(input("\nChoisissez le numéro du WiFi : "))

    if ch < 1 or ch > len(names):
        print("Numéro invalide.")
        return

    wifi = names[ch - 1]

    result = subprocess.check_output(
        f'netsh wlan show profile name="{wifi}" key=clear',
        shell=True,
        encoding="utf-8",
        errors="replace"
    )

    print("\n" + result)

main()