
tablero = [["o","x","x"],
           ["","o","x"],
           ["o","x","x"]]
opcion = "x"
gano1 = 0
gano2 = 0
for row in range(len(tablero)):
    gano = 0
    gano3 = 0
    for col in range(len(tablero[row])):
        print(gano3)
        #print("tabler[row][col]", tablero[row][col])
        #print("tabler[col][row]", tablero[col][row])
        if(tablero[row][col] == opcion and tablero[row][col] != ""):
            gano += 1
        if((col == row) and tablero[row][col] == opcion and tablero[row][col] != ""):
            gano1 += 1
        if((col + row == 2) and tablero[row][col] == opcion and tablero[row][col] != ""):
            gano2 += 1
        if(tablero[col][row] == opcion and tablero[col][row] != ""):
            gano3 += 1
    if(gano == 3 or gano1 == 3 or gano2 == 3 or gano3 == 3):
        print("gane")
    