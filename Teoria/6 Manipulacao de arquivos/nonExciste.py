# Escreva um programa que tente abrir um arquivo chamado “arquivo_que_nao_existe.txt” para leitura. Use um bloco try-except para capturar a exceção FileNotFoundError e imprimir uma mensagem amigável ao usuário informando que o arquivo não foi encontrado.

import os  # Importa o módulo os para interagir com o sistema operacional


try:
  with open('arquivo_que_nao_existe.txt', 'r', encoding='utf-8') as arquivo:  # Abrir modo leitura
    conteudo = arquivo.read()  # Ler


except FileNotFoundError:
  print("O arquivo 'arquivo_que_nao_existe.txt' não foi encontrado.")  # Imprime uma mensagem de erro se o arquivo não for encontrado


if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
  pass  # Não faz nada






