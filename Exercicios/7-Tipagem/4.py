from typing import Union

def processar_dados(valor: Union[int, str]) -> Union[int, str]:
    if isinstance(valor, int):
        return valor * 2
    elif isinstance(valor, str):
        return valor.upper()
    else:
        raise ValueError("O valor deve ser um inteiro ou uma string.")

# Exemplos de uso:
print(processar_dados(10))    # Saída: 20
print(processar_dados("texto"))  # Saída: "TEXTO"
