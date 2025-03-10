frase = input("Digite uma frase: ")


numero_caracteres = len(frase)


palavra = input("Digite uma palavra para verificar se está na frase: ")
estah_na_frase = palavra in frase

#        SINTAXE INICIO: FIM 
primeiros_tres = frase[6:-3]
ultimos_tres = frase[-3:]


print(f"Você digitou uma frase com {numero_caracteres} caracteres.")
print(f"A palavra '{palavra}' está na frase? {estah_na_frase}")
print(f"Os três primeiros caracteres da frase são: {primeiros_tres}")
print(f"Os três últimos caracteres da frase são: {ultimos_tres}")
print(f"Olá, sua frase foi: {frase}")
