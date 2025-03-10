def valida_cnpj(cnpj: str) -> bool:
    """
    Valida os dígitos verificadores de um CNPJ.

    Args:
        cnpj (str): O CNPJ a ser validado. Deve ser uma string de 14 dígitos numéricos.

    Returns:
        bool: True se o CNPJ for válido, False caso contrário.
    """
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False

  

    # Pesos para os cálculos dos dígitos verificadores
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


    def calcula_digito(cnpj, pesos):
      soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
      resto = soma % 11
      return 0 if resto < 2 else 11 - resto

    # Calcula e verifica o primeiro dígito verificador
    digito1 = calcula_digito(cnpj, peso1)
    if digito1 != int(cnpj[12]):
        return False

    # Calcula e verifica o segundo dígito verificador
    digito2 = calcula_digito(cnpj, peso2)
    if digito2 != int(cnpj[13]):
        return False

    return True

# Exemplos de uso
print(valida_cnpj("11222333000181"))  # True
print(valida_cnpj("11222333000182"))  # False