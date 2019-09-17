vetor=[]
cod=int(input("Digite seu codigo: "))
if cod!=0:
    for i in range(0, 5):
        valor=float(input("Digite um valor: "))
        vetor.append(valor)
    if cod==1:
        for i in vetor:
            print(i)
    if cod==2:
        vetor.reverse()
        for i in vetor:
            print(i)        