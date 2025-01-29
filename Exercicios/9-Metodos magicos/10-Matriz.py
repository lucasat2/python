class Matriz:
    def __init__(self, linhas, colunas):
        self._linhas = linhas
        self._colunas = colunas
        self._dados = [[0] * colunas for _ in range(linhas)]
    
    def __getitem__(self, indices):
        i, j = indices
        if not (0 <= i < self._linhas and 0 <= j < self._colunas):
            raise IndexError("Índice fora dos limites")
        return self._dados[i][j]
    
    def __setitem__(self, indices, valor):
        i, j = indices
        if not (0 <= i < self._linhas and 0 <= j < self._colunas):
            raise IndexError("Índice fora dos limites")
        self._dados[i][j] = valor
    
    def __str__(self):
        return '\n'.join('  '.join(str(valor) for valor in linha) for linha in self._dados)

# Exemplo de uso
def main():
    matriz = Matriz(3, 3)
    matriz[0, 0] = 1
    matriz[1, 1] = 2
    matriz[2, 2] = 3
    print("Matriz:")
    print(matriz)
    print(f"Elemento na posição (1, 1): {matriz[1, 1]}")
    print(f"Elemento na posição (0, 2): {matriz[0, 2]}")
    matriz[0, 2] = 4
    print("Matriz atualizada:")
    print(matriz)
    matriz[0, 0] = 0
    print("Matriz após alteração de um elemento:")
    print(matriz)
    try:
        matriz[3, 3] = 5
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()
