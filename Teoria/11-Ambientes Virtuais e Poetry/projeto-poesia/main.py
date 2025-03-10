import requests

response = requests.get("https://potterapi-fedeperin.vercel.app/pt/books")
books = response.json()

for book in books:
    print(book["title"])