'''
Nombre: Rincon Ulloa Yazmin Elizabeth
Fecha: Lunes 23 de Octubre del 2023
Descripcion: Imprimir URL
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de allende"
key = "9gUnckHX2Z3nwC7ZmDbEsNbBfhW9Nh88"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()

#Imprimir la URL
print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
elif json_status !=0:
    print("API Status: " + str(json_status) + " = A failuer route call.\n")

