import tkinter as tk
import tkinter.ttk as ttk
from canvas import *

# v = 1000 cm²/min
 
velocidad_limpieza = 1000  

def datos_zona(zona, ventana_principal):
    tiempo_limpieza = zonas[zona]['area'] / velocidad_limpieza
    ventana_info = tk.Toplevel(ventana_principal)
    ventana_info.title(zona)
    tk.Label(ventana_info, text=f"Zona: {zona}").pack()
    tk.Label(ventana_info, text=f"Área: {zonas[zona]['area']} cm²").pack()
    tk.Label(ventana_info, text=f"Tiempo estimado de limpieza: {tiempo_limpieza:.2f} minutos").pack()

def detect_zona(limpieza, ventana_principal):
    x, y = limpieza.x, limpieza.y
    for zona, info in zonas.items():
        x1, y1, x2, y2 = info['coordenadas']
        if x1 < x < x2 and y1 < y < y2:
            datos_zona(zona, ventana_principal)
            break