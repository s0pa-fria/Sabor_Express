class Forma:
    def calcular_area(self):
        pass  # Isso significa que não faz nada ainda

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Agora vamos criar um círculo e um retângulo
meu_circulo = Circulo(5)
meu_retangulo = Retangulo(4, 6)

# Vamos usar o polimorfismo para calcular a área de cada forma
formas = [meu_circulo, meu_retangulo]

for forma in formas:
    print(f"A área do é: {forma.calcular_area()}")