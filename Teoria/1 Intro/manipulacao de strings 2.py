nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e: {nome[::-1]}')

    if ' ' in nome:
        print("Seu nome contem espacos")
    else:
        print("Seu nome nao contem espacos")  
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A última letra do seu nome e {nome[-1]}')
else:
    print("Desculpe, voce deixou campos vazios")