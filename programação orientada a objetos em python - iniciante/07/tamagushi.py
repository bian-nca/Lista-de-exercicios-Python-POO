class Tamagushi:
    def __init__(self, nome,idade):
            self.nome = nome
            self.idade = idade


    def status(self):
        print("--------------------TAMAGUSHI-----------------------")
        print(f'Nome do tamagushi: {self.nome}')
        print(f'Idade do tamagushi: {self.idade} anos!')
      

    def alterar(self):
        self.oldnome = self.nome
        self.oldidade = self.idade
        #self.oldnome e self.oldidade irão armazenar meus dados do tamagushi q foram alterados caso precise retornar depois os valores originais
        novonome = str(input("Informe o novo nome do Tamagushi: "))
        self.nome = novonome
        novaidade = int(input("Informe a nova idade do tamagushi: "))
        self.idade = novaidade

    def retornar(self):
        self.nome = self.oldnome
        self.idade = self.oldidade

    def humor(self):
        humor = 0
        fome = str(input("O tamagushi está com fome? [SIM | NAO] "))
        if(fome == "NAO"):
            humor = humor +1
        saude = str(input("Informe a condição do tamagushi: [doente | saudavel]"))
        if(saude == "saudavel"):
            humor = humor + 1
        if(humor ==0):
            print("Tamagushi está com fome e doente, por favor, cuide melhor dele!")
            print(f"O HUMOR DO {self.nome} ESTÁ PÉSSIMO!")
            print(f"o(╥﹏╥)o ")
        if (humor == 1) and(fome == 'NAO'):
            print("Tamagushi está com o humor mais ou menos!")
            print("Cuide melhor da saúde do seu tamagushi!")
        if(humor==1) and (fome == 'SIM'):
            print("Tamagushi está com o humor mais ou menos!")
            print("Por favor, alimente o seu tamagushi!")
        if(humor ==2):
            print(f"O humor do seu tamagushi está excelente!{self.nome} está feliz!!")
            print(f"｡◕‿◕｡ ")

    def alimentar(self):
        comida = int(input("Informe o quanto você quer dar de comida ao bichinho: [1 | 2| 3] "))
        if(self.comida ==1):
            print(f"{self.nome} continua com fome!")
        if(self.comida ==2):
            print(f"{self.nome} está satisfeito!")
        else:
            print(f"{self.nome} irá explodir de tanto comer!!! CUIDADO!")

    def brincar(self):
        self.brincando = int(input("Informe a quantidade de tempo que você quer brincar com o bichinho: [5 | 10 | 15| 20 ]"))

    def tedio(self):
        if(self.brincando ==5):
            print(f"{self.nome} já está com tédio!!")
        if(self.brincando == 10): 
            print(f"{self.nome} ficará com tédio em alguns minutos!")
        if(self.brincando ==15):
            print(f"{self.nome} brincou bastante e agorá está ficando com sono!")
        if(self.brincando==20):
            print(f"{self.nome} brincou muito e agora está descansando!!")
        
 