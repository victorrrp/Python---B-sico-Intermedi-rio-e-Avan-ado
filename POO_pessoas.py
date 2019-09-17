'''
Classes em python
'''

#def __init__ -> contém os parâmetros que serão alocados dentro das classes
#estão lá no main


#o self REFERENCIA o objeto no outro arquivo. nesse caso p1
from datetime import datetime
class Pessoa:
    
#ano_atual == atributo de classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    '''variavel = 'Valor' #o valor está sendo acessado no main através do self
        print(variavel)
    
    def outro_metodo(self): #para executar a partir do modo self
        print(self.nome)'''

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = True
            
    def comer(self, alimento):
        if self.comendo:  #caso ele já esteja comendo maçã
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
