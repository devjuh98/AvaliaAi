import utils
import usuarios


tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
print(tituloinicial.center(50, '='),'\n\n')
utils.menuinicial()

while True:
   
    try:
        opcao = int(input(""))
        while opcao!= 1 and opcao!= 2 and opcao!= 0:
            utils.limpar()
            print(tituloinicial.center(50, '='),'\n\n')
            print("\033[31mOpção inválida\033[m\nDigite um número do menu:\n")
            utils.menuinicial()
            opcao = int(input(""))
        if opcao == 1:usuarios.cadastrar_usuario()
        if opcao == 2:usuariologado=usuarios.usuario_login()
        if opcao == 0:utils.limpar();print('Programa encerrado');break
    except ValueError:
        utils.limpar()
        print(tituloinicial.center(50, '='),'\n\n')
        print("\033[31mOpção inválida\033[m\nDigite um número do menu:\n")
        utils.menuinicial()