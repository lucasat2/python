"""

Implemente uma classe chamada Tempo que representa um período em horas e minutos. A classe deve atender aos seguintes requisitos:

Inicialização:

Permitir a criação de objetos Tempo utilizando dois valores inteiros: um representando as horas e outro os minutos.
Operações matemáticas:

Implementar a soma (+) entre dois objetos Tempo, retornando um novo objeto Tempo que represente a soma das durações.
Implementar a subtração (-) entre dois objetos Tempo, retornando um novo objeto Tempo que represente a diferença das durações. Se o resultado for negativo, a operação deve lançar um erro do tipo ValueError com a mensagem "Tempo não pode ser negativo".
Comparação:

Implementar os operadores de comparação (<, >, <=, >=, ==, !=) entre dois objetos Tempo, com base no total de minutos.
Representação em string:

Implementar o método mágico __str__ para representar o tempo no formato "HH:MM", onde HH e MM são preenchidos com zeros à esquerda, se necessário.
"""

class Tempo:
    def __init__(self, horas: int, minutos: int):
        self.total_minutos = horas * 60 + minutos
    
    def __str__(self):
        horas = self.total_minutos // 60
        minutos = self.total_minutos % 60
        return f"{horas:02}:{minutos:02}"
    
    def __add__(self, outro):
        return Tempo(0, self.total_minutos + outro.total_minutos)
    
    def __sub__(self, outro):
        if self.total_minutos < outro.total_minutos:
            raise ValueError("Tempo não pode ser negativo")
        return Tempo(0, self.total_minutos - outro.total_minutos)
    
    def __lt__(self, outro):
        return self.total_minutos < outro.total_minutos
    
    def __le__(self, outro):
        return self.total_minutos <= outro.total_minutos
    
    def __gt__(self, outro):
        return self.total_minutos > outro.total_minutos
    
    def __ge__(self, outro):
        return self.total_minutos >= outro.total_minutos
    
    def __eq__(self, outro):
        return self.total_minutos == outro.total_minutos
    
    def __ne__(self, outro):
        return self.total_minutos != outro.total_minutos

# Exemplo de uso
t1 = Tempo(2, 30)
t2 = Tempo(1, 45)

print(f"t1 = {t1}")  # Saída esperada: "t1 = 02:30"
print(f"t2 = {t2}")  # Saída esperada: "t2 = 01:45"

t3 = t1 + t2
print(f"t1 + t2 = {t3}")  # Saída esperada: "t1 + t2 = 04:15"

t4 = t1 - t2
print(f"t1 - t2 = {t4}")  # Saída esperada: "t1 - t2 = 00:45"

print(f"t1 < t2: {t1 < t2}")  # Saída esperada: "t1 < t2: False"
print(f"t1 > t2: {t1 > t2}")  # Saída esperada: "t1 > t2: True"

try:
    t5 = t2 - t1
except ValueError as e:
    print(e)  # Saída esperada: "Tempo não pode ser negativo"
