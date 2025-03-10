# Implemente uma função atualizar_cadastro que recebe um nome (str) e uma idade. Se a idade não for fornecida, retorne apenas o nome. Se a idade for fornecida, retorne o nome a idade numa string. Use anotações de tipo apropriadas.

from typing import Optional

def atualizar_cadastro(nome: str, idade:int|None = None) -> str:

    if idade is not None:
        return f"Nome: {nome}, Idade: {idade} anos"
    return f"Nome: {nome}"
    


print(atualizar_cadastro("Joao")) 
print(atualizar_cadastro("Maria", 25))