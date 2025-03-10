# Contagem progressiva
print("Números de 1 a 10:")
for numero in range(1, 11):
    print(numero)

# Contagem regressiva
print("Números de 10 a 1:")
for numero in range(10, 0, -1):
    print(numero)


# Array
nomes = ["Alice", "Bruno", "Carla", "Daniel", "Elisa"]

print("Nomes e seus índices:")
for indice in range(len(nomes)):
    print(f"{indice}:{nomes[indice]}")