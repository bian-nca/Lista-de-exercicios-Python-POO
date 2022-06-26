from macaco import Macaco

m1 = Macaco('Cleiton', 'Estômago vazio')
m1.status()

m2 = Macaco('Max', 'Estomago cheio')
m2.status()
m2.comer('Maça','Banana','Morango')
m2.verbucho()

m3 = Macaco('Alex', '')
m3.comer('Banana', 'Maça', 'Banana')
m3.status()
m3.verbucho()
m3.digerir()

m4 = Macaco('Brenda', '')
m4.comer('Banana', 'Maça', m1)
m4.status()
m4.verbucho()

#Quando eu passo o m1 (meu objeto m1) criado aparece a seguinte forma:
#Nome do macaco: Brenda
# Situação do bucho do macaco: Estomâgo cheio! Brenda está satisfeito!
# As refeições que estão no estomâgo do macaquinho são: Banana, Maça , ***<macaco.Macaco object at 0x000002055C2F7C40>***
#nao tenho certeza se é possível um macaco "comer" outro macaco, mas ao apontar m1 como alimento para o m4, o código executa sem problemas e aponta o "Local" do objeto...
