vetor=[]
posição=0
maiores_50=False
for n in range(0, 10):
    valor=int(input("Informe {0} valor para i vetor: ".format(n+1)))
    vetor.append(valor)
for n in vetor:
    if n>50:
        print("Valor {0} maior que 50 na posição {1}".format(n, posição))
        maiores_50=True
    posição=posição+1
if maiores_50==False:
    print("Não tem nenhum numero maior que 50")