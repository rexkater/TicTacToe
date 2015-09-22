print("\n \t\t Equis & Cero\n")
print(" Reglas: \n\n 1) El primer turno le pertenece al jugador que use las equis."
      "\n 2) El segundo turno le pertenece al jugador que use los ceros, y así alternadamente."
      "\n 3) Hay que ingresar las coordenadas en 'x' & 'y' para hacer una marca. (Van del 0 al 2)"
      "\n 4) El primer jugador en hacer una línea de sus marcas es el ganador."
      "\n 5) De no haber más jugadas posibles, el juego será reiniciado. \n")

matriz = [[' ',' ',' '],[' ',' ',' '],[' ', ' ',' ']]
counter = 0

while counter < 9:

    def display():
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if j == 1:
                    print(" |",end=' ')
                print("  " + matriz[i][j], end=' ')
                if j == 1:
                    print(" |",end=' ')
                j += 1
            if i < 2:
                print("\n -----------------")
            else:
                print()
            i += 1
            
    display()

    x = int(input("\n Indique la coordenada en x: "))
    y = int(input(" Indique la coordenada en y: "))
    print()
    
    if -1 < x < 3 and -1 < y < 3 and counter%2 == 0:
        matriz[x][y] = 'x'

    elif -1 < x < 3 and -1 < y < 3 and counter%2 == 1:
        matriz[x][y] = '0'

    else:
        print("Las coordenadas indicadas no son válidas. \n")

    counter += 1

    a = 0
    while a < 3:
        b = 0
        
        if matriz[a][b] == 'x'  and matriz[a][b+1] == 'x'  and matriz [a][b+2] == 'x':
            print("El ganador es el jugador al cual le corresponden las equis.")
            counter += 10
            break
        elif matriz[b][a] == 'x'  and matriz[b+1][a] == 'x'  and matriz [b+2][a] == 'x':
            print("El ganador es el jugador al cual le corresponden las equis.")
            counter += 10
            break
        elif matriz[a][b] == '0'  and matriz[a][b+1] == '0'  and matriz [a][b+2] == '0':
            print("El ganador es el jugador al cual le corresponden los ceros.")
            counter += 10
            break
        elif matriz[b][a] == '0'  and matriz[b+1][a] == '0'  and matriz [b+2][a] == '0':
            print("El ganador es el jugador al cual le corresponden los ceros.")
            counter += 10
            break
        a += 1
    if matriz[0][0] == '0' and matriz[1][1] == '0' and matriz [2][2] == '0':
            print("El ganador es el jugador al cual le corresponden los ceros.")
            counter += 10
            break
    elif matriz[2][0] == '0' and matriz[1][1] == '0' and matriz [0][2] == '0':
            print("El ganador es el jugador al cual le corresponden los ceros.")
            counter += 10
            break

if counter == 9:
    print("No hay más jugadas posibles.\n")
    display()
