from colorama import init, Fore,  Back,  Style
from core.instagramSearchTool import instagramSearchTool
from core.shortCutUrl import shortCutUrl
import os

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchInstagram():
	user = input(" Username: ")
	urlProfil = "https://instagram.com/"+user

	insta = instagramSearchTool()
	insta.getInfo(user)

	name = insta.name
	userId = insta.id
	images = insta.profi_pic_hd
	images = shortCutUrl(images)
	username = insta.username
	private = insta.private
	followers = insta.followers
	friend = insta.friends
	publication = insta.medias
	bio = insta.biography
	url = insta.url
	email = insta.email
	adresse = insta.adresse
	phone = insta.phone


	print("\n[%s]\n" % (username))
	print(found+" Nome: %s" % (name))
	print(found+" Immagine: %s" % (images))
	print(found+" ID: %s" % (userId))
	print(found+" Protetto: %s" % (private))
	print(found+" Follower: %s  |  Following: %s" % (followers, friend))
	print(found+" Pubblicazioni: %s" % (publication))
	print(found+" Bio: %s" % (bio))

	if url:
		print(found+" Url: %s" % (url))
	if email:
		print(found+" Email: %s" % (email))
	if phone:
		print(found+" Telefono: %s" % (phone))
	if adresse:
		print(found+" Indirizzo: %s" % (adresse))

	if not private:
		print("\n"+question+" Vuoi scaricare le ultime 12 foto pubblicate ?")

		while True:
			choix = input("\n [S/N]: ")

			if choix == "" or choix.upper() == "N":
				break
			
			elif choix.upper() == "S":
				print("\n"+question+" Dove vuoi salvare le foto ?")
				pathDefault = os.getcwd()
				print(Fore.YELLOW+" Percorso di default : "+pathDefault+Fore.RESET)
				path = input("\n Percorso: ")
				print("\n"+wait+" Download delle foto di '%s'\n" % (user))
			
				if not path:
					path = pathDefault
			
				insta.downloadPictures(urlProfil, path)
				print("\n"+found+" Download effettuato.")
				break
