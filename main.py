import time
import sqlite3
import requests
import json

#vraag over de te loggen situatie
print('Welke situatie wordt er gelogd?: ')
x = input()

#verbind met SQlite DB
conn = sqlite3.connect('test.db')
c = conn.cursor()

#Maak zo nodig Tabel aan
gentable="CREATE TABLE IF NOT EXISTS {} (TimeStamp TEXT, PWR INTEGER)".format(x)
c.execute(gentable)
conn.commit()

#logging
def main():
    try:
        #vraag huidige verbruik op
        response = requests.get("http://192.168.10.27:8080/rest/items/meter_Electricmeterwatts?state")
        json_data = json.loads(response.text)
        CurrPwr = json_data["state"]
        #sla dat op
        insertstatement = "insert into {} (TimeStamp,PWR) values (CURRENT_TIMESTAMP,?)".format(x)
        c.execute(insertstatement, (CurrPwr,))
        print(CurrPwr)
        conn.commit()
    except:
        #als dit verschijnt: Debuggen!
        print('ERROR')
    #elke minuut
    time.sleep(60)
#het uitvoeren
while True:
    main()