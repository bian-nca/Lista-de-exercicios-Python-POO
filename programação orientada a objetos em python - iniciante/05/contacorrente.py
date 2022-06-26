class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo


 #alterarNome, depósito e saque;

    def status(self):
        print("--------------------INFORMAÇÕES DA CONTA CORRENTE---------------------------")
        print(f'Numero da conta: {self.numero_conta}')
        print(f'Nome do correntista: {self.nome_correntista}')
        print(f'Saldo: R$ {self.saldo} reais na conta!')

    def alterarNome(self):
        novonome = str(input('Informe qual o nome que você deseja: '))
        self.nome_correntista = novonome

    def deposito(self):
        depositando = float(input("Informe quanto você quer depositar: "))
        self.saldo = self.saldo + depositando
        return self.saldo
    
    def saque(self):
        retirando = float(input("Informe quanto você quer retirar: "))
        self.saldo = self.saldo - retirando
        return self.saldo