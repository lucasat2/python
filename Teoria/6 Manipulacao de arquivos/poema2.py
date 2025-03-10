# Programa 2: Ler o arquivo "poema.txt" linha a linha e imprimir o conteúdo na tela

def ler_poema():
  try:

    with open("poema.txt", "r", encoding="utf-8") as arquivo:

      for linha in arquivo:
        print(linha)

  except FileNotFoundError:
    print("O arquivo 'poema.txt' não foi encontrado.")

if __name__ == "__main__":
  ler_poema()