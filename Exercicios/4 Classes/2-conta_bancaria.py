class ContaBancaria: 
  def __init__(self, saldo, titular):
      self.saldo = saldo
      self.titular = titular
        
  def depositar(self,valor):
      self.saldo += valor
      print(f"Depositado: {valor}. Saldo atual: {self.saldo}")
      return self.saldo
   

  def sacar(self,valor): 
      if self.saldo >= valor:
        saldo =- valor
        print(f"Sacado: {valor}. Saldo atual: {self.saldo}")
        return self.saldo
      else:
        print("Saldo insuficiente")


conta = ContaBancaria(1200, "João")
conta.depositar(300)
conta.sacar(100)
conta.sacar(1500)

