import requests
import getpass
import os

pw_list = ''  # Globally define variable.


def guessPassword():
    password = getpass.getpass(
        prompt='Test your password, enter it here (q to quit):')
    Attempt = 0
    if password.lower() == 'q':
        exit()
    elif password in pw_list:
        pw_position = pw_list.index(password)
        print(
            f"Found the password in position {pw_position} of a total of {len(pw_list)} passwords")
    elif password not in pw_list:
        print('That password is not in this list.')
    guessPassword()


try:  # Do I already have the pwd file?
    with open('passwords.txt', 'r') as f:
        pw_list = f.read().splitlines()


except:  # File isn't there, so download it.
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt'
    r = requests.get(url)
    with open('passwords.txt', 'wb') as f:
        f.write(r.content)
    with open('passwords.txt', 'r') as f:
        pw_list = f.read().splitlines()


guessPassword()
