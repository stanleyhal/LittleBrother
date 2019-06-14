#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style
from lib.menu import checkVersion, clear, menu
from lib.loading import thread_loading
#Lookup Menu
from core.searchEmail import SearchEmail
from core.searchPersonne import searchPersonne
from core.searchAdresse import searchAdresse
from core.searchUserName import searchUserName
from core.ipFinder import ipFinder
from core.bssidFinder import bssidFinder
from core.mailToIP import mailToIP
from core.employee_lookup import employee_lookup
from core.google import google
from core.facebookStalk import facebookStalk
from core.searchTwitter import searchTwitter
from core.searchInstagram import searchInstagram
from core.profilerFunc import profilerFunc
from core.searchNumber import searchNumber
#Other tool menu
from core.hashDecrypt import hashdecrypt


#Help & settings
from txt.help import helpLookup
import settings

init()
settings.init()

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"


checkVersion()
thread_loading()



mainOption = """
 [1] Lookup
 [2] Altri tool
 [3] Profiler
 [4] Cambia Nazionalità

 [e] Esci dallo script    [h] Aiuto    [c] Ripulisci Schermata"""


lookupOption = """
 [1] Lookup di persona        [8] Mail tracer
 [2] Lookup di username       [9] Ricerca dipendenti
 [3] Lookup di indirizzo      [10] Google search
 [4] Lookup di nr telef.      [11] Facebook GraphSearch
 [5] IP lookup                [12] Twitter info
 [6] SSID locator             [13] Instagram info
 [7] Lookup di email

 [b] Torna al menu principale    [e] Esci dallo script    [h] Aiuto    [c] Ripulisci Schermata"""

otherToolOption = """
 [1] Hash decrypter

 [b] Torna al menu principale    [e] Esci dallo script    [h] Aiuto    [c] Ripulisci Schermata
"""

profilerOption = """
 [1] Profilazione
 [2] Mostra tutti i Profili
 [3] Crea profilo

 [b] Torna al menu principale    [c] Ripulisci Schermata   [h] Aiuto
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg)
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)	 [6] IT (Italy)

 [b] Torna al menu principale   [c] Ripulisci Schermata   [h] Aiuto
"""

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n LittleBrother("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = settings.Profiler()
				pr.loadDatabase(settings.pathDatabase)
				database = pr.database

				choix = input("\n LittleBrother("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpProfiler)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e' or choix.lower() == 'exit':
					sys.exit("\n" + information + " Bye ! :)")
				elif choix.lower() == "1":
					if pr.count >= 1:
						while True: 
							profile = input(" Profilo: ")
							if profile != '':
								break
						data = pr.searchDatabase(profile, database=database)
						profilerFunc(data, path=settings.pathDatabase)
					else:
						print(warning+" Non è stato impostato alcun profilo. Si prega di crearne uno.")

				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Nome Cognome)"+Fore.RESET)
					while True:
						name = input(" Nome del Profilo: ")
						if name != '':
							break
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					while True:
						print(question+" Vuoi iscrivere un account Twitter su questo Profilo ?")
						choixPr = input(" [S/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							twitter = input("\n Twitter: ")
							info['URL']['Twitter'] = twitter
							break
					# print(found+" %s" % (twitter))
					while True:
						print(question+" Vuoi iscrivere un account Instagram su questo Profilo ?")
						choixPr = input(" [S/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							instagram = input("\n Instagram: ")
							info['URL']['Instagram'] = instagram
							break
					# print(found+" %s" % (instagram))
					while True:
						print(question+" Vuoi iscrivere un account facebook su questo Profilo ?")
						choixPr = input(" [S/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							facebook = input("\n Facebook: ")
							info['URL']['Facebook'] = facebook
							break
					# print(found+" %s" % (facebook))

					create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

					if create:
						print("\n"+found+" Il profilo '%s' è stato creato con successo." % (name))
					else:
						print("\n"+warning+" C'è stato un errore. Il profilo '%s' non è stato creato." % (name))

		elif choix.lower() == 'e' or choix.lower() == 'exit':
			sys.exit("\n" + information + " Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n LittleBrother(" + Fore.BLUE + "Lookup" + Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(settings.codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '3':
					searchAdresse(settings.codemonpays)
				elif lookup.lower() == '4':
					searchNumber(settings.codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '7':
					SearchEmail()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Comando inesistente")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n LittleBrother("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Comando inesistente")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n LittleBrother("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					settings.codemonpays = "FR"
					settings.monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					settings.codemonpays = "BE"
					settings.monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					settings.codemonpays = "CH"
					settings.monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					settings.codemonpays = "LU"
					settings.monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					settings.codemonpays = "XX"
					settings.monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '6':
					settings.codemonpays = "IT"
					settings.monpays = "Italia"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Comando inesistente")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")
