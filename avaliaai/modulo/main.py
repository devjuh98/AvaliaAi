import utils as utils
import usuarios as usuarios
import menus as menus
from models.usuario import Usuario
from models.admin import Admin
import os, json

ARQUIVOUSUARIOS = os.path.join(os.path.dirname(__file__),'data', 'usuarios.json')

try:
    with open(ARQUIVOUSUARIOS, 'r', encoding = 'utf-8') as arq:
        for dados in json.load(arq):
            usuariocadastrado = Usuario(
                dados['nome_real'],
                dados['indice_nome'],
                dados['nome'], 
                dados['email'], 
                dados['senha'], 
                dados['status'])
            usuarios.usuarioslist.append(usuariocadastrado)
        #usuarios.usuarioslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    usuarios.usuarioslist = []
administrador1 = Admin('Guilherme Vasconcellos',0,'guiadm007','guilherme.vasconcellos@ufrpe.br','Adm123@','ativo')
administrador2 = Admin('Julia Galindo',0,'juliaadm007','julia.galindo@ufrpe.br','Adm123@','ativo')
usuarios.usuarioslist.append(administrador1)
usuarios.usuarioslist.append(administrador2)
usuariologado = None
utils.limpar()
menus.menu_inicial()
while True:

    try:
        
        opcao = int(input(""))
        while opcao not in [0,1,2]:
            utils.limpar()
            menus.menu_inicial()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
            opcao = int(input(""))
        if opcao == 1:
            cadastrou = usuarios.cadastrar_usuario()
            if cadastrou:
                opcao = 2
        if opcao == 2:
            usuariologado=usuarios.usuario_login()
            if usuariologado is not None:
                if isinstance(usuariologado, Admin):
                    menus.menu_de_escolha_admin(usuariologado)
                else:
                    menus.menu_de_escolha_usuario(usuariologado)
        
        if opcao == 0:
            utils.limpar()
            print('Programa encerrado')
            break
    except ValueError:
        utils.limpar()
        menus.menu_inicial()
        print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")