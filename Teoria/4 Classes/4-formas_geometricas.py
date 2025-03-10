import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def soma_areas(formas):
    soma = 0
    for forma in formas:
        soma += forma.calcular_area()
    return soma


formas = [
    Retangulo(10, 5),
    Circulo(7),
    Triangulo(6, 8)
]

print(f"Soma das áreas: {soma_areas(formas)}")