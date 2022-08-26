from time import time

class complejidad:
    def sumar(self, n):
        suma = 0
        for x in range(1, n + 1):
            suma += x
        return suma

    def sumaGauss(self, n):
        suma = (n * (n + 1)) / 2
        return suma

if __name__ == "__main__":
    programa = complejidad()
    programa.sumar(1000000000)
    programa.sumaGauss(1000000000)