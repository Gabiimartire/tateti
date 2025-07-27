from tkinter import ttk
from tkinter import *
from scripts.procesar_eleccion import procesar
def jugar(app, frame):
    for button in frame.winfo_children():
        button.destroy()
    app.ventana.title("Juego en progreso")
    style = ttk.Style()
    style.theme_use("clam")  
    style.configure("X.TLabel", font=("Arial", 30, "bold"), foreground="lightblue", background="purple")
    style.configure("BW.TLabel", font=("Arial", 30, "bold"), foreground="white", background="purple")
    frame.grid(column=0, row=1, padx=10, pady=5, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    labels = {}
    i = 0
    tablero = [[""] * 3 for _ in range(3)]
    for row in range(3):
        for col in range(3):
            label = ttk.Label(frame, text="", style="BW.TLabel", width=10, anchor="center")
            label.grid(row=row, column=col, padx=3, pady=1, sticky="nsew")
            labels[i] = label 
            label.bind("<Button-1>", lambda e, r=row, c=col, idx=i: enviar_eleccion(idx,r,c))
            i += 1

    turno = 0
    def enviar_eleccion(i, r, c): 
        nonlocal turno
        if((turno%2)==0):
            labels[i].config(text="X", style="X.TLabel")
            turno += 1
            tablero[r][c] = "X"
            procesar(tablero, "X", "Jugador X")
        else:
            labels[i].config(text="O")
            turno += 1
            tablero[r][c] = "O"
            procesar(tablero, "O", "Jugador O")
