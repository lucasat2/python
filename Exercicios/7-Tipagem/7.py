# Crie uma classe ListaTarefas com um atributo lista de strings e métodos para adicionar e remover tarefas. Use anotações de tipo em todos os atributos e métodos.

from typing import List

class ListaTarefas:
    def __init__(self) -> None:
        self.lista: List[str] = []
        
#-------------------Métodos-------------------
    def adicionar_tarefa(self, tarefa: str) -> None:
        self.lista.append(tarefa)
#---------------------------------------------

    def remover_tarefa(self, tarefa: str) -> bool:
        if tarefa in self.lista:
            self.lista.remove(tarefa)
            return True
        return False
#---------------------------------------------

    def listar_tarefas(self) -> List[str]:
    
        return self.lista

#---------------------------------------------

if __name__ == "__main__":
    minha_lista = ListaTarefas() # Instanciando a classe ListaTarefas
    minha_lista.adicionar_tarefa("Estudar Python")# Adicionando tarefas
    minha_lista.adicionar_tarefa("Fazer compras") # Adicionando tarefas
    print("Tarefas:", minha_lista.listar_tarefas()) # Listando tarefas

    minha_lista.remover_tarefa("Estudar Python") # Removendo tarefas
    print("Tarefas após remoção:", minha_lista.listar_tarefas()) # Listando tarefas após remoção
