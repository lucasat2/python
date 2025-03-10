import requests
from bs4 import BeautifulSoup

# Função para buscar o conteúdo de uma página e extrair os links
def buscar_links(url):
    # Enviar uma solicitação GET para a URL
    resposta = requests.get(url)
    
    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if resposta.status_code == 200:
        # Analisar o conteúdo da página usando o BeautifulSoup
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        
        # Encontrar todas as tags 'a' (tags de ancoragem que contêm links)
        links = sopa.find_all('a')
        
        # Extrair e exibir o atributo 'href' de cada tag 'a'
        for link in links:
            href = link.get('href')
            if href:
                print(href)
    else:
        print(f"Falha ao recuperar a página. Código de status: {resposta.status_code}")

# Definindo um site de exemplo
url = "https://www.wikipedia.org/"

# Chamar a função para buscar e exibir os links
buscar_links(url)
