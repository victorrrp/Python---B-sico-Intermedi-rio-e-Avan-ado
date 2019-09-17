e=0
valor_hora=10
valor_hora_ex=20

c=int(input("Digite seu codigo: "))
h=float(input("Digite o numero de horas trabalhadas: "))

if h>50:
    e=(h-50)*valor_hora_ex
    salario=(50*valor_hora)+e
    print("Salario total{0:.2f}".format(salario))
    print("Salario excedente{0:.2f}".format(e))
else:
    salario=(h*valor_hora)
    print("Salario total{0:.2f}".format(salario))
    print("Salario excedente{0:.2f}".format(e))