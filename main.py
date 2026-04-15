import utils
import usuarios

utils.menuinicial()
while True:
    try:
        opcao = int(input(""))
        while opcao!= 1 and opcao!= 2 and opcao!= 0:
            utils.limpar()
            print("Opção inválida\nDigite um número do menu:\n")
            utils.menuinicial()
            opcao = int(input(""))
        if opcao == 1:utils.limpar();usuarios.cadastrar_usuario()
        if opcao == 2:usuarios.usuario_login()
        if opcao == 0:utils.limpar();print('Programa encerrado');break
    except ValueError:
        utils.limpar()
        print("Opção inválida\n Digite um número do menu\n")
        utils.menuinicial()