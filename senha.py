nome=input("Informe seu nome: ")
senha=input("Digite sua senha: ")

while senha==nome:
    print("Sua senha não pode ser igual ao nome")
    nome=input("Informe o nome: ")
    senha=input("Digite sua senha: ")
print("Cadastro efetuado!")