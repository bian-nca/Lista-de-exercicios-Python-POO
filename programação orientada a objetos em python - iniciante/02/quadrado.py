class Quadrado:
    def __init__(self, tamanho_lado, mudarvalor=False, retornar_valor=False, calcular_area = False):
        self.tamanho_lado = tamanho_lado
        self.mudarvalor = mudarvalor
        self.retornar_valor = retornar_valor
        self.calcular_area = calcular_area
#meu metodo construtor que tem como atributo = tamanho_lado e como metodos = mudarvalor, retornar_valor, calcular_area

    def status(self): 
        print("------------------------------INFORMAÇÕES DO OBJETO = QUADRADO----------------------------------")
        print(f'TAMANHO DO LADO DO QUADRADO: {self.tamanho_lado} cm')
  
        

    def novovalor(self):
        self.guardarvalor = self.tamanho_lado
        novolado = int(input("Informe o novo tamanho do lado: "))
        self.mudarvalor = True
        if(self.mudarvalor == True):
            self.tamanho_lado = novolado
        #se (self.mudarvalor for igual verdadeiro, então meu self.tamanho_lado irá receber o que está armazenado na minha variavél local, 
        # do meu metodo novovalor, "novolado")
        #Para que meu metodo retornevalor funcione,eu criei uma variavel chamada 'guardarvalor' a mesma irá receber o meu valor antigo do tamanho_lado, antes de eu mudá-lo
        #assim, quando eu chamar meu metodo retornevalor, o tamanho_lado irá conseguir utilizar essa nova variavel e voltar ao tamanho do lado original

#meu metodo novovalor tem como objetivo mudar o valor do lado, meu valor logico (mudarvalor) irá me auxiliar nesse metodo!!!

    def retornevalor(self):
        self.tamanho_lado = self.guardarvalor
        print(f'RETORNANDO AO VALOR ORIGIAL QUE ERA {self.tamanho_lado} cm')
        #self.guardarvalor foi criada no metodo novolado que serviu como base para o armazenamento do meu antigo valor do tamanho lado!
        

    def calculararea(self):
        area = self.tamanho_lado * self.tamanho_lado
        print(f'AREA DO QUADRADO: {area}')
        #Metodo que ao ser chamado irá calcular a area do quadrado


