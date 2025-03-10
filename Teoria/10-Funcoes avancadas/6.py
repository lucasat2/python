#  Você tem uma lista de dicionários, onde cada dicionário representa um aluno com as chaves “nome” e “notas” (uma lista de notas). Escreva uma função obter_melhor_aluno(alunos, criterio) que recebe a lista de alunos e uma função criterio como argumentos. A função criterio deve receber um dicionário de aluno e retornar um valor numérico pelo qual os alunos serão comparados. Use a função max() com o parâmetro key para encontrar o aluno com o maior valor retornado pela função criterio. Teste sua função com duas funções de critério diferentes: uma que retorna a média das notas do aluno e outra que retorna a maior nota do aluno.


alunos = [
  {"nome": "Lucas", "notas": [8.5, 7.0, 9.0]},
  {"nome": "Maria", "notas": [6.5, 8.0, 7.5]},
  {"nome": "João", "notas": [9.0, 8.5, 8.0]},
  {"nome": "Ana", "notas": [7.0, 6.5, 7.5]},
  {"nome": "Pedro", "notas": [8.0, 7.5, 8.5]}
]

def calcular_media(notas):
    return sum(notas) / len(notas)

def criterio(aluno):
    return calcular_media(aluno["notas"])

def obter_melhor_aluno(alunos, criterio):
    return max(alunos, key=criterio)

melhor_aluno = obter_melhor_aluno(alunos, criterio)

print("Melhor aluno:", melhor_aluno["nome"])
print("Maior nota:", (melhor_aluno["notas"]))
print("Média das notas:", calcular_media(melhor_aluno["notas"]))
