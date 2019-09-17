m=0
n=int(input("Informe um numero: "))
while n!=0:
    if n>m:
        m=n
    n=int(input("Informe um numero: "))
print("O maior numero é: {0}".format(m))