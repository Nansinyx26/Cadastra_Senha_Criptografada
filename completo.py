from funcoes import *

#Menu:
 
while True:
 
    print("\n===== GERENCIADOR DE SENHAS =====")
    print("\n 1- Cadastrar serviço e senha \n 2- Visualizar senhas \n 3- Atualizar senhas \n 4- Remover senha \n 5- Salvar e sair")
    opção = input("\n Escolha a opção desejada: ")
 
    if opção == "1":
        print("Você escolheu cadastrar um serviço e senha.")
       
        novo_arquivo=input("Digite a instituiçao: ")
        senha=input("Digite a senha: ")
 
        novo_registro=criar_senha(novo_arquivo,senha)
        print("Novo registro criado com sucesso")
 
     
 
    elif opção == "2":
        print("Você escolheu visualizar as senhas.")
 
        instituiçao=input("Digite o nome da instituição ja cadastrada que deseja visualizar a senha: ")

        vizualizar=vizualizar_arquivo(instituiçao)

    elif opção == "3":
        print("Você escolheu atualizar as senhas.")
        arquivo=input("Digite o nome da instituição que deseja atualizar a sua senha: ")
        senha1=input("Digite a nova senha: ")
        atualizar=atualizar_senha(arquivo,senha1)



 
