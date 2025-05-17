import tkinter as tk
import webview
from PIL import Image,ImageTk


# Función para abrir un mapa específico
def abrir_mapa(numero):
    ruta = f"mapar{numero}.html"
    webview.create_window(f"Mapa {numero}", ruta, width=800, height=600)
    webview.start()  # Esto bloqueará la interfaz hasta que se cierre la ventana del mapa

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("1600x900")
ventana.title("Líneas de Buses")

# Lista de nombres de líneas
lineas = [
    'LINEA1', 'LINEA2', 'LINEA3', 'LINEA4', 'LINEA5', 'LINEA6', 'LINEA7',
    'LINEA8', 'LINEA9', 'LINEA10', 'LINEA11', 'LINEA12', 'LINEA13', 'LINEA14',
    'LINEA15', 'LINEA16', 'LINEA17'
]

imagen = Image.open("Mapa de Manta foto.jpg") # Puede ser .png, .jpg, etc.
imagen = imagen.resize((1300, 900))
imagen_tk = ImageTk.PhotoImage(imagen)



# Crear etiqueta con la imagen
etiqueta = tk.Label(ventana, image=imagen_tk)
etiqueta.place(x=366,y=0,anchor='nw')


# Crear botones para admin
boton2 = tk.Button(ventana, text="admin", padx=50, pady=14,)
boton2.pack(side=tk.RIGHT,pady=0,padx=0)





for i, texto in enumerate(lineas, start=1):
    boton = tk.Button(ventana, text=texto, padx=160, pady=14,command=lambda i=i: abrir_mapa(i))
    boton.pack(anchor="w")

# Ejecutar la interfaz
ventana.mainloop()