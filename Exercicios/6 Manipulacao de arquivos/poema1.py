# Programa 1: Leitura e impressão do conteúdo de "poema.txt"

def ler_e_imprimir_arquivo():  

  try:  # Tenta executar o bloco de código abaixo
    
    with open('poema.txt', 'r', encoding='utf-8') as arquivo:  # Abre o arquivo 'poema.txt' no modo de leitura com codificação UTF-8

      conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo e armazena na variável 'conteudo'
      print(conteudo)  # Imprime o conteúdo do arquivo

  except FileNotFoundError:  # Se o arquivo não for encontrado, executa o bloco abaixo
    print("O arquivo 'poema.txt' não foi encontrado.")  

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
  ler_e_imprimir_arquivo()  

  