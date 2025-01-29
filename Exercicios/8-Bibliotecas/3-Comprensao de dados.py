import gzip  # Biblioteca para compressão usando o formato GZIP
import bz2  # Biblioteca para compressão usando o formato BZ2
import lzma  # Biblioteca para compressão usando o formato LZMA
import time  # Biblioteca para medir tempo de execução
from pathlib import Path  # Biblioteca para manipulação de caminhos e arquivos

# Função para comprimir um arquivo usando diferentes métodos
def compress_file(input_file, method):
    with open(input_file, 'rb') as f:  # Abre o arquivo original em modo leitura binária
        data = f.read()  # Lê todo o conteúdo do arquivo

    if method == 'gzip':
        output_file = input_file.with_suffix('.gz')  # Define o nome do arquivo comprimido com extensão .gz
        with gzip.open(output_file, 'wb') as f:  # Abre o arquivo comprimido em modo escrita binária
            f.write(data)  # Escreve os dados comprimidos
    elif method == 'bz2':
        output_file = input_file.with_suffix('.bz2')  # Define o nome do arquivo comprimido com extensão .bz2
        with bz2.open(output_file, 'wb') as f:  # Abre o arquivo comprimido em modo escrita binária
            f.write(data)  # Escreve os dados comprimidos
    elif method == 'lzma':
        output_file = input_file.with_suffix('.xz')  # Define o nome do arquivo comprimido com extensão .xz
        with lzma.open(output_file, 'wb') as f:  # Abre o arquivo comprimido em modo escrita binária
            f.write(data)  # Escreve os dados comprimidos
    else:
        raise ValueError(f"Método de compressão não suportado: {method}")  # Lança um erro se o método for inválido

    return output_file  # Retorna o caminho do arquivo comprimido

# Função para descomprimir um arquivo usando diferentes métodos
def decompress_file(input_file, method):
    if method == 'gzip':
        with gzip.open(input_file, 'rb') as f:  # Abre o arquivo GZIP em modo leitura binária
            data = f.read()  # Lê os dados descomprimidos
    elif method == 'bz2':
        with bz2.open(input_file, 'rb') as f:  # Abre o arquivo BZ2 em modo leitura binária
            data = f.read()  # Lê os dados descomprimidos
    elif method == 'lzma':
        with lzma.open(input_file, 'rb') as f:  # Abre o arquivo LZMA em modo leitura binária
            data = f.read()  # Lê os dados descomprimidos
    else:
        raise ValueError(f"Método de descompressão não suportado: {method}")  # Lança um erro se o método for inválido

    return data  # Retorna os dados descomprimidos

# Função principal para comparar métodos de compressão
def main():
    # Caminho do arquivo a ser testado
    input_file = Path('test_file.txt')  # Define o caminho para o arquivo de teste
    if not input_file.exists():  # Verifica se o arquivo não existe
        input_file.write_text('Exemplo de conteúdo para teste de compressão. ' * 100)  # Cria um arquivo com conteúdo de teste

    methods = ['gzip', 'bz2', 'lzma']  # Lista de métodos de compressão a serem comparados
    results = []  # Lista para armazenar os resultados de cada método

    for method in methods:  # Itera sobre cada método de compressão
        # Medir tempo de compressão
        start_time = time.time()  # Marca o tempo inicial
        compressed_file = compress_file(input_file, method)  # Comprime o arquivo usando o método atual
        compression_time = time.time() - start_time  # Calcula o tempo de compressão

        # Tamanho do arquivo comprimido
        compressed_size = compressed_file.stat().st_size  # Obtém o tamanho do arquivo comprimido

        # Medir tempo de descompressão
        start_time = time.time()  # Marca o tempo inicial
        decompress_file(compressed_file, method)  # Descomprime o arquivo
        decompression_time = time.time() - start_time  # Calcula o tempo de descompressão

        # Tamanho do arquivo original
        original_size = input_file.stat().st_size  # Obtém o tamanho do arquivo original

        # Taxa de compressão
        compression_rate = original_size / compressed_size  # Calcula a taxa de compressão

        # Armazenar resultados
        results.append({  # Adiciona os resultados do método atual à lista
            'method': method,  # Método de compressão utilizado
            'compression_time': compression_time,  # Tempo de compressão
            'decompression_time': decompression_time,  # Tempo de descompressão
            'original_size': original_size,  # Tamanho do arquivo original
            'compressed_size': compressed_size,  # Tamanho do arquivo comprimido
            'compression_rate': compression_rate,  # Taxa de compressão
        })

    # Gerar relatório
    print("\nRelatório Comparativo de Compressão:\n")  # Exibe o cabeçalho do relatório
    for result in results:  # Itera sobre os resultados armazenados
        print(f"Método: {result['method']}")  # Exibe o método de compressão
        print(f"  Tempo de compressão: {result['compression_time']:.6f} segundos")  # Exibe o tempo de compressão
        print(f"  Tempo de descompressão: {result['decompression_time']:.6f} segundos")  # Exibe o tempo de descompressão
        print(f"  Tamanho original: {result['original_size']} bytes")  # Exibe o tamanho do arquivo original
        print(f"  Tamanho comprimido: {result['compressed_size']} bytes")  # Exibe o tamanho do arquivo comprimido
        print(f"  Taxa de compressão: {result['compression_rate']:.2f}\n")  # Exibe a taxa de compressão

if __name__ == "__main__":
    main()  # Chama a função principal para executar o programa
