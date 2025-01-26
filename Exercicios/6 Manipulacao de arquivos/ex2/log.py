"""
Escreva um código que crie um arquivo chamado “log.txt” e adicione a linha “Nova entrada de log” ao final do arquivo, sem apagar o conteúdo existente.

Ou seja, toda vez que o programa for executado, o arquivo “log.txt” deve ser atualizado com uma linha a mais de texto.

Na primeira vez que o programa é executado, o arquivo “log.txt” deve ser criado se não existir.
"""

def append_log_entry():  
  with open("log.txt", "a") as log_file:  # Abre o arquivo 'log.txt' no modo de adição (append)
    log_file.write("Queijo quente\n")  # Escreve uma nova linha de log no arquivo

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
  append_log_entry()  