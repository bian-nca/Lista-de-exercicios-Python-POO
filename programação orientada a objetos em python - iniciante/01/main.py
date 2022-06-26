from bola import Bola  #aqui estou importando a minha classe bola para instanciar meus objetos aqui no meu código principal

b1 = Bola('Vermelha',68, 'PLÁSTICO')  #b1 está sendo instanciado 
b1.status()  #b1.status() está chamando meu método, que, nesse caso, é o meu método status 
   
b2 = Bola('Azul', 89, 'BORRACHA')   #b2 está sendo instanciado, chamando meu construtor da classe Bola
b2.status()   #b2 está chamando meu metódo status
b2.trocandocor()   #b2 aqui está chamando meu metodo TROCANDOCOR que irá permitir que o usuário informe a nova cor do objeto b2 
b2.status()  #meu metodo status foi chamado novamente para conferirmos se a cor da bola foi realmente trocado
b2.mostrandocor()  #metodo que mostrará a cor atual da bola



