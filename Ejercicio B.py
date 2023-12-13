#Suma de matrices y su comparacion

while True:
    try:
        f = int(input("Numero de fila: "))
        if f > 1:
            print("Siguiente")
        else:
            print("Debe ser mas de uno fila ")
            continue
        break
    except ValueError:
        print("Debes escribir un numero")

while True:
    try:
        c = int(input("Numero de columna: "))
        if c > 1:
            print("Siguiente")
        else:
            print("Debe ser mas de uno columna ")
            continue
        break
    except ValueError:
        print("Debes escribir un numero")
matriz = []
for row_position in range(f):
    row = []
    for element in range(c):
        while True:
            try:
                 row.append(int(input(f"La fila {row_position} y columna {element}: ")))
                 break
            except ValueError:
                 print("Debes escribir un numero")
                 continue
    matriz.append(row)
for row in matriz:
    print(row)
suma_matriz = []
for i in range(len(matriz[0])):
    suma_columna = 0
    for j in range(len(matriz)):
        suma_columna += matriz[j][i]
    suma_matriz.append(suma_columna)
print("Su suma de las columna son:",suma_matriz)

print("La suma de las columna son iguales: ", len(list(set(suma_matriz)))==1)






