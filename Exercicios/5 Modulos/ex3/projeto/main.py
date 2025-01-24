from saudacoes.formal import cumprimentar as cumprimentar_formal
from saudacoes.informal import cumprimentar as cumprimentar_informal

nome = input("Digite seu nome: ").strip()

print("Saudação formal:")
cumprimentar_formal(nome)

print("Saudação informal:")
cumprimentar_informal(nome)
