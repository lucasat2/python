# Você tem uma lista de caminhos de arquivos. Utilize a função filter() com uma função lambda para obter apenas os caminhos que correspondem a arquivos com extensão “.txt”.

caminhos = [ 'arquivo1.txt', 'arquivo2.txt', 'arquivo3.jpg', 'arquivo4.txt', 'arquivo5.jpg','arquivo9.png','arquivo10.svg','arquivo11.rar']

arquivos_txt = list(filter(lambda caminho: caminho.endswith('.txt'), caminhos))

print(arquivos_txt)