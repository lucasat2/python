from dataclasses import dataclass

@dataclass
class Endereco:
    rua: str
    numero: int
    cidade: str
    estado: str
    cep: str

adress = Endereco("Rua das Flores", 123, "São Paulo", "SP", "12345-678")
adress2 = Endereco("Rua das Flores", 123, "São Paulo", "SP", "12345-678")

print(adress.rua)
print(adress.numero)
print(adress.cidade)
print(adress.estado) 
print(adress.cep)

print(adress == adress2)
