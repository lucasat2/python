def adicionar_item(inventario, item, quantidade=1):
  if item in inventario:
    inventario[item] += quantidade
  else:
    inventario[item] = quantidade

def remover_item(inventario, item, quantidade=1):
  if item in inventario:
    inventario[item] -= quantidade
    if inventario[item] <= 0:
      del inventario[item]

def listar_inventario(inventario):
  for item, quantidade in inventario.items():
    print(f"{item}: {quantidade}")

def gerenciar_inventario():
  inventario = {}
  
  adicionar_item(inventario, "Poção de Cura", 3)
  adicionar_item(inventario, "Espada", 2)
  adicionar_item(inventario, "Escudo", 1)
  
  remover_item(inventario, "Espada", 2)
  
  listar_inventario(inventario)

if __name__ == "__main__":
  gerenciar_inventario()