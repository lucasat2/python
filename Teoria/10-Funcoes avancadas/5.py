# Escreva uma função de alta ordem chamada aplicar_operacao(numeros, operacao) que recebe uma lista de números e uma função operacao como argumentos. A função aplicar_operacao deve aplicar a função operacao a cada número na lista e retornar uma nova lista com os resultados. Em seguida, crie duas funções, dobrar(x) que retorna o dobro de x, e triplicar(x) que retorna o triplo de x. Utilize a função aplicar_operacao para dobrar todos os números em uma lista e, em seguida, triplicar todos os números em outra lista.


def aplicar_operacao(numeros,operacao):
  resultado = [operacao(numero) for numero in numeros]
  return resultado  

def dobrar(x):
  return x * 2

def triplicar(x):
  return x * 3

lista = [10,20,30,40,50,60]

dobrados = aplicar_operacao(lista,dobrar)

triplicados = aplicar_operacao(lista,triplicar)

print(f'Dobrados: {dobrados}')
print(f'triplicados: {triplicados}')