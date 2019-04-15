from core.twitterSearchTool import twitterSearchTool

def searchTwitter():
	username = input(" Username: ")
	twitool = twitterSearchTool()
	twitool.getInfoProfile(username)

	username = twitool.username
	profilId = twitool.id
	name = twitool.name
	location = twitool.location
	url = twitool.url
	description = twitool.description
	protected = twitool.protected
	followers = twitool.followers
	friend = twitool.friends
	dateCreate = twitool.create
	geo = twitool.geo #
	verif = twitool.verified
	status = twitool.status
	langue = twitool.langue
	naissance = twitool.birth

	print("\n[@%s]" % (username))
	print("\n[+] Nome: %s" % (name))
	print("[+] Lingua: %s" % (langue.upper()))
	print("[+] Profilo privato: %s" % (protected))
	print("[+] ID profilo: %s" % (profilId))
	print("[+] Protetto: %s" % (protected))
	print("[+] Follower: %s | Following: %s" % (followers, friend))
	print("[+] Tweets: %s" % (status))
	print("[+] Città: %s" % (location))
	print("[+] Luogo di nascita: %s"  % (naissance))
	print("[+] Url: %s" % (url))
	print("[+] Data iscrizione: %s" % (dateCreate))
	print("[BIO]: %s" % (description))
