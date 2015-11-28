# Python 3
# Mail Archive

import os, shutil, archiveContents
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter


def addMail():
    # gets name of mail
    folderLocation = input("Path to pages:\n")

    # mailName = input("Name this piece of mail:\n") + '.pdf'
    print("Name this piece of mail: ")
    mailName = nameExists()

    mail = canvas.Canvas(mailName, pagesize=letter)

    # changes directory to location of mail pages
    os.chdir(folderLocation)

    # lists all pages to be added to mail file
    pages = os.listdir()
    pages.remove('.DS_Store')

    # verifies all entries in pages list are images
    for entry in pages:
        root, ext = os.path.splitext(entry)
        if ext in ['.jpg', '.jpeg']:
            continue
        else:
            deleteDecision = input('\n{0} is not a valid image type. Would you like to delete?\n'.format(entry))
            if deleteDecision.lower().startswith('y'):
                pages.remove(entry)
            elif deleteDecision.lower().startswith('n'):
                print('\nExiting program...\n')
                exit()
            else:
                print("\nInvalid option. Exiting program.\n")
                exit()

    # adds each image in pages list to mail .pdf file
    for entry in pages:
        mail.drawImage(entry, 0, 0, 11 * inch, 17 * inch)
        mail.showPage()

    mail.save()
    shutil.move(folderLocation + '/' + mailName, '/Users/Sam/Documents/Mail Archive')


# gets mailname from user and checks if it exists in mail archive
def nameExists():
    while True:
        name = input("\n") + '.pdf'
        if name in archiveContents.archiveContents:
            print("This filename is in use. Please choose a new one:\n")
        else:
            return name
