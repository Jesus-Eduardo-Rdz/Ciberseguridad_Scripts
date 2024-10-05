#Jesus Eduardo Rodriguez Garcia
#Darien Alexander Ñañez Torres
#Christian Dominguez Villanueva

import subprocess

monitoreo_conexiones = './monitoreo_conexiones.sh'

try:
    result = subprocess.run(monitoreo_conexiones, shell=True, capture_output=True, text=True, check=True)
    
    with open('conexiones_sospechosas.txt', 'w') as f:
        f.write(result.stdout)
    
    print("Salida guardada en 'conexiones_sospechosas.txt'.")

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el script de Bash: {e}\nSalida de error: {e.stderr}")

except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")

