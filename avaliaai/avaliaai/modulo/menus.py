import utils as utils
import usuarios as usuarios
import avaliacoes as avaliacoes




def menuinicial():
    tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
    print(tituloinicial.center(50,'='),'\n')
    print("\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )

def menuavaliar(usuariologado):
    
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
            print('\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:')

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
            utils.limpar()
            menueditar(usuariologado)
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            opcao = int(input('Digite a opção desejada: '))
            continue

        # Opção válida
        if opcao == 1:
            novo_nome = input('Digite o novo nome ou 0 para cancelar:\n\n')
            if novo_nome.strip() == '0':
                utils.limpar()
                return
            if utils.validanome_editar(novo_nome):
                usuarios.editar_nome(usuariologado, novo_nome)
            else:
                print("\033[31mNOME INVÁLIDO! Tente novamente.\n\033[m")
        elif opcao == 2:
            novo_email = input('Digite o novo email ou 0 para cancelar:\n\n')
            if novo_email.strip() == '0':
                utils.limpar()
                return
            if utils.validaemail_editar(novo_email):
                usuarios.editar_email(usuariologado, novo_email)
            else:
                print("\033[31mE-MAIL INVÁLIDO! Tente novamente.\n\033[m")
        elif opcao == 3:
            
            print('Digite a senha atual ou 0 para cancelar:\n')
            senha_atual = utils.senha_com_asterisco().strip()
            if senha_atual == '0':
                utils.limpar()
                return
            if senha_atual != usuariologado["senha"]:
                print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                continue
            print('Digite a nova senha ou 0 para cancelar:\n')
            nova_senha = utils.senha_com_asterisco().strip() 
            if nova_senha == '0':
                utils.limpar()
                return
            print('Confirme a nova senha:\n\n')
            confirmar_senha = utils.senha_com_asterisco().strip()  
            if confirmar_senha != nova_senha:
                print("\033[31mAS SENHAS NÃO COINCIDEM! Tente novamente.\n\033[m")
                continue
            if utils.validasenha_editar(nova_senha):
                usuarios.editar_senha(usuariologado, nova_senha)
            else:
                print("\033[31mSENHA INVÁLIDA! Tente novamente.\n\033[m")
        elif opcao == 0:
            utils.limpar()
            return
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
            print('Digite a senha atual para confirmar ou 0 para cancelar:\n')
            senha_atual = utils.senha_com_asterisco().strip()
           
            if senha_atual == '0':
                utils.limpar()
                return
            if senha_atual != usuariologado["senha"]:
                print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                continue
            usuarios.deletar_conta(usuariologado)
            utils.limpar()
            print("\033[32mCONTA DELETADA COM SUCESSO!\n\033[m")
            return
        elif opcao == 2:
            utils.limpar()
            return
        
# Função para exibir o menu de checar avaliações de disiciplinas e professores
def menuchecaravaliacao():
    while True:
        titulochecar = '\033[36mCHECAR AVALIAÇÕES\033[m'
        print(titulochecar.center(50, '='),'\n\n')
        print("Selecine uma opção:\n\n[1]-Checar Avaliações de Disciplinas\n[2]-Checar Avaliações de Professores\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:\n\033[m")
            opcao = int(input("Digite a opção desejada:"))
            continue
        if opcao not in [0, 1, 2]:
            utils.limpar()
            menuchecaravaliacao()
            print("\033[31mOPÇÃO INVÁLIDA!\n\033[m")
            opcao = int(input("Digite a opção desejada:"))
            continue
        
        # Opção válida
        if opcao == 1:
            avaliacoes.checardisciplina()
        if opcao == 2:
            print('')
        if opcao == 0:
            return
