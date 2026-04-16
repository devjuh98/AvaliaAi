import utils
import getpass
import json

usuarioslist = []


def usuario_login():
   
    utils.limpar()
    utils.titulologin()
    while True:
        email = input('Digite o email do usuário para login ou 0 para cancelar\n')
        if email.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        senha = getpass.getpass('Digite a senha para login ou 0 para cancelar\n')
        if senha.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        for usuario in usuarioslist:
            if usuario['email'] == email.lower().strip() and usuario['senha'] == senha.strip():
                utils.limpar()
                print('\033[32mLogin efetuado com sucesso!\n\033[m')
                return email
        utils.limpar()
        utils.titulologin()
        print('\033[31mEmail ou senha incorretos. Tente novamente.\n\033[m')
    

def cadastrar_usuario():
    utils.limpar()
    utils.titulocadastro()
    while True:
        
        nome = input('Digite o nome do usuário ou 0 para cancelar cadastro:\n')
        if nome.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validanome(nome):
            utils.limpar()
            utils.titulocadastro()
            print("\033[32mNome Cadastrado!\n\033[m")
            break
        
    while True:
      
        email = input('Digite o email do usuário ou 0 para cancelar cadastro:\n').lower()
        utils.limpar() 
        if email.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validaemail(email):
            utils.limpar()
            utils.titulocadastro()
            print("\033[32mEmail Cadastrado!\n\033[m")
            break
       
    while True:

       
        senha = getpass.getpass('Digite a senha do usuário ou 0 para cancelar cadastro:\n')
        utils.limpar() 
        if senha.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validasenha(senha):
            utils.limpar()
            utils.titulocadastro()
            print("\033[32mSenha Cadastrada!\n\nCadastro concluído com sucesso!\n\033[m")
            input("\033[32mPressione Enter para ir ao login\033\n[m")
            break
        
    usuarioslist.append({
        'nome': nome.strip(),
        'email': email.strip().lower(),
        'senha': senha.strip(),
        'status': 'ativo'
    })
    with open('usuarios.json', 'w', encoding='utf-8') as arq:
        json.dump(usuarioslist, arq, indent = 4, ensure_ascii=False)
    usuario_login()

