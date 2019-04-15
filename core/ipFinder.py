import requests, re, json
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"


def ipFinder():
	ip = input(" Indirizzo IP: ")
	print("\n"+wait+" Ricerca '%s'..." % (ip))

	TABLE_DATA = []

	url = "http://ip-api.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print(warning+" Indirizzo IP non valido.")

	else:
		infos = ("IP", ip)
		TABLE_DATA.append(infos)
		infos = ("ISP", values['isp'])
		TABLE_DATA.append(infos)
		infos = ("Organizzazione", values['org'])
		TABLE_DATA.append(infos)
		infos = ("Paese", values['country'])
		TABLE_DATA.append(infos)
		infos = ("Regione", values['regionName'])
		TABLE_DATA.append(infos)
		infos = ("Città", values['city'])
		TABLE_DATA.append(infos)
		infos = ("CAP", values['zip'])
		TABLE_DATA.append(infos)
		localisation = str(values['lat'])+', '+str(values['lon'])
		infos = ("Geo-localizzazione", localisation)
		TABLE_DATA.append(infos)
		infos = ("Maps", "https://www.google.it/maps?q="+localisation)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA, ip)
		print("\n"+table.table)
		# print("[ %s ]" % (ip))
		# print("\n IP: " + ip)
		# print(" Hostname: " + values['ipName'])
		# print(" ISP: " + values['isp'])
		# print(" Organizzazione: "+values['org'])
		# print(" Paese: " + values['country'])
		# print(" Regione: " + values['region'])
		# print(" Città: " + values['city'])
		# localisation = str(values['lat']) + ','+str(values['lon'])
		# print(" Geo-localizzazione: "+localisation)
		# print(" + Maps: https://www.google.it/maps?q=%s" % (localisation))
