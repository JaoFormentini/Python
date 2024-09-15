class Empregado:
    def __init__(self, nome, salariobase):
      self.nome = nome  
      self.salariobase = salariobase
     
    def salario(self):
      return self.salariobase

class Gerente(Empregado):
    def salariobonus(self):
      total = self.salariobase * 1.4
      return f"O salario do gerente é: {total}"

class Vendedor(Empregado):
    def salariovend(self):
      comissao = self.salariobase * 1.15
      return f"O salario do vendedor é igual a: {comissao}"

x = float(input("Qual o salario base? "))

nicolas = Gerente("Nicolas",x)
Vitor = Vendedor("Vitor",x)

print(f"O salario base é: {nicolas.salario()}")
print(nicolas.salariobonus())

print(f"\nO salario base é: {Vitor.salario()}")
print(Vitor.salariovend())

