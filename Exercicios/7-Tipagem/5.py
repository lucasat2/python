from typing import Tuple

def para_string(ponto: Tuple[int, int]) -> Tuple[str, str]:  #Tupla com 2 numeros inteiros e retorna 2 strings
    return (str(ponto[0]), str(ponto[1]))  #funcao str converte para string


resultado = para_string((10, 20))
print(resultado)  
