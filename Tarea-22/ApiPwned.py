#Integrantes
#Darien Alexander Ñañez Torres
#Christian Dominguez Villanueva
#Jesus Eduardo Rodriguez Garcia

import requests
import json
import logging
import getpass
import six
import argparse          

if six.PY3:
    print('Python Version 3')
elif six.PY2:
    print('Error, Python Version 2')
    
key = getpass.getpass('Introduce el API Key solitada: ')

parser = argparse.ArgumentParser()
parser.add_argument('-email', dest='email', help='correo electronico')
params = parser.parse_args()

headers = {}
headers['content-type'] = 'application/json'
headers['api-version']= '3'
headers['User-Agent']= 'python'
headers['hibp-api-key']= key


url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
      params.email+'?truncateResponse=false'

try:
    r = requests.get(url, headers=headers)
    if r.status_code == 200: 
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo",params.email,"son:")
        else:
            print("El correo",params.email,"no ha sido filtrado")
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

   
   
