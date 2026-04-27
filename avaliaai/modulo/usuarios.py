import utils as utils
import menus as menus
import json
import os

ARQUIVOUSUARIOS = os.path.join(os.path.dirname(__file__), 'usuarios.json')
usuarioslist = []

def usuario_login():
    '''Função para realizar o login do usuário,
    não possui parâmetros de entrada e retorna o usuário logado ou None.'''
   
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
            menus.menuinicial()
            return
        print('\nDigite a senha para login ou 0 para cancelar:\n')
        senha = utils.senha_com_asterisco().strip()
        
        while not senha:
            utils.limpar()
            utils.titulologin()
            print('\033[31mSenha não pode ser vazia.\033[m\n\nE-mail digitado: ', email)
            senha = utils.senha_com_asterisco().strip()
            print('\nDigite a senha do usuário ou 0 para cancelar:\n\n').strip()
        if senha == '0':
            utils.limpar()
            menus.menuinicial()
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
    '''Função para realizar o cadastro do usuário,
    armazenando os dados em um json e em uma lista
    sem parâmetros de entrada e sem retorno.'''
    
    utils.limpar()
    utils.titulocadastro()
    while True:
        
        nome = input('Digite o nome do usuário ou 0 para cancelar cadastro:\n\n')
        if nome.strip() == '0':
            utils.limpar()
            menus.menuinicial()
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
            menus.menuinicial()
            return
        if utils.validaemail(email):
            utils.limpar()
            utils.titulocadastro()
            print("\033[32mEmail Cadastrado!\n\033[m")
            break
       
    while True:

        print('Digite a senha do usuário ou 0 para cancelar cadastro:\n')
        senha = utils.senha_com_asterisco().strip()
        utils.limpar() 
        if senha.strip() == '0':
            utils.limpar()
            menus.menuinicial()
            return
        if utils.validasenha(senha):
            utils.limpar()
            utils.titulocadastro()
            print('Confirme a senha ou digite 0 para cancelar cadastro:\n')
            confirmasenha = utils.senha_com_asterisco().strip()
            if confirmasenha == '0':
                utils.limpar()
                menus.menuinicial()
                return
            while confirmasenha != senha:
                utils.limpar()
                utils.titulocadastro()
                print('\n\033[31mSenhas não coincidem.\033[m\n\nTente novamente ou digite 0 para cancelar cadastro:\n')
                confirmasenha = utils.senha_com_asterisco().strip()
                if confirmasenha == '0':
                    utils.limpar()
                    menus.menuinicial()
                    return
            usuarioslist.append({
            'nome': nome.strip(),
            'email': email.strip().lower(),
            'senha': senha.strip(),
            'status': 'ativo'
            })
            salvar()
            utils.limpar()
            utils.titulocadastro()
            print("\033[32mSenha Cadastrada!\n\nCadastro concluído com sucesso!\n\033[m")
            input("\033[32mPressione Enter para ir ao login\033\n\n[m")
            return True

# Função para salvar os dados dos usuários no arquivo JSON
def salvar():
    with open(ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
        json.dump(usuarioslist, arq, indent = 4, ensure_ascii=False)

# Funções para editar informações do usuário
def editar_nome(usuariologado, novo_nome):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["nome"] = novo_nome.strip()
            salvar()
            print("\033[32mNome atualizado com sucesso!\n\033[m")
            input("Pressione Enter para voltar ao menu...")
            return True
    return False
def editar_email(usuariologado, novo_email):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["email"] = novo_email.strip().lower()
            salvar()
            print("\033[32mEmail atualizado com sucesso!\n\033[m")
            input("Pressione Enter para voltar ao menu...")
            return True
    return False
def editar_senha(usuariologado, nova_senha):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuario["senha"] = nova_senha.strip()
            salvar()
            print("\033[32mSenha atualizada com sucesso!\n\033[m")
            input("Pressione Enter para voltar ao menu...")
            return True
    return False

# Função para deletar a conta do usuário
def deletar_conta(usuariologado):
    for usuario in usuarioslist:
        if usuario["email"] == usuariologado["email"]:
            usuarioslist.remove(usuario)
            salvar()
            print("\033[32mCONTA DELETADA COM SUCESSO!\n\033[m")
            return True
    return False

# Função para visualizar os dados do usuário
def ver_dados(usuariologado):
    print("\033[34mINFORMAÇÕES DO USUÁRIO:\n\033[m")
    print(f"Nome: {usuariologado['nome']}")
    print(f"Email: {usuariologado['email']}") 
    print(f"Senha: {utils.ver_senha_com_asterisco(usuariologado['senha'])}")
    print(f"Status: {usuariologado['status']}")
    print("\n\033[32mDigite 0 para voltar ao menu.\n\033[m")
    while True:
        opcao = input()
        if opcao.strip() == '0':
            utils.limpar()
            menus.menudeescolha(usuariologado)
            return
        else:
            print("\033[31mOpção inválida. Digite 0 para voltar ao menu.\n\033[m")