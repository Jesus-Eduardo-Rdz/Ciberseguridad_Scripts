import requests
import json
import logging
import getpass

key = getpass.getpass('Introduce el API Key solitada: ')

email =input('Ingrese el correo a investigar: ')
headers = {}
headers['content-type'] = 'application/json'
headers['api-version']= '3'
headers['User-Agent']= 'python'
headers['hibp-api-key']= key


url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
      email+'?truncateResponse=false'

try:
    r = requests.get(url, headers=headers)
    if r.status_code == 200: 
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo",email,"son:")
        else:
            print("El correo",email,"no ha sido filtrado")
        for filtracion in data:
            print(filtracion["Name"])
        msg = email+" Filtraciones encontradas: "+str(encontrados)
        print(msg)
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)
    else:
        msg = r.text
        print(msg)
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.ERROR)
        logging.error(msg)
except Exception as e:
   logging.error('Error al obtener la solicitud:$s',e)
   print (f'Ha ocurrido un error : {e}')

   
   
