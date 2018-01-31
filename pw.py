#! python3
# py.pw - An insecure password locker program.

PASSWORDS =  {
    'email': 'your_password',
    'blog': 'your_password',
    'account': 'your_password',
}

import sys
import pdb
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python3 pw.py [account] copy account password')
    print('Exsisting keys')
    for key in PASSWORDS.keys():
        print('Accounts:   ' + key)
    sys.exit()

account = sys.argv[1] # first command line arg is the account name.

if account in PASSWORDS:
    pswd = PASSWORDS[account]
    pyperclip.copy(pswd)
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)

