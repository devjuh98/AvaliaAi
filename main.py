import utils
import usuarios
import json

try:
    with open('usuarios.json', 'r', encoding = 'utf-8') as arq:
        usuarios.usuarioslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    usuarios.usuarioslist = []
   


utils.menuinicial()

while True:
   
    try:
        opcao = int(input(""))
        while opcao!= 1 and opcao!= 2 and opcao!= 0:
            utils.limpar()
            utils.menuinicial()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
            opcao = int(input(""))
        if opcao == 1:usuarios.cadastrar_usuario()
        if opcao == 2:usuariologado=usuarios.usuario_login()
        if opcao == 0:utils.limpar();print('Programa encerrado');break
    except ValueError:
        utils.limpar()
        utils.menuinicial()
        print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")