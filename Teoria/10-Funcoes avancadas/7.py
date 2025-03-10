def gerar_primos(maximo):

    def eh_primo(n):
        if n < 2:
            return False
            
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, maximo + 1):
        if eh_primo(num):
            yield num

# Gerando os primeiros 5 números primos
maximo = 100  # Definindo um limite alto para garantir que temos pelo menos 5 primos
gerador = gerar_primos(maximo)

for _ in range(5):
    print(next(gerador))
