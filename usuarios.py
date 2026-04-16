import utils
import getpass
import json

tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
titulocadastro = '\033[36mCADASTRO DE USUÁRIO\033[m'
titulologin = '\033[36mLOGIN DE USUÁRIO\033[m'

usuarioslist = []


def usuario_login():
    try:
        with open('usuarios.json', 'r', encoding = 'utf-8') as arq:
            usuarioslist = json.load(arq)

        utils.limpar()
        print(titulologin.center(50, '='), '\n')
        while True:
            email = input('Digite o email do usuário para login ou 0 para cancelar\n')
            if email.strip() == '0':
                utils.limpar()
                print(tituloinicial.center(50,'='), '\n\n')
                utils.menuinicial()
                return
            senha = getpass.getpass('Digite a senha para login ou 0 para cancelar\n')
            if senha.strip() == '0':
                utils.limpar()
                print(tituloinicial.center(50,'='), '\n\n')
                utils.menuinicial()
                return
            for usuario in usuarioslist:
                if usuario['email'] == email.lower() and usuario['senha'] == senha:
                    utils.limpar()
                    print('\033[32mLogin efetuado com sucesso!\n\033[m')
                    return email
            utils.limpar()
            print(titulologin.center(50, '='),'\n')
            print('\033[31mEmail ou senha incorretos. Tente novamente.\n\033[m')
    except(FileNotFoundError, json.JSONDecodeError):
        utils.limpar()
        print("Não há usuários cadastrados!\nVoltando para tela inicial...\n")
        print(tituloinicial.center(50, '='),'\n\n')
        utils.menuinicial()
        return

def cadastrar_usuario():
    utils.limpar()
    print(titulocadastro.center(50, '='),'\n')
    while True:
        
        nome = input('Digite o nome do usuário ou 0 para cancelar cadastro:\n')
        if nome.strip() == '0':
            utils.limpar()
            print(tituloinicial.center(50,'='), '\n\n')
            utils.menuinicial()
            return
        if utils.validanome(nome):
            utils.limpar()
            print(titulocadastro.center(50, '='),'\n')
            print("\033[32mNome Cadastrado!\n\033[m")
            break
        
    while True:
      
        email = input('Digite o email do usuário ou 0 para cancelar cadastro:\n').lower()
        utils.limpar() 
        if email.strip() == '0':
            utils.limpar()
            print(tituloinicial.center(50,'='), '\n\n')
            utils.menuinicial()
            return
        if utils.validaemail(email):
            utils.limpar()
            print(titulocadastro.center(50, '='),'\n')
            print("\033[32mEmail Cadastrado!\n\033[m")
            break
       
    while True:

       
        senha = getpass.getpass('Digite a senha do usuário ou 0 para cancelar cadastro:\n')
        utils.limpar() 
        if senha.strip() == '0':
            utils.limpar()
            print(tituloinicial.center(50,'='), '\n\n')
            utils.menuinicial()
            return
        if utils.validasenha(senha):
            utils.limpar()
            print(titulocadastro.center(50, '='),'\n')
            print("\033[32mSenha Cadastrada!\n\nCadastro concluído com sucesso!\n\033[m")
            input("\033[32mPressione Enter para ir ao login\033[m")
            break
        
    usuarioslist.append({
        'nome': nome,
        'email': email,
        'senha': senha,
        'status': 'ativo'
    })
    with open('usuarios.json', 'w', encoding='utf-8') as arq:
        json.dump(usuarioslist, arq, indent = 4, ensure_ascii=False)
    usuario_login()

