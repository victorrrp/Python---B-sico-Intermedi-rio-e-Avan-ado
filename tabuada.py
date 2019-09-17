n=int(input("Informe um numero entre 1 e 10: "))

while n>10:
    print("O numero deve ser menor que 10")
    n=int(input("Informe um numero: "))
print("Tabuada de {0}". format(n))
valor=0
for i in range(1,11):
    valor=n*i
    print("{0} x {1}= {2}".format(n, i, valor))