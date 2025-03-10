# Crie uma função que tenta modificar uma variável global chamada contador. 
# Demonstre a diferença entre usar e não usar a palavra global.


contador = 0

def modificar_sem_global():
  contador = 10
  print("Dentro da função (sem global):", contador)

def modificar_com_global():
  global contador
  contador = 10
  print("Dentro da função (com global):", contador)


print("Antes de modificar_sem_global:", contador)
modificar_sem_global()
print("Depois de modificar_sem_global:", contador)

print("Antes de modificar_com_global:", contador)
modificar_com_global()
print("Depois de modificar_com_global:", contador)