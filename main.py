from POO_pessoas import Pessoa

'''
Para critério de explicação: 
p1 == objeto; 
Pessoa == instância da classe;
falar, comer, parar_comer == instância do objeto
'''
p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Victor', 22)

p1.comer('maçã') #é necessário colocar os parênteses
p1.falar('Poo') #delegando funções
p1.parar_comer()
p1.parar_comer()

p1.falar('Poo')
p1.comer('alimento')

p1.parar_comer()

p1.parar_comer()
p1.falar('assunto')



p2.falar('"Sem tempo irmão"')
p2.parar_falar()
p2.comer('churrasco')
p2.parar_comer()


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
