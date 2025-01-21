def calcular_fatorial(numero):
    """
    Retorna:
        int: Fatorial do número fornecido.
    """

    if numero < 0:
        return 
    
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial*= i 
    return fatorial

# Testando a função com alguns valores
valores_de_teste = [0, 1, 5, 7, -3]

for valor in valores_de_teste:
    print(f"Fatorial de {valor}: {calcular_fatorial(valor)}")