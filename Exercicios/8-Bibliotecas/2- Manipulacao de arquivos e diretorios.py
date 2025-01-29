from pathlib import Path  # Importa a biblioteca pathlib para manipulação de caminhos e arquivos
import shutil  # Importa a biblioteca shutil para operações de cópia de arquivos

def main():
    # Diretório atual
    diretorio_atual = Path.cwd()  # Obtém o diretório atual de trabalho

    # Listar todos os arquivos no diretório atual
    print("Arquivos no diretório atual:")  # Exibe uma mensagem inicial
    for arquivo in diretorio_atual.iterdir():  # Itera sobre todos os itens no diretório atual
        print(arquivo)  # Imprime o nome de cada item

    # Criar a pasta "backup" (se não existir)
    pasta_backup = diretorio_atual / "backup"  # Define o caminho para a pasta "backup"
    pasta_backup.mkdir(exist_ok=True)  # Cria a pasta "backup" se ela ainda não existir

    # Copiar todos os arquivos .py para a pasta "backup"
    arquivos_copiados = []  # Lista para armazenar os arquivos copiados
  
    for arquivo_py in diretorio_atual.glob("*.py"):  # Busca todos os arquivos com extensão .py no diretório atual
        destino = pasta_backup / arquivo_py.name  # Define o destino do arquivo na pasta "backup"
        shutil.copy(arquivo_py, destino)  # Copia o arquivo .py para o destino
        arquivos_copiados.append(destino)  # Adiciona o arquivo copiado à lista

    # Imprimir o caminho absoluto de cada arquivo copiado
    print("\nArquivos copiados para a pasta 'backup':")  # Exibe uma mensagem inicial
  
    for arquivo in arquivos_copiados:  # Itera sobre a lista de arquivos copiados
        print(arquivo.resolve())  # Imprime o caminho absoluto de cada arquivo

if __name__ == "__main__":
    main()  # Chama a função principal para executar o programa
