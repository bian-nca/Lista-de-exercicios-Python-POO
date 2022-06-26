class Bombacombustivel:
    def __init__(self, tipocombustivel, qtdcombustivel, valorlitro):
        self.tipocombustivel = tipocombustivel
        self.qtdcombustivel = qtdcombustivel
        self.valorlitro = valorlitro


    def abastecerporvalor(self):
        valor = float(input("Informe o valor a ser abastecido: R$"))
        litros = self.valorlitro * valor
        print(f"Aquantidade de litros que foi colocada no veículo: {litros}")

    def abastercerporlitro(self):
        comb = float(input("Informe a quantidade em litros de combustivel: "))
        self.valorlitro = (comb * self.valorlitro)
        print(f"TOTAL A PAGAR: R$ {self.valorlitro} reais")
    
    def alterarvalor(self):
        novovalor = float(input("Informe o novo valor do litro do combustivel: "))
        self.valorlitro = novovalor

    def alterarcombustivel(self):
        tipocomb = str(input("Informe o tipo de combustível: "))
        self.tipocombustivel = tipocomb

    def alterarqtdcombustivel(self):
        litros = float (input("Informe a quantidade de livros que foi utilizado para abastecer: "))
        self.combustivel = self.qtdcombustivel - litros
        print(f"A quantidade de litros na bomba no total agora é : {self.combustivel} litros")

    def status(self):
        print("--------------------info--------------------------")
        print(f"TIPO DO COMBUSTIVEL: {self.tipocombustivel}")
        print(f"QUANTIDADE DE COMBUSTIVEL: {self.qtdcombustivel}")
        print(f"VALOR DO LITRO: {self.valorlitro}")

