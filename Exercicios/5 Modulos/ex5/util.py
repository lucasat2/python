def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, pesos):
        soma = sum(int(cpf[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(cpf, [10, 9, 8, 7, 6, 5, 4, 3, 2])
    if int(cpf[9]) != primeiro_digito:
        return False

    segundo_digito = calcular_digito(cpf, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2])
    if int(cpf[10]) != segundo_digito:
        return False

    return True

def obter_input_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número positivo.")