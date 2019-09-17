quant_hora=float(input("Informe o numero de horas trabalhadas no mês: "))
valor_hora=float(input("Informe quanto voce ganha por hora: "))

salario=quant_hora*valor_hora

print("Voce trabalha {0} horas por mês, cada hora voce ganha {1}. Seu salario é: {2:.2f}".format(quant_hora, valor_hora, salario))