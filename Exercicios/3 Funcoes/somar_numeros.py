def somar_numeros(*args): #posso passar quantos argumentos eu quiser
  if not args:  #se não tiver argumentos
    return None #retorna None
  return max(args) #retorna o maior valor

# Exemplos de uso
print(somar_numeros(10)) # retorna 10
print(somar_numeros(10, 30, 20)) # retorna 30
print(somar_numeros(5, 10, 50, 40)) # retorna 50
print(somar_numeros()) # retorna None