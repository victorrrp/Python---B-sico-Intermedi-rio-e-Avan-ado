vetor=[]
for n in range(1, 11):
    valor=int(input("Digite um valor: "))
    vetor.append(valor)

vetor.reverse()
for n in vetor:
    print(n)