# Implemente uma função definir_prioridade_tarefa que aceita os valores literais “alta”, “media” ou “baixa” para definir a prioridade de uma tarefa.

# A função deve retornar uma mensagem personalizada baseada na prioridade da tarefa, e incluir uma recomendação de prazo (em dias) com base na prioridade escolhida.


def definir_prioridade_tarefa(prioridade:str) -> str:
   
    if prioridade == "alta":
        return "Prioridade: Alta. Conclua em até 1 dia."
    elif prioridade == "media":
        return "Prioridade: Média.  Conclua a tarefa em até 3 dias."
    elif prioridade == "baixa":
        return "Prioridade: Baixa. Concluaa tarefa em até 7 dias."
    else:
        return "Prioridade inválida. Por favor, escolha entre 'alta', 'media' ou 'baixa'."


print(definir_prioridade_tarefa("alta"))   # Prioridade: Alta. Conclua em até 1 dia a tarefa.
print(definir_prioridade_tarefa("media"))  # Prioridade: Média. Conclua a tarefa em até 3 dias.
print(definir_prioridade_tarefa("baixa"))  # Prioridade: Baixa. Conclua a tarefa em até 7 dias.
print(definir_prioridade_tarefa("urgente")) # Prioridade inválida.
