import tkinter as tk
from canvas import *
from limpieza import *

def main():
    root = tk.Tk()
    root.title("Aplicacion")

    frame = ttk.Frame(root, padding="3 3 12 12")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    canvas = tk.Canvas(frame, width=500, height=690, bg="white")
    canvas.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    title_label = ttk.Label(frame, text="ACTIVIDAD ROOMBA")
    title_label.grid(row=0, column=0, sticky=(tk.N))

    sala = Zona("sala", "white", 500, 690, canvas)
    obj = Obstaculo("objeto", "pink", 90, 260, 101, 151, canvas)

    sala.dibuja_zona()
    obj.dibuja_obj()
    
    canvas.bind("<Button>", lambda event: detect_zona(event, canvas))
        
    root.mainloop()

if __name__ == "__main__":
    main()