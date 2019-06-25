# coding=utf-8

import requests
import json

url = 'http://sozluk.gov.tr/gts'

params = dict(
    ara='alay'
)

resp = requests.get(url=url, params=params)
data = resp.json()
print(json.dumps(data, indent=4, sort_keys=True))

print('Anlam sayısı: ' + str(len(data[0]["anlamlarListe"])))

for x in range(len(data[0]["anlamlarListe"])):
	print('Anlam: ' + data[0]["anlamlarListe"][x]["anlam"])
