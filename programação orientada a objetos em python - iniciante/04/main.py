from pessoa import Pessoa

p1 = Pessoa('bianca', 20, 62, 1.54)
p1.status()


p2 = Pessoa('thiago', 18, 89, 1.89)
p2.envelhercer()
p2.status()

#no meu p2 é chamado meu metodo envelhecer que irá "passar um ano", ou seja, no caso meu objeto terá 19 anos e nao 18 
#e tbm por condicão ele irá "crescer" 0.5cm a mais por ter menos de 21 anos

p3 = Pessoa('alzinete', 22, 76, 1.65)
p3.envelhercer()
p3.status()

#esse objeto foi criado para mostrar que, mesmo meu metodo envelhercer seja chamado, apenas a idade será alterada, mas a altura não irá pois a pessoa tem mais de 21 anos

p4 = Pessoa('dylan', 20, 69, 1.78)
p4.envelhercer()
p4.status()
p4.emagrecer()

#aqui, apenas a idade tbm sera alterada pois, mesmo o meu objeto tendo apeans 20 anos, quando eu chamo meu metodo enverlhecer, ele irá ter 21 anos e nao será aceito na minha condicional de altura

p5 = Pessoa('Flavia', 32, 56, 1.53)
p5.status()
p5.engordar()
