# Crie uma função chamada analisar_numero que recebe um número e retorna três valores: se é par ou ímpar, se é positivo ou negativo, e se é inteiro ou decimal.


def analisar_numero(numero):
   
    if numero % 2 == 0:
        par_ou_impar = "par"
    else:
        par_ou_impar = "ímpar"
    
 
    if numero > 0:
        positivo_ou_negativo = "positivo"
    elif numero < 0:
        positivo_ou_negativo = "negativo"
    else:
        positivo_ou_negativo = "neutro"
    
   
    if isinstance(numero, int): #se numero for um numero inteiro
        inteiro_ou_decimal = "inteiro"
    else:
        inteiro_ou_decimal = "decimal"
    
    return par_ou_impar, positivo_ou_negativo, inteiro_ou_decimal


resultado = analisar_numero(3.5)
print(resultado)  