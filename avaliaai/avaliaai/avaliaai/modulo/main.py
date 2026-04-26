import modulo.utils as utils
import modulo.usuarios as usuarios
import modulo.menus as menus
import os, json

ARQUIVOUSUARIOS = os.path.join(os.path.dirname(__file__), 'usuarios.json')

try:
    with open(ARQUIVOUSUARIOS, 'r', encoding = 'utf-8') as arq:
        usuarios.usuarioslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    usuarios.usuarioslist = []

usuariologado = None

while True:

    utils.limpar()
    menus.menuinicial()

    try:
        opcao = int(input(""))
        while opcao not in [0,1,2]:
            utils.limpar()
            menus.menuinicial()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
            opcao = int(input(""))
        if opcao == 1:
            cadastrou = usuarios.cadastrar_usuario()
            if cadastrou:
                opcao = 2
        if opcao == 2:
            usuariologado=usuarios.usuario_login()
            if usuariologado is not None:
                menus.menudeescolha(usuariologado)
        
        if opcao == 0:
            utils.limpar()
            print('Programa encerrado')
            break
    except ValueError:
        utils.limpar()
        menus.menuinicial()
        print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")