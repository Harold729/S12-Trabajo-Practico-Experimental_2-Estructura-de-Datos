
def create_matrix(n):
    # Crea una matriz de tamaño n x n
    matrix = [[i for i in range(j*n, (j+1)*n)] for j in range(n)]
    return matrix


def print_matrix(matrix):
    # Imprime la matriz en un formato legible
    for row in matrix:
        print("  [", end="")
        print(", ".join("{:3}".format(element) for element in row), end="")
        print("]")


def validate_num():
    # Valida que el usuario ingrese un número entero válido
    while True:
        try:
            values = int(input("Ingresar un número entero:\n>> "))
            break
        except ValueError:
            print("Ingrese un número válido")
    return values


def main():
    # Función principal del programa
    n = validate_num()
    matrix = create_matrix(n)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
