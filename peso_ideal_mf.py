sexo=input("Digite seu sexo (m/f): ")
altura=float(input("Digite sua altura: "))

#.lower()--> converte toda letra maiuscula em minuscula
if  sexo.lower()=='m':
    peso_ideal=(72.7*altura)-58

elif  sexo.lower()=='f':
    peso_ideal=(62.1*altura)-44.7

else:
    print("Sexo não reconhecido.")
print("Seu peso ideal é:{0:.2f}".format(peso_ideal))