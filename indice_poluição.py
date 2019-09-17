indice=float(input("Digite o indice de poluição: "))

if  indice>=0.3 and indice<0.4:
    print("Grupo 1 suspender atividades")
elif  indice>=0.4 and indice<0.5:
    print("Grupo 1 e 2 suspender atividades")
elif  indice>=0.5:
    print("Todos os grupos, suspender atividades")
else:
    print("Níveis aceitáveis")