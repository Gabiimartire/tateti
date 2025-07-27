from tkinter import ttk
from tkinter import *
class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("TA-TE-TI")
        self.ventana.geometry("600x600")
        style = ttk.Style()
        style.configure("BW.TLabel", font=("Arial", 30, "bold"), foreground="white", background="#630B57")
        titulo = ttk.Label(self.ventana, text="TA-TE-TI", style="BW.TLabel")
        titulo.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.config(bg="#630B57")
        from pantallas.mostrar_botones import botones
        botones(self)
        self.ventana.mainloop()
def main():
    app = App()
    return 0

if __name__ == "__main__":
    main()