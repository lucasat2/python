"""
Crie um exemplo de código que imprima o diretório atual (diretório de trabalho, também chamado “working directory”) e, em seguida, faça duas coisas:

Abra um arquivo chamado “dados.txt” localizado em uma subpasta “amostras” do diretório atual usando um caminho relativo, e imprima o conteúdo na tela, depois feche o arquivo.
Faça a mesma coisa, mas abrindo o arquivo usando um caminho absoluto.

"""

import os  # Importa o módulo os para interagir com o sistema operacional

def imprimir_diretorio_e_abrir_arquivo():  
  diretorio_atual = os.getcwd()  # Obtém o diretório de trabalho atual
  print(f"Diretório atual: {diretorio_atual}")  # Imprime o diretório de trabalho atual

#---------------------------------------------------------------------------------------------------------

  # Abrindo o arquivo usando um caminho relativo

  caminho_relativo = os.path.join('amostras', 'dados.txt')  # Cria o caminho relativo para o arquivo 'dados.txt' na subpasta 'amostras'
  print(f"Caminho relativo: {caminho_relativo}")  

  try:
    with open(caminho_relativo, 'r', encoding='utf-8') as arquivo:  # Abrir modo leitura
      conteudo = arquivo.read()  #ler
      print("Conteúdo do arquivo (caminho relativo):")  
      print(conteudo) 

  except FileNotFoundError:
    print(f"O arquivo '{caminho_relativo}' não foi encontrado.") 

  #---------------------------------------------------------------------------------------------------------  

  # Abrindo o arquivo usando um caminho absoluto
  caminho_absoluto = os.path.abspath(caminho_relativo)  # Obtém o caminho absoluto para o arquivo 'dados.txt' na subpasta 'amostras'
  print(f"Caminho absoluto: {caminho_absoluto}") 

  try:
    with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:  # Abrir modo leitura
      conteudo = arquivo.read()  # Ler
      print("Conteúdo do arquivo (caminho absoluto):")  
      print(conteudo)  

  except FileNotFoundError:
    print(f"O arquivo '{caminho_absoluto}' não foi encontrado.")  # Imprime uma mensagem de erro se o arquivo não for encontrado

  #---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
  imprimir_diretorio_e_abrir_arquivo()  # Chama a função imprimir_diretorio_e_abrir_arquivo