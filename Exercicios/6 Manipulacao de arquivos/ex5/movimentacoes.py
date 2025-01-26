import os
import shutil

def mover_arquivo():
    # Solicita ao usuário os caminhos dos arquivos A e B
    caminho_a = input("Insira o caminho do arquivo A: ")
    caminho_b = input("Insira o caminho do arquivo B: ")

    # Verifica se o arquivo A existe
    if not os.path.isfile(caminho_a):
        print(f"Erro: O arquivo '{caminho_a}' não existe.")
        return

    # Verifica se o caminho B já existe
    if os.path.exists(caminho_b):
        print(f"Erro: O caminho '{caminho_b}' já existe.")
        return

    # Tenta mover o arquivo A para o caminho B
    try:
        shutil.move(caminho_a, caminho_b)
        print(f"Arquivo '{caminho_a}' movido com sucesso para '{caminho_b}'.")
    except Exception as e:
        print(f"Erro ao mover o arquivo: {e}")

# Executa a função
if __name__ == "__main__":
    mover_arquivo()