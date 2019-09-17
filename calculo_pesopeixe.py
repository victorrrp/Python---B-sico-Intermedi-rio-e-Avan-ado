e=0
m=0

peso=float(input("Informe a quantidade quilos de peixe: "))

if  peso>50:
    m=(peso-50)*4
    e='excesso'
    print("Voce deverá pagar:{0:.2f}".format(m))
else:
    m=0
    e=0
    print("Multas:{0}".format(m))
    print("Excesso:{0}".format(e))