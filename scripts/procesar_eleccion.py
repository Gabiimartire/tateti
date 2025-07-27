def procesar(tablero, i):
    gano = 0
    gano1 = 0
    gano2 = 0
    for row in range(len(tablero)):
        for col in range(len(tablero[row])):
            print("row",row)
            print("Tablero row ",tablero[row])
            if(tablero[0] == tablero[row][col] and tablero[0] != ""):
                gano += 1
                if(gano == 3):
                    return print(f"ganó {i}")
            elif(row == col):
                if(tablero[row] == tablero[row][col] and tablero[0] != ""):
                    gano1 += 1
                    if(gano1 == 3):
                        return print(f"ganó {i}")
            elif(tablero[row] == tablero[0] and tablero[0] != ""):
                 gano2 += 1
                 if(gano == 3):
                    return print(f"ganó {i}")
    