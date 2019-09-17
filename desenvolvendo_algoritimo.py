n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))
n4=int(input("Digite o quarto numero: "))

q1=n1*n1
q2=n2*n2
q3=n3*n3
q4=n4*n4

if  q3>=1000:
    print(q3)
else:
    print("N1:{0}, Quadrado:{1}".format(n1, q1))
    print("N2:{0}, Quadrado:{1}".format(n2, q2))
    print("N3:{0}, Quadrado:{1}".format(n3, q3))
    print("N4:{0}, Quadrado:{1}".format(n4, q4))