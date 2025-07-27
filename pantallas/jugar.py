from tkinter import ttk
from tkinter import *
from scripts.procesar_eleccion import procesar
def jugar(app, frame):
    for button in frame.winfo_children():
        button.destroy()
    app.ventana.title("Juego en progreso")
    style = ttk.Style()
    style.configure("BW.TLabel", font=("Arial", 30, "bold"), foreground="white", background="lightgray")
    frame.grid(column=0, row=1, padx=10, pady=5, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    labels = {}
    i = 0
    for row in range(3):
        for col in range(3):
            label = ttk.Label(frame, text="", style="BW.TLabel", width=10)
            label.grid(row=row, column=col, padx=3, pady=1, sticky="nsew")
            labels[i] = label 
            label.bind("<Button-1>", lambda e, r=row, c=col, idx=i: enviar_eleccion(idx,r,c))
            i += 1
    def enviar_eleccion(turno, r, c): 
        if((turno%2) == 0):
            labels[turno].config(text="X")
        else:
            labels[turno].config(text="O")
        procesar(turno, r, c)