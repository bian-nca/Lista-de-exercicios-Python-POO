class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

 
    def status(self):
        print("------------------------------- 🐒 INFORMAÇÕES MACACO 🐒  -----------------------")
        print(f"Nome do macaco: {self.nome}")
        print(f"Situação do bucho do macaco: {self.bucho}")

    def comer(self, alimento1, alimento2, alimento3):
        self.alimento1 = alimento1
        self.alimento2 = alimento2
        self.alimento3 = alimento3
        buchocheio = str(f"Estomâgo cheio! {self.nome} está satisfeito!")
        self.bucho = buchocheio

    def verbucho(self):
        print(f"As refeições que estão no estomâgo do macaquinho são: {self.alimento1}, {self.alimento2} , {self.alimento3}")

    def digerir(self):
        print(f"{self.nome} está digerindo a comida no momento!!")
        
