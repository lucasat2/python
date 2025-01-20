
frase_usuario = input("Digite uma frase: ")


contagens = {
    'vogais': 0,
    'consoantes': 0,
    'espacos': 0,
    'pontuacoes': 0
}


vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
pontuacoes = ".,!?-"


for caractere in frase_usuario.lower():
    if caractere in vogais:
        contagens['vogais'] += 1
    elif caractere in consoantes:
        contagens['consoantes'] += 1
    elif caractere == " ":
        contagens['espacos'] += 1
    elif caractere in pontuacoes:
        contagens['pontuacoes'] += 1


total_caracteres = sum(contagens.values())

# porcentagens
porcentagem_vogais = (contagens['vogais'] / total_caracteres) * 100 
porcentagem_consoantes = (contagens['consoantes'] / total_caracteres) * 100 
porcentagem_espacos = (contagens['espacos'] / total_caracteres) * 100 
porcentagem_pontuacoes = (contagens['pontuacoes'] / total_caracteres) *100


#resultados
print(f"Vogais: {porcentagem_vogais:.2f}%")
print(f"Consoantes: {porcentagem_consoantes:.2f}%")
print(f"Espacos: {porcentagem_espacos:.2f}%")
print(f"Pontuacoes: {porcentagem_pontuacoes:.2f}%")

"""
Faça um programa que lê uma string e conta o número de vogais, consoantes, espaços e pontuações (caracteres “.”,“,”,“!”,“?”,"-").

Observação: é proibido o uso de funções auxiliares, como o  count(), por exemplo.

A saída do programa deve ser a porcentagem de cada tipo de caractere na string, com 2 casas após a vírgula.

Exemplo:
Entrada:
Mesmo que a realidade seja um pesadelo, nao podemos deixar de sonhar.
Saída:
Vogais: 40.58%
Consoantes: 40.58%
Espacos: 15.94%
Pontuacoes: 2.90%

Sugestão: use um Dict para armazenar a contagem de cada caractere. Depois itere pelas vogais “aeiou” para somar, depois pelas consoantes “bcdf….z”, etc.
    """