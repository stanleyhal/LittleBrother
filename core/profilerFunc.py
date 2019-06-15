from colorama import init, Fore,  Back,  Style
from core.watcher import watcher
from core.instagramSearchTool import instagramSearchTool
from core.facebookSearchTool import facebookSearchTool
from core.twitterSearchTool import twitterSearchTool
from core.Profiler import Profiler
from terminaltables import SingleTable
import time, os

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"

def profilerFunc(profile='', path=''):

	from datetime import date
	today = date.today()
	
	today = None
	profileID = None
	profileName = None 
	phones = None 
	emails = None 
	instagramLocation = None 
	twitterLocation = None
	facebookLocation = None
	facebookWork = None
	facebookUsername = None 
	twitterUsername = None
	instagramUsername = None
	facebookID = None 
	facebookUrl = None 
	twitterID = None 
	twitterUrlAccount = None
	instagramID = None
	InstagramUrlAccount = None
	placeVisited = None
	twitterBio = None 
	instagramBio = None

	list_biographi = []
	list_placeVisited = []
	list_emails = []
	list_phones = []
	list_urls = []
	list_news = []

	if profile:
		profileName = profile['name']
		profileID = profile['id']
		file = profile['file']

		print("\n"+found+" Profilo selezionato: %s (%s)\n" % (profileName, profileID))

		pr = Profiler()
		dataProfile = pr.readProfile(file, path=path)

		if dataProfile:
			for data in dataProfile:
				if data.upper() == 'URL':
					try:
						url_twitter = dataProfile[data]['Twitter']
					except:
						url_twitter = None
					
					try:
						url_instagram = dataProfile[data]['Instagram']
					except:
						url_instagram = None
					
					try:
						url_facebook = dataProfile[data]['Facebook']
					except:
						url_facebook = None

		name_txt = file.replace(".prfl", ".txt")
		path_txt = path+'\\'+name_txt
		
		if url_twitter:
			twitterInfoDic = {"Twitter": {}}
			twittool = twitterSearchTool()
			twittool.getInfoProfile(url_twitter)
			twitterID, twitterInfoDic['Twitter']['id'] = twittool.id, twittool.id 
			twitterName, twitterInfoDic['Twitter']['name'] = twittool.name, twittool.name
			twitterUsername, twitterInfoDic['Twitter']['username'] = twittool.username, twittool.username
			twitterLocation, twitterInfoDic['Twitter']['location'] = twittool.location, twittool.location
			twitterUrlFound, twitterInfoDic['Twitter']['urlFound'] = twittool.url, twittool.url
			twitterBio, twitterInfoDic['Twitter']['description'] = twittool.description, twittool.description
			twitterUrlAccount, twitterInfoDic['Twitter']['urlAccount'] = url_twitter, url_twitter
		if url_facebook:
			facebookInfoDic = {"Facebook": {}}
			fbtool = facebookSearchTool()
			fbtool.getInfoProfile(url_facebook)
			facebookID, facebookInfoDic['Facebook']['id'] = fbtool.facebookId, fbtool.facebookId
			facebookName, facebookInfoDic['Facebook']['name'] = fbtool.name, fbtool.name
			facebookLocation, facebookInfoDic['Facebook']['location'] = fbtool.address, fbtool.address
			facebookWork, facebookInfoDic['Facebook']['job'] = fbtool.job, fbtool.job
			facebookUrl, facebookInfoDic['Facebook']['urlAccount'] = url_facebook, url_facebook
			facebookUsername, facebookInfoDic['Facebook']['username'] = fbtool.username, fbtool.username
			facebookAffiliation, facebookInfoDic['Facebook']['affiliations'] = fbtool.affiliations, fbtool.affiliations
		if url_instagram:
			instagramInfoDic = {"Instagram": {}}
			instatool = instagramSearchTool()
			instatool.getInfo(url_instagram)
			instagramID, instagramInfoDic['Instagram']['id'] = instatool.id, instatool.id
			instagramBio, instagramInfoDic['Instagram']['description'] = instatool.biography, instatool.biography
			instagramUsername, instagramInfoDic['Instagram']['username'] = instatool.username, instatool.username
			instagramName, instagramInfoDic['Instagram']['name'] = instatool.name, instatool.name
			instagramEmail, instagramInfoDic['Instagram']['email'] = instatool.email, instatool.email
			instagramPhone, instagramInfoDic['Instagram']['phone'] = instatool.phone, instatool.phone
			instagramUrlFound, instagramInfoDic['Instagram']['urlFound'] = url_instagram, url_instagram
			instagramLocation, instagramInfoDic['Instagram']['location'] = instatool.adresse, instatool.adresse
			InstagramUrlAccount, instagramInfoDic['Instagram']['urlAccount'] = instatool.urlAccount, instatool.urlAccount

		for data in dataProfile:
			if data.upper() == 'TWITTER':
				if dataProfile[data]['name'] != twitterName:
					dataProfile[data]['name'] = twitterName
					list_news.append(twitterName)
				if dataProfile[data]['location'] != twitterLocation:
					dataProfile[data]['location'] = twitterLocation
					list_news.append(twitterLocation)
				if dataProfile[data]['urlFound'] != twitterUrlFound:
					dataProfile[data]['urlFound'] = twitterUrlFound
					list_news.append(twitterUrlFound)
				if dataProfile[data]['description'] != twitterBio:
					dataProfile[data]['description'] = twitterBio
					list_news.append(twitterBio)

			elif data.upper() == "FACEBOOK":
				if dataProfile[data]['name'] != facebookName:
					dataProfile[data]['name'] = facebookName
					list_news.append(facebookName)
				if dataProfile[data]['location'] != facebookLocation:
					dataProfile[data]['location'] = facebookLocation
					list_news.append(facebookLocation)
				if dataProfile[data]['job'] != facebookWork:
					dataProfile[data]['job'] = facebookWork
					list_news.append(facebookWork)
				if dataProfile[data]['affiliations'] != facebookAffiliation:
					dataProfile[data]['affiliations'] = facebookAffiliation
					list_news.append(facebookAffiliation)

			elif data.upper() == 'INSTAGRAM':
				if dataProfile[data]['name'] != instagramName:
					dataProfile[data]['name'] = instagramName
					list_news.append(instagramName)
				if dataProfile[data]['location'] != instagramLocation:
					dataProfile[data]['location'] = instagramLocation
					list_news.append(instagramLocation)
				if dataProfile[data]['urlFound'] != instagramUrlFound:
					dataProfile[data]['urlFound'] = instagramUrlFound
					list_news.append(instagramUrlFound)
				if dataProfile[data]['description'] != instagramBio:
					dataProfile[data]['description'] = instagramBio
					list_news.append(instagramBio)

		if url_twitter:
			dataProfile.update(twitterInfoDic)
		if url_facebook:
			dataProfile.update(facebookInfoDic)
		if url_instagram:
			dataProfile.update(instagramInfoDic)
		
		if url_twitter or url_facebook or url_instagram:
			pr.writeProfile(file, path, dataProfile)

			if instagramEmail:
				list_emails.append(instagramEmail)
		
			placeVisited = "; ".join(list_placeVisited)

			for bio in list_biographi:
				regex = RegexTool(bio)
				emails = regex.Email().email
				phones = regex.Telephone().telephone
				urls = regex.Url().url

				for email in emails:
					list_emails.append(email)
				for phone in phone:
					list_phone.append(phone)
				for url in urls:
					list_urls.append(urls)

			if list_emails:
				emails = ", ".join(list_emails)
			else:
				emails = ''
			
			if list_phones:
				phones = ", ".join(list_phones)
			else:
				phones = ''

			if list_urls:
				urls = ", ".join(list_urls)
			else:
				urls = ''

			global_info = """
	Date: %s

	Profilo ID : %s
	Nome, Cognome: %s

	Telefono: %s
	Email: %s
	Localizzazione: %s ; %s ; %s
	Professione: %s
	Alias: %s ; %s ; %s

	Facebook  (%s) - %s
	Twitter   (%s) - %s
	Instagram (%s) - %s

	Indirizzi visitati: %s

	Descrizioni: 
	%s	

	%s
			""" % (
					today, profileID, profileName, phones, emails, 
					instagramLocation, twitterLocation, facebookLocation,
					facebookWork,
					facebookUsername, twitterUsername, instagramUsername,
					facebookID, facebookUrl, twitterID, twitterUrlAccount, instagramID, InstagramUrlAccount,
					placeVisited,
					twitterBio, instagramBio
					)

			lists = []
			w = watcher()
			if url_instagram:
				w.instagramWatcher(url_instagram)
				lists.append(w.medias)
			if url_twitter:
				w.twitterWatcher(url_twitter)
				lists.append(w.tweet)
			
			if lists:
				data = pr.timeSort(lists, reverse=True) # True: Ordre Decroissant, False: Ordre croissant (defaut : False)

				TABLE_DATA = [
					('Date', 'Domain', 'Publication', 'Localisation'),
				]

				for d in data:
					date = time.ctime(d)
					domain = data[d]['domain']
			
					if domain == "Twitter":
						tweet = data[d]['tweet'].replace("https://twitter.com", '')
						tuples = (date, domain, tweet, 'None')
						TABLE_DATA.append(tuples)
			
					else:
						publication = data[d]['urlMedia']
						publicationShort = shortCutUrl(publication)
						typePublication = data[d]['type']
						localisation = data[d]['location']
				
						if localisation:
							list_placeVisited.append(localisation)
				
						tuples = (date, domain, publicationShort, localisation)
						TABLE_DATA.append(tuples)

				tableLastPost = SingleTable(TABLE_DATA, " Last post ")

				print(tableLastPost.table)
				print("-------------")
				print("\n"+global_info)

				if len(list_news) > 0:
					newsItems = "; ".join(list_news)
					print("Novità:\n"+newsItems)
		
				print("-------------")

				print(question+" Vuoi esportare i dati recuperati in '%s' ? " % (name_txt))

				while True:
					choix = input("\n [S/n]: ")

					if choix == '' or choix.upper() == 'S':
						f = pr.exportText(name_txt, path, global_info)
						if f:
							print("\n"+found+" Dati esportati con successo !")
							print(" %s" % (path_txt))
						else:
							print("\n"+warning+" C'è stato un errore, i dati non sono stati esportati !")
						break

					elif choix.upper() == 'N':
						break

				print("\n"+question+" Vuoi creare una copia di '%s' ? " % (name_txt))
		
				while True:
					choix = input("\n [S/N]: ")

					if choix.upper() == 'S':
						print("\n"+question+" Dove vuoi salvare la copia ?")
						pathDefault = os.getcwd()
						print(Fore.YELLOW+" Default path: "+pathDefault+Fore.RESET)
						path = input("\n Path: ")

						if not path:
							path = pathDefault
							path += "\\"
						if path.endswith(".txt"):
							path = path_txt
						else:
							path = path+name_txt

						with open(path, 'w', encoding="utf-8") as f:
							f.write(global_info)
							f.close()

						print("\n"+found+" '%s' è stato copiato con successo !" % (name_txt))
						break

					elif choix == '' or choix.upper() == 'N':
						break        

	else:
		print("\n"+warning+" Profilo non trovato")
