__author__ = 'ampersamd'

import archiveContents
from archive import *


print('\nWelcome to Mail Archiving\n')

while True:
    task = input("What would you like to do?\nEnter 'info' for more information.\n")

    if task.lower() == 'info':
        print("""Add: Add new mail item\n
            View: View all archived mail items\n
            Exit: Exit mail digitlizer\n""")
    elif task.lower() == 'add':
        addMail()
    elif task.lower() == 'view':
        print('\nMail Archives\n______________________________\n')
        for item in archiveContents.archiveContents:
            print(item + '\n')
    elif task.lower() == 'exit':
       exit()