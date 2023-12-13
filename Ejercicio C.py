
def replace_number_with_asterisk(numbers, n):
    for i in range(len(numbers)):
        if numbers[i] == n:
            numbers[i] = "*"
    return numbers


def numbers_list():
    while True:
        result = []
        cont = 0
        fix_list = str(input("Ingresar una lista de números:\n>> "))
        result_list = fix_list.strip("[]").split(",")
        for i in result_list:
            if i.startswith(" "):
                i = i.lstrip()
            for j in i:
                if j.isalpha() or j.isspace():
                    cont += 1
        if cont > 0:
            print("Ingrese un arreglo valido siguiento esta estructura: [ 1, 2, 3, 4, 5]")
        else:
            for elemento in result_list:
                entero = int(elemento)
                result.append(entero)
            break
    return result


def validate_num():
    while True:
        try:
            values = int(input("Ingresar un número entero:\n>> "))
            break
        except ValueError:
            print("Ingrese un número válido")
    return values



# lista de prueba = [1, 2, 3, 4, 5, 3, 6, 7, 3]
# numero de prueba = 3

def main():
    numbers = numbers_list()
    n = validate_num()
    modified_numbers = replace_number_with_asterisk(numbers, n)
    print(modified_numbers)


if __name__ == "__main__":
    main()
