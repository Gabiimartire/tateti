from tkinter import messagebox
def ganador(player):
    messagebox.showinfo("FELICITACIONES! ", player)
def procesar(tablero, opcion, i):
    p_ganador = ""
    gano1 = 0
    gano2 = 0
    for row in range(len(tablero)):
        gano = 0
        gano3 = 0
        for col in range(len(tablero[row])):
            if(tablero[row][col] == opcion and tablero[row][col] != ""):
                gano += 1
            if((col == row) and tablero[row][col] == opcion and tablero[row][col] != ""):
                gano1 += 1
            if((col + row == 2) and tablero[row][col] == opcion and tablero[row][col] != ""):
                gano2 += 1
            if(tablero[col][row] == opcion and tablero[col][row] != ""):
                gano3 += 1
        if(gano == 3 or gano1 == 3 or gano2 == 3 or gano3 == 3):
            p_ganador = f"¡Ganaste {i}!"
            ganador(p_ganador)