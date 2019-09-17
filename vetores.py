vetor=[]#lista vazia
pares=[]#lista vazia

for n in range(1, 11):
    vetor.append(n)#adiciona ao final do vetor o valor da variavel
    if n%2==0:
        pares.append(n)
for p in pares:#pegando numero no próprio vetor
    print(p)