class Carro :

  def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo =modelo
      self.ano = ano

  def exibir_informacoes(self):
      print(f"Marca: {self.marca}")
      print(f"Modelo: {self.modelo}")
      print(f"Ano: {self.ano}")


carro1 = Carro("Chevrolet", "Onix", 2020)
carro2 = Carro("Fiat", "Uno", 2019)

carro1.exibir_informacoes()