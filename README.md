# Stroom-monitoring t.b.v. het Research and Advice-project van Amy Brons
## benodigdheden
* Raspberry PI 3 of 4 (model B)
* Z-Wave ontvanger
* OpenHABian op een MicroSD-kaart
* Fibaro FGWP102 stroommeter
* De te testen Server
* een systeem met python 3.x (getest op Python 3.8 en 3.9)
## instructies
1. installeer de Raspberry PI met randapparatuur (zie: https://www.openhab.org/docs/installation/openhabian.html)
2. koppel de stroommeter aan de Z-Wave ontvanger en voeg deze toe aan OpenHAB als 'meter' (verander dit anders in de API-url!)
3. voeg een zgn. item toe voor de metingen in watts
4. verander het IP-adres (192.168.10.27) in de URL in de code
5. voer de file main.py uit 
6. voer een naam in voor de tabel met resulaten
7. er wordt, tot er CTRL-C wordt gegeven, elke minuut het energieverbruik op dat moment gelogd. Dit kan bijvoorbeeld worden geëxporteerd naar een CSV-bestand om daar verder verwerkt te worden

