"""
Desafio !

Você foi contratado para desenvolver um sistema de registro e análise de dados para um censo demográfico de animais de estimação em um bairro. Os dados coletados incluem o nome do animal, a espécie (cachorro, gato, pássaro, etc.) e a idade em anos. Sua tarefa é criar um programa Python que faça o seguinte:

Coleta de Dados:

Permita que o usuário insira os dados de vários animais de estimação.
A entrada deve continuar até que o usuário digite “fim” no nome do animal.
Os dados de cada animal devem ser armazenados em um dicionário com as chaves nome, especie e idade.
Todos os dicionários devem ser armazenados em uma lista.
Análise de Dados:

Crie um trecho do programa para analisar os dados que usa a lista de dicionários como dados de entrada.
Calcule:
A quantidade total de animais registrados.
A quantidade de animais por espécie (ex: “cachorro”: 5, “gato”: 3 etc.) armazenando em um dicionário.
A idade média dos animais de cada espécie, também usando outro dicionário.
Todas as respostas devem estar organizadas em dicionários contendo:
A chave total com o número total de animais.
A chave especies com um dicionário onde cada chave é uma espécie e o valor é a contagem de animais daquela espécie.
A chave idades_medias com um dicionário onde cada chave é uma espécie e o valor é a idade média dos animais daquela espécie.
Exibição dos Resultados:

Após a coleta e análise dos dados, o programa deve exibir os resultados no seguinte formato: 
Total de animais: [número total]

Contagem por espécie:         

[especie 1]: [número]         

[especie 2]: [número]         

...     

Idade média por espécie:         

[especie 1]: [idade média]         

[especie 2]: [idade média]    


"""

animais = []

# Coleta de Dados
while True:
    nome = input("Digite o nome do animal (ou 'fim' para terminar): ")
    if nome.lower() == 'fim':
        break
    especie = input("Digite a espécie do animal: ")
    idade = int(input("Digite a idade do animal: "))
    animais.append({"nome": nome, "especie": especie, "idade": idade})

# Análise de Dados
total_animais = len(animais)
contagem_especies = {}
idades_especies = {}

for animal in animais:
    especie = animal["especie"]
    idade = animal["idade"]
    
    if especie in contagem_especies:
        contagem_especies[especie] += 1
        idades_especies[especie].append(idade)
    else:
        contagem_especies[especie] = 1
        idades_especies[especie] = [idade]

idades_medias = {especie: sum(idades) / len(idades) for especie, idades in idades_especies.items()}

# Exibição dos Resultados
print(f"\nTotal de animais: {total_animais}\n")

print("Contagem por espécie:")
for especie, contagem in contagem_especies.items():
    print(f"{especie}: {contagem}")

print("\nIdade média por espécie:")
for especie, idade_media in idades_medias.items():
    print(f"{especie}: {idade_media:.2f}")
