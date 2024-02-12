import tkinter as tk
import tkinter.ttk as ttk

zonas = {
    'Zona 1': {'coordenadas': (0, 0, 500, 150), 'color': 'light blue', 'area': 500 * 150},
    'Zona 2': {'coordenadas': (0, 150, 101, 630), 'color': 'purple', 'area': 480 * 101},
    'Zona 3': {'coordenadas': (191, 150, 500, 630), 'color': 'light green', 'area': 309 * 480},
    'Zona 4': {'coordenadas': (101, 410, 191, 630), 'color': 'orange', 'area': 90 * 220},
}

class Zona():
    def __init__(self, nombre, color, ancho, alto, canvas):
        self.nombre = nombre
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.canvas = canvas
        
    def get_area(self):
        return self.ancho * self.alto

    def dibuja_zona(self):
        for self.zona, info in zonas.items():
            self.canvas.create_rectangle(*info['coordenadas'], fill=info['color'])
        for self.zona in zonas.items()
        
class Obstaculo():
    def __init__(self, nombre, color, ancho_obj, alto_obj, x, y, canvas:tk.Canvas):
        self.nombre = nombre
        self.color = color
        self.ancho_obj = ancho_obj
        self.alto_obj = alto_obj
        self.x = x
        self.y = y
        self.canvas = canvas
        
    def get_area_obj(self):
        return self.ancho_obj * self.alto_obj
    
    def dibuja_obj(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.ancho_obj, self.y + self.alto_obj, outline="orange", fill=self.color)
        self.canvas.create_text(self.x + self.ancho_obj/2 -30 ,self.y + self.alto_obj/2 -20, text=f"{self.nombre}\n{self.ancho_obj}cm x{self.alto_obj}cm \n {self.get_area_obj()} cm^2", anchor="nw", fill="black")
