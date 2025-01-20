
alfabeto = 'abcdefghijklmnopqrstuvwyxz'
usuario = input("Digite uma frase")
letras_encontradas = set()

for caractere in frase_usuario.lower():
    letras_encontradas.add(caractere)


pangrama = True
for letra in alfabeto:
    if letra not in letras_encontradas:
        pangrama = False
        break

if pangrama:
    print("A frase é um pangrama!")
else:
    print("A frase NÃO é um pangrama.")
