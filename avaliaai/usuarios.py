import avaliaai.utils as utils
import getpass
import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), 'usuarios.json')
usuarioslist = []

def usuario_login():
   
    utils.limpar()
    utils.titulologin()
    while True:
        email = input('Digite o e-mail do usuário para login ou 0 para cancelar:\n\n').strip()
        while not email:
            utils.limpar()
            utils.titulologin()
            email = input('\033[31mE-mail não pode ser vazio.\n\033[m\nDigite o e-mail do usuário ou 0 para cancelar:\n\n').strip()
        if email == '0':
            utils.limpar()
            utils.menuinicial()
            return
        senha = getpass.getpass('\nDigite a senha para login ou 0 para cancelar:\n\n').strip()
        while not senha:
            utils.limpar()
            utils.titulologin()
            print('\033[31mSenha não pode ser vazia.\033[m\n\nE-mail digitado: ', email)
            senha = getpass.getpass('\nDigite a senha do usuário ou 0 para cancelar:\n\n').strip()
        if senha == '0':
            utils.limpar()
            utils.menuinicial()
            return
        for usuario in usuarioslist:
            if usuario['email'] == email.lower() and usuario['senha'] == senha:
                utils.limpar()
                print('\033[32mLogin efetuado com sucesso!\n\033[m')
                return usuario
        utils.limpar()
        utils.titulologin()
        print('\033[31mEmail ou senha incorretos. Tente novamente.\n\033[m')
    

def cadastrar_usuario():
    utils.limpar()
    utils.titulocadastro()
    while True:
        
        nome = input('Digite o nome do usuário ou 0 para cancelar cadastro:\n\n')
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
      
        email = input('Digite o email do usuário ou 0 para cancelar cadastro:\n\n').lower()
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

        senha = getpass.getpass('Digite a senha do usuário ou 0 para cancelar cadastro:\n\n')
        utils.limpar() 
        if senha.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validasenha(senha):
            utils.limpar()
            utils.titulocadastro()
            confirmasenha = getpass.getpass('Confirme a senha ou digite 0 para cancelar cadastro:\n\n')
            if confirmasenha == '0':
                utils.limpar()
                utils.menuinicial()
                return
            while confirmasenha != senha:
                utils.limpar()
                utils.titulocadastro()
                confirmasenha = getpass.getpass('\n\033[31mSenhas não coincidem.\033[m\n\nTente novamente ou digite 0 para cancelar cadastro:\n\n')
                if confirmasenha == '0':
                    utils.limpar()
                    utils.menuinicial()
                    return
            usuarioslist.append({
            'nome': nome.strip(),
            'email': email.strip().lower(),
            'senha': senha.strip(),
            'status': 'ativo'
            })
            with open(ARQUIVO, 'w', encoding='utf-8') as arq:
                json.dump(usuarioslist, arq, indent = 4, ensure_ascii=False)
            utils.limpar()
            utils.titulologin()
            print("\033[32mSenha Cadastrada!\n\nCadastro concluído com sucesso!\n\033[m")
            input("\033[32mPressione Enter para ir ao login\033\n\n[m")
            return True

# Função para salvar os dados dos usuários no arquivo JSON
def salvar():
    with open(ARQUIVO, 'w', encoding='utf-8') as arq:
        json.dump(usuarioslist, arq, indent = 4, ensure_ascii=False)

# Funções para editar informações do usuário
def editar_nome(usuariologado, novo_nome):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["nome"] = novo_nome.strip()
            salvar()
            print("\033[32mNome atualizado com sucesso!\n\033[m")
            return True
    return False
def editar_email(usuariologado, novo_email):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["email"] = novo_email.strip().lower()
            salvar()
            print("\033[32mEmail atualizado com sucesso!\n\033[m")
            return True
    return False
def editar_senha(usuariologado, nova_senha):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["senha"] = nova_senha.strip()
            salvar()
            print("\033[32mSenha atualizada com sucesso!\n\033[m")
            return True
    return False
