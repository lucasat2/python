class ContaBancaria: 
  def __init__(self, saldo, titular):
      self.__saldo = saldo
      self.titular = titular


  def get_saldo(self):
      return self.__saldo

  def set_saldo(self, valor):
      if self.__saldo < 0:
        print("Saldo não pode ser negativo")
      else:
        self.__saldo = saldo
       
  def depositar(self,valor):
      self.__saldo += valor
      print(f"Depositado: {valor}. Saldo atual: {self.__saldo}")
      return self.__saldo
   

  def sacar(self,valor): 
      if self.__saldo >= valor:
        saldo =- valor
        print(f"Sacado: {valor}. Saldo atual: {self.__saldo}")
        return self.__saldo
      else:
        print("Saldo insuficiente")


conta = ContaBancaria(1200, "João")
conta.depositar(300)
conta.sacar(100)
conta.sacar(1500)

