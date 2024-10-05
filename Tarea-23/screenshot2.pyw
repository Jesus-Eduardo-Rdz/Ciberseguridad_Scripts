#Darien Alexander Ñañez Torres
#Jesus Eduardo Rodriguez Garcia
#Christian Dominguez Villanueva

import pyautogui
import datetime
import subprocess

try:
    im = pyautogui.screenshot()
    fecha = datetime.datetime.now()
    nombre = r'SS_'
    nombre += str(fecha.strftime('%Y%m%d_%H%M%S'))
    nombre +='.png'
    im.save(nombre)

    xd=datetime.datetime.now()
    file_name=f"process_{xd.strftime('%Y%%m%d_%H%M%S')}.txt"
    output = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
    with open(file_name, 'w') as f:
        f.write(output.stdout)

except pyautogui.Error as e:
    print(f"Error al tomar la captura de pantalla: {e}")
except FileNotFoundError as e:
    print(f"Error: Archivo no encontrado: {e}")
