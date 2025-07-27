from tkinter import ttk
from tkinter import *
from pantallas.jugar import jugar
def botones(app):
    style = ttk.Style()
    style.configure("BW.TButton", font=("Arial", 20, "bold"), foreground="black", background="#9d00ff")
    style.configure("BW.TFrame", background="#7D2181")
    frame = ttk.Frame(app.ventana, style="BW.TFrame")
    app.ventana.rowconfigure(1, weight=1)
    app.ventana.columnconfigure(0, weight=1)
    frame.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    button1 = ttk.Button(frame, text="Jugar", style="BW.TButton",  width=20)
    button1.grid(column=0, row=0, padx=10, pady=10)
    button1.config(width=20)
    button2 = ttk.Button(frame, text="Salir", style="BW.TButton",  width=20)
    button2.grid(column=0, row=1, padx=10, pady=10)
    button2.config(width=20)
    button1.bind("<Button-1>", lambda e: jugar(app, frame))
    button2.bind("<Button-1>", lambda e: frame.quit())
