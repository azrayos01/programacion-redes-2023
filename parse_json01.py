'''
Nombre: Rincon Ulloa Yazmin Elizabeth
Fecha: Lunes 23 de Octubre del 2023
Descripcion: Importando API
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de allende"
key = "9gUnckHX2Z3nwC7ZmDbEsNbBfhW9Nh88"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print(json_data ['route']['sessionId'])

#Extraer la distancia y el tiempo
print(json_data ['route']['distance'])
print(json_data ['route']['time'])
#Extraer del primer elemento Legs el campo formattedTime
print(json_data ['route']['formattedTime'])