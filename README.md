LittleBrother
=

LittleBrother è uno strumento utile per la raccolta di informazioni da fonti aperte (OSINT) che ha come fine la ricerca di informazioni su persone di nazionalità francese, svizzera, lussemburghese, belga e italiana (in questa versione). E' costituita da svariati moduli che consentono di effettuare una ricerca efficace. Non occorrono chiavi API nè identificativi di connessione.

![](https://i.ibb.co/GkVKF8C/screen.png)

Disclaimer
=
LittleBrother è stato sviluppato per effettuare ricerche su se stessi e per visualizzare le informazioni private e sensibili che ci si trascina dietro con l'utilizzo dei social network. Si sconsiglia vivamente l'uso di questo strumento su altre persone all'infuori di se stessi o da un utilizzo improprio.

Novità nella versione 6.0
=
- Inoltre (+)
	- In questa versione è stata effettuata la traduzione in italiano del tool, originalmente in francese, ed è stata  aggiunta la possibilità di effettuare ricerche su db italiani. 
	- E' stato aggiunto il file 'requirements.txt'.
	- Nuova interfaccia.
	- E' stato aggiunto un nuovo modulo di OSINT, il modulo 'Profilazione' sostituisce il database e il 'Dox maker' presente nella versione precedente di LittleBrother. Questo modulo permette di creare un profilo e di recuperare informazioni sui siti definiti dall'utilizzatore, salvaguardando questi dati e visualizzando gli ultimi post pubblicati sui social (ordinati a seconda della data di pubblicazione).
	- Sono stati aggiunti nuovi servizi di ricerca (Annuari) a seconda della localizzazione dell'utilizzatore. LittleBrother utilizza il vostro indirizzo IP per determinare la Nazione da cui siete collegate. In nessun caso saranno condivisi indirizzi IP o altre informazioni private. Potrete scegliere una Nazione diversa rispetto alla vostra per focalizzare le vostre ricerche.
	- La ricerca su Instagram e LinkedIn sono state integrate nel 'Lookup di persona'.
	- Nuovo modulo 'Ricerca dipendenti' che permette di ricercare dipendenti attraverso il nome di un'azienda e città.
	- I moduli di ricerca di informazioni su Instagram e Facebook sono stati migliorati per estrarre maggiori informazioni.  

- Sono state escluse (-)
	- Alcune librerie python (dnspython, socket e smtplib) sono state eliminate in questa versione.
	- 'Social engineering tool' è stato modificato in 'Other tool' ed è composto solamente dal modulo di brute-force di un Hash.
	- I moduli 'Spam Email' e 'SMS' sono stati eliminati da LittleBrother.
	- Il modulo di creazione di DoS 'Dox maker' è stato eliminato da LittleBrother.


Compatibile
=
- Windows
- MacOS
- Linux

Python version:
=
- Python3

Moduli Python
=
- requests
- bs4
- terminaltables
- colorama


Installazione
=
    git clone https://github.com/stanleyhal/LittleBrother
    cd LittleBrother
    python3 -m pip install -r requirements.txt
    python3 LittleBrother.py


Features
=
 - Lookup:

	- Lookup telefonico
	- Lookup  Email
	- Lookup Cognome / Nome
	- Lookup Cognome
	- Lookup indirizzo
	- Localizzazione di Mail ip
	- Localizzazione Ip
	- Localizzazione Bssid
	- Lettura dati Exif
	- Google search
	- Twitter
	- Instagram
	- Facebook
	- Ricerca dipendenti LinkedIn (New !)
	- Hash Bruteforce (New !)

 - Altri strumenti:

	- Hash Bruteforce

- Profilazione (New !)
	- Effettuare la profilazione
	- Database management
	- Creatore di Profili

Contributors
= 
[lulz3xploit](https://github.com/lulz3xploit)
= 
[H3L](https://github.com/lrhel)
