
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print("Dicionário original:", pessoa)


pessoa["profissao"] = "Engenheiro"


if "idade" in pessoa:
    print("Idade:", pessoa["idade"])


del pessoa["cidade"]

print("Dicionário alterado:", pessoa)
