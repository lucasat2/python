# Requisições HTTP

# Desenvolva um programa que faça uma requisição GET para uma API pública da sua escolha (usando a biblioteca requests), converta o resultado de JSON para dicionário/lista e imprima as informações.

import requests  # Importa a biblioteca requests para fazer requisições HTTP
import json  # Importa a biblioteca json para manipulação de dados JSON

def get_post(post_id):  # Define a função que recebe um ID de post como argumento
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # Monta a URL da API com o ID do post
    response = requests.get(url)  # Faz a requisição GET para a API
    
    if response.status_code == 200:  # Verifica se a resposta da API foi bem-sucedida
        data = response.json()  # Converte o JSON retornado para um dicionário Python
        print(json.dumps(data, indent=4, ensure_ascii=False))  # Exibe os dados formatados na saída
    else:
        print(f"Erro: {response.status_code}")  # Exibe uma mensagem de erro caso a requisição falhe

# Testando a função
get_post(5)  # Chama a função para obter e exibir os dados do post com ID 1