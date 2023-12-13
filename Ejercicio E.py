"""Crear un programa para ingresar caracteres a una pila, se ingresarán los
caracteres hasta que el valor que se ingrese sea *, en ese momento debe
presentar los elementos que se han ingresado a la pila (en su orden de
salida) y su correspondiente valor en código ASCII."""
class Nodo:  # Creamos la clase nodo
    def __init__(self, dato=None, sig=None):
        self.dato = dato
        self.sig = sig
class Pila:  # Creamos la estrutura de datos pila con sus metodos
    def __init__(self):  # creamos la estrcutura
        self.cabecera = None

    def es_vacio(self):  # Retorna verdadero se esta vacia la pila
        return self.cabecera is None

    def apilar(self, dato):  # Método para agregar elementos al final de la Pila
        if not self.cabecera:
            self.cabecera = Nodo(dato=dato)
            return
        actual = self.cabecera
        while actual.sig:
            actual = actual.sig
        actual.sig = Nodo(dato=dato)

    def desapilar(self):  # Método para sacar el nodo de la pila retorna el dato que habia
        if not self.es_vacio():
            actual = self.cabecera
            prev = None
            while actual.sig is not None:
                prev = actual
                actual = actual.sig
            if prev is None:
                prev = actual
                self.cabecera = actual.sig
                return prev.dato
            elif actual:
                prev.sig = actual.sig
                return actual.dato
        else:
            return None

# imprime un pila horinzontal con formato ej: a => b => c
    def imprimir_pila(self):
        nodo = self.cabecera
        if not self.es_vacio():
            while nodo is not None:
                if nodo.sig is not None:
                    print(nodo.dato, end="  =>  ")
                else:
                    print(nodo.dato)
                nodo = nodo.sig
        else:
            print("Pila Vacia")
# Funcion que retorna el valor en ascii de cualquier carater
def convertir_car_ascii(caracter):
    return ord(caracter)
# Funcion que valida que sea solo un caracter , aun el espacio es contado como caracter
def validar_caracter(promt):
    while True:
        caracter = input(promt)
        if len(caracter) == 1:
            if 46 < convertir_car_ascii(caracter) < 58:
                print("Ha ingresado un numero, Ingresar de Nuevo")
            else:
                if convertir_car_ascii(caracter) == 32 or convertir_car_ascii(caracter) == 9:
                    print("Ha ingresado espacio o tab se lo considera como caracter")
                return caracter
        elif len(caracter) > 1:
            print("Ha ingresado mas de un caracter")
        else:
            print("No ha ingresado caracter")

# procedimento que imprime la pila vaciando la pila o desapialndola

def ingresardatos_pila(p):
    print("\t\t***** Ingreso de caracteres *****"
          "\n\t\t - Se termina cuando ingrese  * -")
    i = 1  # contador de caracteres
    while True:  # bucle que controla la salida hasta que sea caracter
        c = validar_caracter(f"Ingrese caracter #{i}: ")  # valida que solo sea caracter
        if c == "*":  # si el usuario llega a ingresar * sale del buque
            break
        p.apilar(c)  # apila los caracteres
        i += 1
def imprimir_desapilando(p):
    if p.es_vacio():
        print("Pila Vacia")
    else:
        while True:
            dato = p.desapilar()
            if dato is not None:
                print(f"{dato} su codigo ASCII es :{convertir_car_ascii(dato)}")
            else:
                break
def presentardatos_pila(p):
    print("\t\t***** Presentacion de datos ingresados a la Pila *****"
          "\nOrden como se ingreso a la Pila")
    p.imprimir_pila()
    print("Orden de salida con su codigo ascii")
    imprimir_desapilando(p)

if __name__ == '__main__':
    s = Pila()
    ingresardatos_pila(s)
    if not s.es_vacio():
        presentardatos_pila(s)
    else:
        print("***** No hay datos ingresados, Pila Vacia *****")
