class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self. nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def status(self):
        print('-------------------------INFORMAÇÕES DA PESSOA CADASTRADA---------------------------------')
        print(f'NOME: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Peso: {self.peso} kg')
        print(f'Altura: {self.altura} metros')

#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

    def envelhercer(self):
        self.idade = self.idade + 1
        if(self.idade < 21):
            self.altura = self.altura + 0.5

    def engordar(self):
        calorias = 0
        caloria1 = str(input("VOCÊ TOMOU CAFÉ DA MANHÃ? [SIM | NAO]"))
        if (caloria1 == "SIM"):
            calorias = calorias + 100
        caloria2 = str(input("VOCÊ ALMOÇOU? [SIM | NAO] "))
        if(caloria2 == "SIM"):
            calorias = calorias + 100
        caloria3 = str (input("VOCÊ JANTOU? [SIM | NAO] "))
        if (caloria3 == "SIM"):
            calorias = calorias + 100
        if(calorias == 100):
            print(f'Você engordou apenas {calorias} calorias!!')
        if(calorias == 200):
            print(f'Você engordou apenas {calorias} calorias!!!')
        if(calorias == 300):
            print(f' Você engordou {calorias} calorias!!')
        if(calorias == 0):
            print(f'Você não comeu nada o dia todo, isso não faz bem para a saúde... por favor, coma algo!!')
#como nao foi definido o que meu metodo engordar deveria fazer, criei da seguinte maneira:
# pensando nas tres refeições ao dia, a cada refeição que a pessoa faz, 100 calorias ela irá ganhar, dessa forma, contabilizando essas calorias dependendo da resposta dela
#caso a pessoa nao coma nada, irá mostrar na tela para a pessoa se alimentar pois nao faz bem a saude ficar sem comer o dia todo!!
        

    def emagrecer(self):
       contagem = 0
       acad = str(input("Você faz academia? [SIM | NAO]"))
       if(acad == "SIM"):
        contagem = contagem + 1
       regime = str(input("Você faz dieta? [SIM | NAO] "))
       if(regime == "SIM"):
        contagem = contagem + 1
       if(contagem == 1) and (acad =='SIM'):
        print("você irá emagrecer bem devagar pois apenas fazer academia não adianta se você não fazer a sua dieta")
       if (contagem == 1) and(regime == 'SIM'):
        print("você precisa fazer academia junto com a sua dieta, pois, caso nao, irá emagrecer devagar!")
       if(contagem == 2):
         print("você está no caminho certo para emagrecer!!")
       if(contagem == 0):
        print("Voce nao vai emagrecer sozinho se nao fazer academia e dieta!!!")

    def crescer(self):
       pass


