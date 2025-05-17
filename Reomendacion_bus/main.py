import subprocess
import webbrowser
import time

# Lanza el servidor en segundo plano
subprocess.Popen(['python', 'servidor.py'])

# Espera un poco a que el servidor arranque
time.sleep(2)

# Abre el HTML en el navegador
webbrowser.open('ubicación.html')