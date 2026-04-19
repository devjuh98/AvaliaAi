import avaliaai.utils as utils
import avaliaai.usuarios as usuarios
import os, json

ARQUIVO = os.path.join(os.path.dirname(__file__), 'usuarios.json')

try:
    with open(ARQUIVO, 'r', encoding = 'utf-8') as arq:
        usuarios.usuarioslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    usuarios.usuarioslist = []

usuariologado = None

while True:

    utils.limpar()
    utils.menuinicial()

    try:
        opcao = int(input(""))
        while opcao!= 1 and opcao!= 2 and opcao!= 0:
            utils.limpar()
            utils.menuinicial()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
            opcao = int(input(""))
        if opcao == 1:
            cadastrou = usuarios.cadastrar_usuario()
            if cadastrou:
                opcao = 2
        if opcao == 2:
            usuariologado=usuarios.usuario_login()
            if usuariologado is not None:
                utils.menudeescolha(usuariologado)
        
        if opcao == 0:
            utils.limpar()
            print('Programa encerrado')
            break
    except ValueError:
        utils.limpar()
        utils.menuinicial()
        print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")