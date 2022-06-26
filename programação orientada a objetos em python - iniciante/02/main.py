from quadrado import Quadrado

q1 = Quadrado(12)
q1.status()

q2 = Quadrado(6)
q2.status()
q2.calculararea()


q3 = Quadrado(8) 
q3.status()
q3.novovalor()
q3.status()
q3.calculararea()
#No objeto q3 foi instanciado como tamanho lado = 8
#seu status mostrará isso, mas ao chamar meu metodo novovalor() isso irá mudar 
#meu metodo irá permitir que o usuario informe o novo lado do tamanho do lado
#para saber se foi alterado chamei meu metodo status que mostrará se o valor do tamanho lado foi alterado ou nao
#calculararea ira calcular a area do meu quadrado, nesse caso, ja com o novo valor atribuido

q4 = Quadrado(10)
q4.status()
q4.novovalor()
q4.status()
q4.retornevalor()
q4.status()

#no objeto q4, ele foi inicialmente instanciando com o tamanho do lado igual a a 10
#foi requerido o metodo status para mostrar a sua caracteritisca, dessa forma logo depois chamei meu metodo novalor que irá pedir para o usuario informar o novo lado do tamanho do quadrado
# em seguida chamei meu metodo status para conferir se o novo valor foi passado
#assim, chamei meu metodo retornevalor() que irá retornar com o valor original do lado, no caso o tamanho do lado voltou a ser 10!