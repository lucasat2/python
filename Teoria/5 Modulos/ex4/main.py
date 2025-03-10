from saudacoes.geral import saudar

nome = input("Digite seu nome: ").strip()
tipo = input("Digite o tipo de saudação ('formal' ou 'informal'): ").strip().lower()

try:
    saudar(nome, tipo)
except ValueError as e:
    print(e)