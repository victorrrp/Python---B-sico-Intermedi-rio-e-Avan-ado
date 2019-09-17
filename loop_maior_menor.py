maior=-999
menor=999
soma=0
valor=0
for n in range(1,11):
    valor=int(input("Informe um valor: "))
    if valor>0:
        valor=valor
    if valor>maior:
        maior=valor
    if menor==-1 or valor<menor:
        menor=valor
    soma=soma+valor
media=soma/10
print("Maior: {0}".format(maior))
print("Menor: {0}".format(menor))
print("Media: {0}".format(media))