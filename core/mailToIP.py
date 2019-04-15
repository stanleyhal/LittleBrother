import os, requests, re, json
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"

def mailToIP():
	def isp_host(ip):
		url = "http://ip-api.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(response)
		return values['isp']

	def ip_loc(ip):
		url = "https://extreme-ip-lookup.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(response)

		return(values['country']+', '+values['region']+', '+ values['city'])

	def get_domain(ip):
		s = socket.gethostbyaddr(ip)
		return(s[0])

	files = input(" Percorso: ")
	if not os.path.exists(files):
		print("\n"+warning+" File non trovato.")
	else:
		pass
	# clear()		
	print("\n"+wait+" Ricerca in corso ...")
	f = open(files, 'r')

	for line in f:
		line.strip()
		if "From: " in line:
			print(information+" Messaggio inviato da: "+line.replace("From: ",""))
		if 'Received: from' in line:
			ip_find = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
			for ip in ip_find:
				try:
					isp = isp_host(ip)
					loc = ip_loc(ip)
					domain = get_domain(ip)
				except:
					isp = 'Not found'
					loc = 'Not found'
					domain = 'Not found'

				print("""
[ %s ]
 + %s
 + %s
 + %s
  				""" % (ip, domain, isp, loc))
	f.close()
