import math

class CalculadoraRaizCuadrada:
    def __init__(self, numero):
        self.numero = numero

    def calcular_raiz(self):
        """Calcula la raíz cuadrada del número."""
        if self.numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.numero)

    def mostrar_resultado(self):
        """Muestra el resultado de la raíz cuadrada."""
        try:
            raiz = self.calcular_raiz()
            print(f"La raíz cuadrada de {self.numero} es {raiz:.4f}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    try:
        numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        calculadora = CalculadoraRaizCuadrada(numero)
        calculadora.mostrar_resultado()
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
