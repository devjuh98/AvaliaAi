import getpass
import modulo.usuarios as usuarios
import modulo.avaliacoes
import os

def limpar():
    os.system('cls')

def menuinicial():
    tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
    print(tituloinicial.center(50,'='),'\n')
    print("\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )

def menuavaliar():
    
    while True:
        
        try:
            limpar()
            tituloavaliar()
            print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar\n')
            opcao = int(input(''))
            while opcao not in [0,1,2]:
                limpar()
                tituloavaliar()
                print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar')
                opcao = int(input(''))
            if opcao == 1:
                modulo.avaliacoes.avaliadisciplina()
            if opcao == 2:
                print('')
            if opcao == 0:
                return

        except ValueError:
            limpar()           
            tituloavaliar()
            print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar\n')
    

def menudeescolha(usuariologado):
    
    while True:
        print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
        "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:')
            continue

        if opcao == 1:
            print('')
        elif opcao == 2:
            menuavaliar()
        elif opcao == 3:
            menueditar(usuariologado)
        elif opcao == 4:
            usuarios.ver_dados(usuariologado)
        elif opcao == 5:
            menudeletar(usuariologado)   
        elif opcao == 0:
            return
        else:
            limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:')
        


def titulocadastro():
    titulocadastro = '\033[36mCADASTRO DE USUÁRIO\033[m'
    print(titulocadastro.center(50, '='),'\n\n')

def titulologin():
    titulologin = '\033[36mLOGIN DE USUÁRIO\033[m'
    print(titulologin.center(50, '='),'\n\n')  

def tituloavaliar():
    tituloavaliar = '\033[36mFAZER AVALIAÇÃO\033[m'
    print(tituloavaliar.center(50, '='),'\n\n')

def tituloavaldisc():
    tituloavaldisc = '\033[36mAVALIAR DISCIPLINA\033[m'
    print(tituloavaldisc.center(50, '='),'\n\n')

def validanome(nome):
    nometrip = nome.strip()
   
    if not nometrip:
        limpar()
        titulocadastro()
        print("\033[31mNOME NÃO PODE SER VAZIO.\n\033[m")
        return False
    if sum(caracter.isalpha() for caracter in nometrip) < 3:
        limpar()
        titulocadastro()
        print("\033[31mNOME DEVE CONTER NO MÍNIMO 3 LETRAS.\n\033[m")
        return False
    if not 6 <=len(nometrip) <= 20:
        limpar()
        titulocadastro()
        print("\033[31mNOME DEVE CONTER ENTRE 6 E 20 CARACTERES.\n\033[m")
        return False
    if ' ' in nometrip:
        limpar()
        titulocadastro()
        print("\033[31mNOME NÃO DEVE CONTER ESPAÇOS.\n\033[m")
        return False
    if nometrip[0].isdigit():
        limpar()
        titulocadastro()
        print("\033[31mNOME NÃO DEVE COMEÇAR COM NÚMERO.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter in "_.-" for caracter in nometrip):
        limpar()
        titulocadastro()
        print("\033[31mNOME NÃO DEVE TER CARACTERES ESPECIAIS ALÉM DE '-', '_' E '.'.\n\033[m")
        return False
    
    
    return True

def validaemail(email):
    emailtrip = email.strip().lower()
   
    if not emailtrip:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL NÃO DEVE SER VAZIO.\n\033[m")
        return False
    if emailtrip.count('@') != 1:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER UM ÚNICO '@'.\n\033[m")
        return False
   
    nome, dominio = emailtrip.split('@')
   
    
    if not dominio == 'ufrpe.br':
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER O DOMÍNIO '@ufrpe.br'.\n\033[m")
        return False
    if not nome:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER ALGO ANTES DO '@'.\n\033[m")
        return False
    if nome.isdigit():
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL NÃO DEVE CONTER APENAS NÚMEROS ANTES DO '@'.\n\033[m")
        return False
    if " " in nome:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL NÃO DEVE CONTER ESPAÇOS VAZIOS.\n\033[m")
        return False
    if any(caracter in ['áéíóúãõâêîôûàèìòùäëïöü'] for caracter in emailtrip):
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL NÃO DEVE CONTER ACENTO.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter == '.' for caracter in nome):
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL SÓ DEVE CONTER CARACTERES ALFANUMÉRICOS OU O CARACTER '.' ANTES DO '@'.\n\033[m")
        return False
    if nome[0] == '.' or nome[-1] == '.':
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL NÃO DEVE COMEÇAR OU TERMINAR COM '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') > 1:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER APENAS  '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') < 1:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER APENAS '.' ENTRE NOME E SOBRENOME.\n\033[m")
        return False
    
    nomeparte1, nomeparte2 = nome.split('.')

    if not sum(caracter.isalpha() for caracter in nomeparte1) >= 2 or not sum(caracter.isalpha() for caracter in nomeparte2) >= 2:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER PELO MENOS 2 LETRAS ANTES E DEPOIS DO '.'.\n\033[m")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario['email'] == email:
            limpar()
            titulocadastro()
            print("\033[31mJÁ EXISTE UM CADASTRO COM ESSE E-MAIL.\n\033[m")
            return False

   
    return True
       
def validasenha(senha):
    senhatrip = senha.strip()
   
    if not senhatrip:
        limpar()
        titulocadastro()
        print("\033[31mSENHA NÃO PODE SER VAZIA.\n\033[m")
        return False
    if len(senhatrip) < 8:
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER NO MÍNIMO 8 CARACTERES.\n\033[m")
        return False
    if len(senhatrip) > 12:
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER NO MÁXIMO 12 CARACTERES.\n\033[m")
        return False
    if not any(caracter.isupper() for caracter in senhatrip):
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER PELO MENOS 1 LETRA MAIÚSCULA.\n\033[m")
        return False
    if not any(caracter.islower() for caracter in senhatrip):
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER PELO MENOS 1 LETRA MINÚSCULA.\n\033[m")
        return False
    if  all(caracter.isalnum() for caracter in senhatrip):
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER PELO MENOS UM CARACTER ESPECIAL.\n\033[m")
        return False
    if not any(caracter.isdigit() for caracter in senhatrip):
        limpar()
        titulocadastro()
        print("\033[31mSENHA DEVE CONTER PELO MENOS UM NÚMERO.\n\033[m")
        return False
    
   
    return True

# Função para exibir o menu de edição de dados do usuário
def menueditar(usuariologado):
    while True:
        tituloeditar = '\033[36mEDITAR DADOS\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("Selecione uma opção:\n\n[1]-Editar Nome\n[2]-Editar Email\n[3]-Editar Senha\n[0]-Voltar")
        try:
             opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            opcao = int(input('Digite a opção desejada: '))
            continue
        if opcao not in [0, 1, 2, 3]:
            limpar()
            menueditar(usuariologado)
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            opcao = int(input('Digite a opção desejada: '))
            continue

        # Opção válida
        if opcao == 1:
            novo_nome = input('Digite o novo nome ou 0 para cancelar:\n\n')
            if novo_nome.strip() == '0':
                limpar()
                return
            if validanome_editar(novo_nome):
                usuarios.editar_nome(usuariologado, novo_nome)
            else:
                print("\033[31mNOME INVÁLIDO! Tente novamente.\n\033[m")
        elif opcao == 2:
            novo_email = input('Digite o novo email ou 0 para cancelar:\n\n')
            if novo_email.strip() == '0':
                limpar()
                return
            if validaemail_editar(novo_email):
                usuarios.editar_email(usuariologado, novo_email)
            else:
                print("\033[31mE-MAIL INVÁLIDO! Tente novamente.\n\033[m")
        elif opcao == 3:
            senha_atual = input('Digite a senha atual ou 0 para cancelar:\n\n')
            if senha_atual.strip() == '0':
                limpar()
                return
            if senha_atual != usuariologado["senha"]:
                print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                continue
            nova_senha = input('Digite a nova senha ou 0 para cancelar:\n\n')
            if nova_senha.strip() == '0':
                limpar()
                return
            confirmar_senha = input('Confirme a nova senha:\n\n')
            if confirmar_senha != nova_senha:
                print("\033[31mAS SENHAS NÃO COINCIDEM! Tente novamente.\n\033[m")
                continue
            if validasenha_editar(nova_senha):
                usuarios.editar_senha(usuariologado, nova_senha)
            else:
                print("\033[31mSENHA INVÁLIDA! Tente novamente.\n\033[m")
        elif opcao == 0:
            limpar()
            return

# Função para validar o novo nome do usuário durante a edição
def validanome_editar(novo_nome):
    nometrip = novo_nome.strip()
   
    if not nometrip:
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME NÃO PODE SER VAZIO.\n\033[m")
        return False
    if sum(caracter.isalpha() for caracter in nometrip) < 3:
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME DEVE CONTER NO MÍNIMO 3 LETRAS.\n\033[m")
        return False
    if not 6 <=len(nometrip) <= 20:
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME DEVE CONTER ENTRE 6 E 20 CARACTERES.\n\033[m")
        return False
    if ' ' in nometrip:
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME NÃO DEVE CONTER ESPAÇOS.\n\033[m")
        return False
    if nometrip[0].isdigit():
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME NÃO DEVE COMEÇAR COM NÚMERO.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter in "_.-" for caracter in nometrip):
        limpar()
        tituloeditar = '\033[36mEDITAR NOME\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mNOME NÃO DEVE TER CARACTERES ESPECIAIS ALÉM DE '-', '_' E '.'.\n\033[m")
        return False
    
    
    return True

# Função para validar o novo email do usuário durante a edição
def validaemail_editar(novo_email):
    emailtrip = novo_email.strip().lower()
   
    if not emailtrip:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL NÃO DEVE SER VAZIO.\n\033[m")
        return False
    if emailtrip.count('@') != 1:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER UM ÚNICO '@'.\n\033[m")
        return False
   
    nome, dominio = emailtrip.split('@')
   
    
    if not dominio == 'ufrpe.br':
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER O DOMÍNIO '@ufrpe.br'.\n\033[m")
        return False
    if not nome:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER ALGO ANTES DO '@'.\n\033[m")
        return False
    if nome.isdigit():
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL NÃO DEVE CONTER APENAS NÚMEROS ANTES DO '@'.\n\033[m")
        return False
    if " " in nome:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL NÃO DEVE CONTER ESPAÇOS VAZIOS.\n\033[m")
        return False
    if any(caracter in ['áéíóúãõâêîôûàèìòùäëïöü'] for caracter in emailtrip):
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL NÃO DEVE CONTER ACENTO.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter == '.' for caracter in nome):
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL SÓ DEVE CONTER CARACTERES ALFANUMÉRICOS OU O CARACTER '.' ANTES DO '@'.\n\033[m")
        return False
    if nome[0] == '.' or nome[-1] == '.':
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL NÃO DEVE COMEÇAR OU TERMINAR COM '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') > 1:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER APENAS  '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') < 1:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER APENAS '.' ENTRE NOME E SOBRENOME.\n\033[m")
        return False
    
    nomeparte1, nomeparte2 = nome.split('.')

    if not sum(caracter.isalpha() for caracter in nomeparte1) >= 2 or not sum(caracter.isalpha() for caracter in nomeparte2) >= 2:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER PELO MENOS 2 LETRAS ANTES E DEPOIS DO '.'.\n\033[m")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario['email'] == novo_email:
            limpar()
            tituloeditar = '\033[36mEDITAR EMAIL\033[m'
            print(tituloeditar.center(50, '='),'\n\n')
            print("\033[31mJÁ EXISTE UM CADASTRO COM ESSE E-MAIL.\n\033[m")
            return False
        
    return True

# Função para validar a nova senha do usuário durante a edição
def validasenha_editar(nova_senha):
    senhatrip = nova_senha.strip()
   
    if not senhatrip:
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA NÃO PODE SER VAZIA.\n\033[m")
        return False
    if len(senhatrip) < 8:
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER NO MÍNIMO 8 CARACTERES.\n\033[m")
        return False
    if len(senhatrip) > 12:
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER NO MÁXIMO 12 CARACTERES.\n\033[m")
        return False
    if not any(caracter.isupper() for caracter in senhatrip):
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER PELO MENOS 1 LETRA MAIÚSCULA.\n\033[m")
        return False
    if not any(caracter.islower() for caracter in senhatrip):
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER PELO MENOS 1 LETRA MINÚSCULA.\n\033[m")
        return False
    if  all(caracter.isalnum() for caracter in senhatrip):
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER PELO MENOS UM CARACTER ESPECIAL.\n\033[m")
        return False
    if not any(caracter.isdigit() for caracter in senhatrip):
        limpar()
        tituloeditar = '\033[36mEDITAR SENHA\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mSENHA DEVE CONTER PELO MENOS UM NÚMERO.\n\033[m")
        return False
    
    return True

# Função para exibir o menu de confirmação de exclusão de conta
def menudeletar(usuariologado):
    while True:
        titulodeletar = '\033[36mDELETAR CONTA\033[m'
        print(titulodeletar.center(50, '='),'\n\n')
        print("Tem certeza que deseja deletar sua conta?\n\n[1]-Sim\n[2]-Não")
        try:
             opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            opcao = int(input('Digite a opção desejada: '))
            continue
        if opcao not in [1, 2]:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            opcao = int(input('Digite a opção desejada: '))
            continue

        # Opção válida
        if opcao == 1:
            senha_atual = input('Digite a senha atual para confirmar ou 0 para cancelar:\n\n')
            if senha_atual.strip() == '0':
                limpar()
                return
            if senha_atual != usuariologado["senha"]:
                print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                continue
            usuarios.deletar_conta(usuariologado)
            limpar()
            print("\033[32mCONTA DELETADA COM SUCESSO!\n\033[m")
            return
        elif opcao == 2:
            limpar()
            return