class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def status(self):
        print("------------------------------FUNCIONARIO-----------------------")
        print(f"Nome do funcionario: {self.nome}")
        print(f"Salario do(a) {self.nome}: R$ {self.salario} reais")