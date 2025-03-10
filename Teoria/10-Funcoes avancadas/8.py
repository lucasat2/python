import time
from functools import cache

@cache
def buscar_dados_api(url: str):
    print(f"Buscando dados da API para a URL: {url}")
    time.sleep(2)  # Simula um atraso na requisição
    return f"Dados obtidos de {url}"

# Testando chamadas repetidas com a mesma URL e diferentes URLs
urls = ["https://api.exemplo.com/dados1", "https://api.exemplo.com/dados2", "https://api.exemplo.com/dados1"]

for url in urls:
    print(buscar_dados_api(url))
