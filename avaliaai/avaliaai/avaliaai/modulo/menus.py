import utils as utils
import usuarios as usuarios
import avaliacoes as avaliacoes

def menuinicial():
    '''Função para exibir o menu inicial do programa, 
    sem parâmetros de entrada eem retorno.'''
    tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
    print(tituloinicial.center(50,'='),'\n')
    print("\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )

def menuavaliar(usuariologado):
    '''Função para exibir o menu de avaliação de disciplinas e professores,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    while True:
        
        try:
            utils.limpar()
            utils.tituloavaliar()
            print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar\n')
            opcao = int(input(''))
            while opcao not in [0,1,2]:
                utils.limpar()
                utils.tituloavaliar()
                print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar')
                opcao = int(input(''))
            if opcao == 1:
                avaliacoes.avaliadisciplina(usuariologado)
            if opcao == 2:
                avaliacoes.avaliaprofessor(usuariologado)
            if opcao == 0:
                utils.limpar()
                return

        except ValueError:
            utils.limpar()           
            utils.tituloavaliar()
            print('Faça uma avaliação:\n\n[1]-Disciplina\n[2]-Professor\n[0]-Voltar\n')

def menudeescolha(usuariologado):
    '''Função para exibir o menu de escolha de ações do usuário logado,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    while True:
        print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
        "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            utils.limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:')
            continue

        if opcao == 1:
            menuchecaravaliacao()
        elif opcao == 2:
            menuavaliar(usuariologado)
        elif opcao == 3:
            menueditar(usuariologado)
        elif opcao == 4:
            usuarios.ver_dados(usuariologado)
        elif opcao == 5:
            menudeletar(usuariologado)
            if usuariologado not in usuarios.usuarioslist:
                return   
        elif opcao == 0:
            return
        else:
            utils.limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')

# Função para exibir o menu de edição de dados do usuário
def menueditar(usuariologado):
    while True:
        utils.limpar()
        tituloeditar = '\033[36mEDITAR DADOS\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("Selecione uma opção:\n\n[1]-Editar Nome\n[2]-Editar Email\n[3]-Editar Senha\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue

        # Opção válida
        if opcao == 1:
            while True:
                utils.limpar()
                novo_nome = input('Digite o novo nome ou 0 para cancelar:\n\n')
                if novo_nome.strip() == '0':
                    break
                if utils.validanome_editar(novo_nome):
                    usuarios.editar_nome(usuariologado, novo_nome)
                    break
                else:
                    print("\033[31mNOME INVÁLIDO! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
        elif opcao == 2:
            while True:
                utils.limpar()
                novo_email = input('Digite o novo email ou 0 para cancelar:\n\n')
                if novo_email.strip() == '0':
                    break
                if utils.validaemail_editar(novo_email):
                    usuarios.editar_email(usuariologado, novo_email)
                    break
                else:
                    print("\033[31mE-MAIL INVÁLIDO! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
        elif opcao == 3:
            while True:
                utils.limpar()
                print('Digite a senha atual ou 0 para cancelar:\n\n')
                senha_atual = utils.senha_com_asterisco().strip()
                if senha_atual.strip() == '0':
                    break
                if senha_atual != usuariologado["senha"]:
                    print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
                print('Digite a nova senha ou 0 para cancelar:\n\n')
                nova_senha = utils.senha_com_asterisco().strip() 
                if nova_senha.strip() == '0':
                    break
                print('Confirme a nova senha:\n\n')
                confirmar_senha = utils.senha_com_asterisco().strip()  
                if confirmar_senha != nova_senha:
                    print("\033[31mAS SENHAS NÃO COINCIDEM! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
                if utils.validasenha_editar(nova_senha):
                    usuarios.editar_senha(usuariologado, nova_senha)
                    break
                else:
                    print("\033[31mSENHA INVÁLIDA! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
        elif opcao == 0:
            utils.limpar()
            return
        else:
            print("\033[31mOPÇÃO INVÁLIDA! Escolha entre 0, 1, 2 ou 3.\033[m\n")
            input("Pressione Enter para continuar...")
            continue

# Função para exibir o menu de confirmação de exclusão de conta
def menudeletar(usuariologado):
    utils.limpar()
    titulodeletar = '\033[36mDELETAR CONTA\033[m'
    print(titulodeletar.center(50, '='),'\n\n')
    print("Tem certeza que deseja deletar sua conta?\n\n[1]-Sim\n[2]-Não")

    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            continue

        # Opção válida
        if opcao == 1:
            print('Digite a senha atual para confirmar ou 0 para cancelar:\n')
            senha_atual = utils.senha_com_asterisco().strip()
           
            if senha_atual == '0':
                utils.limpar()
                return
            if senha_atual != usuariologado["senha"]:
                print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                continue
            usuarios.deletar_conta(usuariologado)
            input("Pressione Enter para voltar ao menu...")
            utils.limpar()
            return
        elif opcao == 2:
            utils.limpar()
            return
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            continue
        
# Função para exibir o menu de checar avaliações de disiciplinas e professores
def menuchecaravaliacao():
    while True:
        utils.limpar()
        titulochecar = '\033[36mCHECAR AVALIAÇÕES\033[m'
        print(titulochecar.center(50, '='),'\n\n')
        print("Selecine uma opção:\n\n[1]-Checar Avaliações de Disciplinas\n[2]-Checar Avaliações de Professores\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue
        
        # Opção válida
        if opcao == 1:
            avaliacoes.checardisciplina()
        elif opcao == 2:
            avaliacoes.checarprofessor()
        elif opcao == 0:
            return
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue
