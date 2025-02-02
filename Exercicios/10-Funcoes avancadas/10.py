import csv
from collections import defaultdict

def processar_transacoes(nome_arquivo):
    totais_por_dia = defaultdict(float)
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if len(linha) < 3:
                continue  # Ignorar linhas inválidas
            
            data, _, valor, *_ = linha  # Extraindo data e valor
            
            try:
                totais_por_dia[data] += float(valor)
            except ValueError:
                continue  # Ignorar linhas com valores inválidos
    
    return dict(totais_por_dia)  # Retorna o dicionário final