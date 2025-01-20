convidados = {"Ana", "Bruno", "Carla"}
print(convidados)  # A ordem pode variar, mas o conteúdo é o mesmo


nomes_repetidos = ["Ana", "Ana", "Carla"]
convidados = set(nomes_repetidos)
print(convidados)  # {"Ana", "Carla"}


convidados.add("Daniel")
print(convidados)  # {"Ana", "Carla", "Daniel"}


