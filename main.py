import subprocess


def get_wifi_passwords():
    """Gets the passwords of all saved Wi-Fi networks."""

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp437').split('\n')

    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    print("\n{:<30}| {:<}".format("WI-FI Name", "Password"))
    print("--------------------------------------------")

    for i in profiles:
        result = subprocess.check_output(['netsh', 'wlan', 'show',
                                          'profiles', i, 'key=clear']).decode('cp437').split('\n')
        results = []

        for b in result:
            if "Key Content" in b:
                results.append(b.split(":")[1][1:-1])

        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))


if __name__ == "__main__":
    get_wifi_passwords()
