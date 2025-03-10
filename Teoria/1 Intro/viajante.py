# Registro de itens coletados ou usados


# Inicialização do diário

# O programa registra itens que um aventureiro coleta ou usa durante suas jornadas. Ele mantém um "diário" (um dicionário Python) que armazena os itens e suas respectivas quantidades. A entrada do usuário permite adicionar ou subtrair itens, e o programa encerra quando "fim" é digitado.

diario = {}

# O dicionário diario é usado para armazenar os itens e suas quantidades.
# Cada chave representa o nome de um item, e o valor associado indica a quantidade do item disponível.

# Entrada do usuário
print("Digite as ações (ex: 'coletar espada', 'usar poção'). Digite 'fim' para encerrar:")

while True:
    entrada = input()
    if entrada.lower() == "fim":
        break
      
# Um loop while é usado para receber entradas continuamente até que o usuário digite "fim".
# A entrada é transformada em letras minúsculas com entrada.lower() para facilitar o tratamento.

    partes = entrada.split()
    if len(partes) != 2:
        print("Entrada inválida. Use o formato 'acao item'.")
        continue
      
# A entrada é dividida em duas partes com split():
# Ação (ex.: "coletar", "usar")
# Nome do item (ex.: "espada", "poção")
# Se a entrada não tiver exatamente duas partes, o programa exibe uma mensagem de erro e continua para a próxima iteração do loop.

    acao, item = partes[0].lower(), partes[1].lower()

    if acao == "coletar":
        diario[item] = diario.get(item, 0) + 1
    elif acao == "usar":
        if item in diario and diario[item] > 0:
            diario[item] -= 1
        else:
            print(f"Você não possui {item} para usar.")
            
            Coletar:

# Se a ação for "coletar", o item é adicionado ao diario.
# O método get(item, 0) retorna a quantidade atual do item no diário ou 0, caso o item ainda não exista.
# Usar:

# Se a ação for "usar", o programa verifica:
# Se o item existe no diário.
# Se sua quantidade é maior que 0.
# Caso essas condições sejam atendidas, a quantidade do item é decrementada. Caso contrário, uma mensagem informa que o item não está disponível.
            
            
    else:
        print("Ação inválida. Use 'coletar' ou 'usar'.")
# Se a ação não for "coletar" ou "usar", o programa exibe uma mensagem de erro.


# Saída
print(f"Diário final: {diario}")
