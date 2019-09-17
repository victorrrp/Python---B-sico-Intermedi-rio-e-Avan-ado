vetor=[]
soma=0

for n in range(0, 20):
    valor=int(input("Digite {0}/20 para valor do vetor: "))
    vetor.append(valor)
    soma=soma+valor
print("Soma:{0}".format(soma))