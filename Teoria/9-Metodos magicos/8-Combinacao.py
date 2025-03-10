class Colecao:
    def __init__(self):
        self._itens = []
        
    def adicionar_item(self, item):
        self._itens.append(item)
    
    def __len__(self):
        return len(self._itens)
    
    def __getitem__(self, index):
        return self._itens[index]
    
    def __contains__(self, item):
        return item in self._itens
    
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index >= len(self._itens):
            raise StopIteration
        item = self._itens[self._index]
        self._index += 1
        return item

# Exemplo de uso
colecao = Colecao()
colecao.adicionar_item("Item 1")
colecao.adicionar_item("Item 2")

print(f"Tamanho da coleção: {len(colecao)}")  # Saída esperada: 2
print(f"Item 1 está na coleção? {'Item 1' in colecao}")  # Saída esperada: True

for item in colecao:
    print(item)
