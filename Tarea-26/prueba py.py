#Darien Alexander Ñañez Torres
#Jesus Eduardo Rodriguez Garcia
#Chritian Dominguez Villanueva 
import subprocess
from openpyxl import Workbook
try:
    ps_script= 'C:/Users/Eduardo/Documents/Ciberseguridad/Servicios.ps1'
    cm = ["powershell", "-File", ps_script]
    output = subprocess.check_output(cm, universal_newlines=True)
    lines = output.splitlines()
    wb = Workbook()
    ws = wb.active
    for i, line in enumerate(lines):
        ws.cell(row=i+1, column=1).value = line
    wb.save("service.xlsx")
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo de PowerShell en la ruta {ps_script}")

except Exception as e:
    print(f"Error: {e}")
