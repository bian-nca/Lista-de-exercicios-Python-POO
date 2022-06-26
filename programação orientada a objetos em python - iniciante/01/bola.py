class Bola:
    def __init__(self, cor, circunferencia, material, trocacor=False, mostracor= False):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material 
        self.trocacor = trocacor
        self.mostracor = mostracor

#class Bola é onde estou criando a minha classe Bola
#def __init__ é meu construtor em si com os seguintes atributos e metodos (ATRIBUTOS = cor, circunferencia, material   METODOS = trocacor, mostracor)
#os metodos troccor, mostracor são parametros, não exigidos na hora de instanciar um objeto, que servirá como base 'valores lógicos' dentro dos metodos que irei criar em seguida

    def status(self):
        print('------------------------INFORMAÇÕES DA BOLA-------------------------------')
        print(f'COR DA BOLA: {self.cor}')
        print(f'CIRCUNFERÊNCIA DA BOLA: {self.circunferencia} cm')
        print(f'MATERIAL DA BOLA: {self.material}') 
        #meu metodo status servirá para mostrará o que foi definido, como características, para meus objetos instanciados!!!

    def trocandocor(self):
       cornova = input(print(f'Informe a nova cor da bola: '))
       self.trocacor = True
       if(self.trocacor == True):
            self.cor = cornova
       else:
        self.cor = self.cor
        #meu metodo trocandocor tem como finalidade deixar que o usuário informe a nova cor da bola, o próprio usuário irá definir esse atributo
        #quando esse metodo é chamado, meu valor logico do 'trocacor' é passado para verdadeiro e dessa forma,
        #  "se self.trocacor ==verdadeiro" meu atributo cor irá receber o significado que a minha variavel 'cornova' irá receber
        #caso "se self.trocacor nao for verdadeiro" entao meu self.cor continuará com seu valor anterior
    
    def mostrandocor(self):
        print(F'A COR DA BOLA, NESSE EXATO MOMENTO, É {self.cor}')
        self.mostracor = True
      