#!python3.4

__author__ = 'ampersamd'

import os, shutil, archiveContents
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter


class MailArchiveApp(App):
	pass


class MailArchiveRoot(BoxLayout):
	pass


class AddMailForm(BoxLayout):
	# TODO Remove script from addMail method
	folderPath = ObjectProperty()
	mailName = ObjectProperty()

	def addMail(self):
		# gets name of mail and
		folderLocation = self.folderPath.text
		mailName = self.mailName.text

		pages = os.listdir(folderLocation)
		pages.remove('.DS_Store')
		os.chdir(folderLocation)

		mail = canvas.Canvas(mailName, pagesize=letter)

		#TODO: Verify all apge images are compatible images
		"""
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
		"""

		# adds each image in pages list to mail .pdf file
		for entry in pages:
			mail.drawImage(entry, 0, 0, 11 * inch, 17 * inch)
			mail.showPage()

		mail.save()
		shutil.move(folderLocation + '/' + mailName, '/Users/{USER}/Documents/Mail Archive')


# TODO find if mail name exists in mail archive



"""
print('\nWelcome to Mail Archiving\n')

while True:
    task = input("What would you like to do?\nEnter 'info' for more information.\n")

    if task.lower() == 'info':
        print("Add: Add new mail item\nView: View all archived mail items\nExit: Exit mail digitlizer\n)
    elif task.lower() == 'add':
        addMail()
    elif task.lower() == 'view':
        print('\nMail Archives\n______________________________\n')
        for item in archiveContents.archiveContents:
            print(item + '\n')
    elif task.lower() == 'exit':
       exit()

"""

if __name__ == "__main__":
	MailArchiveApp().run()
