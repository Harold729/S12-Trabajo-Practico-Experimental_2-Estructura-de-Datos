class Cola:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def mostrar_colas(self):
        if not self.is_empty():
            promedio = sum(self.queue) / len(self.queue)
            print("Elementos en la cola (en su orden de salida):", self.queue)
            print("Promedio:", promedio)
        else:
            print("La cola está vacía.")

def ingresar_numeros():
    cola = Cola()
    while True:
        try:
            numero = int(input("Ingrese un número entero (0 para terminar): "))
            if numero == 0:
                break
            cola.enqueue(numero)
        except ValueError:
            print("Por favor, ingrese un número entero.")
    cola.mostrar_colas()

ingresar_numeros()