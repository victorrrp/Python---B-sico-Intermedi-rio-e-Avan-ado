contador_esfera=0
contador_limpeza=0
contador_cabo_conector=0
contador_quebrado=0
quantidade=0

identificador=int(input("Digite o id do mouse: "))
while identificador!=0:
    print("1-Esfera")
    print("2-Limpeza")
    print("3-Cabo e Conector")
    print("4-Quebrado")
    
    defeito=int(input("Digite o defeito: "))

    if defeito==1:
        contador_esfera=contador_esfera+1
    elif defeito==2:
        contador_limpeza=contador_limpeza+1
    elif defeito==3:
        contador_cabo_conector=contador_cabo_conector+1
    elif defeito==4:
        contador_quebrado=contador_quebrado+1
    quantidade=quantidade+1
    identificador=int(input("Digite o id do mouse: "))

p1=contador_esfera/quantidade*100.0
p2=contador_limpeza/quantidade*100.0
p3=contador_cabo_conector/quantidade*100.0
p4=contador_quebrado/quantidade*100.0

print("Quantidade de mouses: {0}".format(quantidade))
print("Situação                        Quantidade              Percentual")
print("1-Esfera                           {0}                   {1:.2f}%".format(contador_esfera, p1))
print("2-Limpeza                          {0}                   {1:.2f}%".format(contador_limpeza, p2))
print("3-Cabo e Conector                  {0}                   {1:.2f}%".format(contador_cabo_conector, p3))
print("4-Quebrado                         {0}                   {1:.2f}%".format(contador_quebrado, p4))