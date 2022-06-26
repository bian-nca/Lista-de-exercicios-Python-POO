from contacorrente import ContaCorrente

cc1 = ContaCorrente(00000-12, 'Bianca', 0.00)
cc1.status()

cc2 = ContaCorrente(3203-14, 'Thiago',1200.00)
cc2.status()

cc3 = ContaCorrente(21232-12,'max', 15000.00)
cc3.status()
cc3.saque()
cc3.status()

cc4 = ContaCorrente(232323-12,'bea', 1212.00)
cc4.status()
cc4.alterarNome()
cc4.deposito()
cc4.status()