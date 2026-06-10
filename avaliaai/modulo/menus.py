import funcoes_admin
import utils as utils
import usuarios as usuarios
import avaliacoes as avaliacoes
import materiais as materiais
import calculo_taxas
from models.usuario import Usuario
from models.avaliacoes_disciplinas import Avaliacoes_disciplinas
from models.avaliacoes_professores import Avaliacoes_professores

def menu_inicial():
    '''Função para exibir o menu inicial do programa, 
    sem parâmetros de entrada e sem retorno.'''
    tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
    print(tituloinicial.center(50,'='),'\n')
    print("\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )

def menu_avaliar(usuariologado):
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
def menu_de_escolha_admin(usuariologado):
    '''Função para exibir o menu de escolha de ações do usuário logado com status admin,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    while True:
        tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
        print(tituloescolha.center(50, '='),'\n\n')
        print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
        "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Nível de dificuldade do período\n[9]-Gerenciar Disciplinas\n[10]-Gerenciar Professores\n[0]-Voltar")
        while True:
            try:
                opcao = int(input('Digite a opção desejada: '))
                if opcao in [0,1,2,3,4,5,6,7,9,10]:
                    break
                else:
                    utils.limpar()
                    tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
                    print(tituloescolha.center(50, '='),'\n\n')
                    print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')
                    print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
                    "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Nível de dificuldade do período\n[9]-Gerenciar Disciplinas\n[10]-Gerenciar Professor\n[0]-Voltar")
            except ValueError:
                utils.limpar()
                tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
                print(tituloescolha.center(50, '='),'\n\n')
                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')
                print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
                "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Nível de dificuldade do período\n[9]-Gerenciar Disciplinas\n[10]-Gerenciar Professores\n[0]-Voltar")

        if opcao == 1:
            menuchecaravaliacao()
        elif opcao == 2:
            menu_avaliar(usuariologado)
        elif opcao == 3:
            menueditar(usuariologado)
        elif opcao == 4:
            usuariologado.ver_dados()
            #usuarios.ver_dados(usuariologado)
        elif opcao == 5:
            menudeletar(usuariologado)
            if usuariologado not in usuarios.usuarioslist:
                utils.limpar()
                menu_inicial()
                return
        elif opcao == 6:
            menu_materiaisaula()
        elif opcao == 7:
            calculo_taxas.indices()
        elif opcao == 8:
            menu_dificuldade_periodo()
        elif opcao == 9:
            menu_gerenciar_disciplinas()
        elif opcao == 10:
            menu_gerenciar_professores()
        elif opcao == 0:
            utils.limpar()
            menu_inicial()
            return
        else:
            utils.limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')

def menu_de_escolha_usuario(usuariologado):
    '''Função para exibir o menu de escolha de ações do usuário logado,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    while True:
        tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
        print(tituloescolha.center(50, '='),'\n\n')
        print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
        "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Nível de Dificuldade do Período\n[0]-Voltar")
        while True:
            try:
                opcao = int(input('Digite a opção desejada: '))
                if opcao in [0,1,2,3,4,5,6,7,8]:
                    break
                else:
                    utils.limpar()
                    tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
                    print(tituloescolha.center(50, '='),'\n\n')
                    print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')
                    print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
                    "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Dificuldade por Período\n[0]-Voltar")
            except ValueError:
                utils.limpar()
                tituloescolha = '\033[36mMENU DE ESCOLHA\033[m'
                print(tituloescolha.center(50, '='),'\n\n')
                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')
                print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
                "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[6]-Materiais de Aula\n[7]-Índice de Reprovação e Aprovação\n[8]-Dificuldade por Período\n[0]-Voltar")

        if opcao == 1:
            menuchecaravaliacao()
        elif opcao == 2:
            menu_avaliar(usuariologado)
        elif opcao == 3:
            menueditar(usuariologado)
        elif opcao == 4:
            usuariologado.ver_dados()
            #usuarios.ver_dados(usuariologado)
        elif opcao == 5:
            menudeletar(usuariologado)
            if usuariologado not in usuarios.usuarioslist:
                utils.limpar()
                menu_inicial()
                return
        elif opcao == 6:
            menu_materiaisaula()
        elif opcao == 7:
            calculo_taxas.indices()
        elif opcao == 8:
            menu_dificuldade_periodo()
        elif opcao == 0:
            utils.limpar()
            menu_inicial()
            return
        else:
            utils.limpar()
            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n\nDIGITE UM NÙMERO DO MENU:')

def menueditar(usuariologado):
    '''Função para exibir o menu de edição de dados do usuário,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
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
                    usuariologado.editar_nome(novo_nome)
                   # usuarios.editar_nome(usuariologado, novo_nome)
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
                    
                    usuariologado.editar_email(novo_email)
                    #usuarios.editar_email(usuariologado, novo_email)
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
                if senha_atual != usuariologado.senha:
                    print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                    input("Pressione Enter para continuar...")
                    continue
                while True:
                    print('Digite a nova senha ou 0 para cancelar:\n\n')
                    nova_senha = utils.senha_com_asterisco().strip() 
                    if nova_senha.strip() == '0':
                        break
                    if not utils.validasenha_editar(nova_senha):
                        print("\033[31mSENHA INVÁLIDA! Tente novamente.\n\033[m")
                        input("Pressione Enter para continuar...")
                        continue
                    
                    print('Confirme a nova senha:\n\n')
                    confirmar_senha = utils.senha_com_asterisco().strip()  
                    if confirmar_senha != nova_senha:
                        print("\033[31mAS SENHAS NÃO COINCIDEM! Tente novamente.\n\033[m")
                        input("Pressione Enter para continuar...")
                        continue
                    if utils.validasenha_editar(nova_senha):
                        usuariologado.editar_senha(nova_senha)
                        #usuarios.editar_senha(usuariologado, nova_senha)
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

def menudeletar(usuariologado):
    '''Função para exibir o menu de confirmação de exclusão de conta,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    while True:
        utils.limpar()
        titulodeletar = '\033[36mDELETAR CONTA\033[m'
        print(titulodeletar.center(50, '='),'\n\n')
        print("Tem certeza que deseja deletar sua conta?\n\n[1]-Sim\n[2]-Não")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue

        # Opção válida
        if opcao == 1:
            while True:
                print('Digite a senha atual para confirmar ou 0 para cancelar:\n')
                senha_atual = utils.senha_com_asterisco().strip()
            
                if senha_atual == '0':
                    utils.limpar()
                    break
                if senha_atual != usuariologado.senha:
                    print("\033[31mSENHA ATUAL INCORRETA! Tente novamente.\n\033[m")
                    continue
                usuariologado.deletar_conta()
                #usuarios.deletar_conta(usuariologado)
                input("Pressione Enter para voltar ao menu...")
                utils.limpar()
                return
        elif opcao == 2:
            utils.limpar()
            return
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue
        
def menuchecaravaliacao():
    '''Função para exibir o menu de checar avaliações de disciplinas e professores,
     sem parâmetros de entrada e sem retorno.'''
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
            utils.limpar()
            return
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            input("Pressione Enter para continuar...")
            continue
def menu_gerenciar_disciplinas():
    utils.limpar()
    utils.titulogerenciardisciplina()
    while True:
        
        print("[1]-Adicionar Disciplina\n[2]-Remover Disciplina\n[3]-Editar Disciplina\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao in [0,1,2,3]:
                utils.limpar()
                if opcao == 1:
                    funcoes_admin.adicionar_disciplina()
                    utils.titulogerenciardisciplina()
                if opcao == 2:
                    funcoes_admin.remover_disciplina()
                    utils.titulogerenciardisciplina()
                if opcao == 3:
                    funcoes_admin.editar_disciplina()
                    utils.titulogerenciardisciplina()
                if opcao == 0:
                    utils.limpar()
                    return
            else:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                utils.titulogerenciardisciplina()
                print("Digite um número do menu:\n")
        except ValueError:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            utils.titulogerenciardisciplina()
            print("Digite um número do menu:\n")

def menu_gerenciar_professores():
    utils.limpar()
    utils.titulogerenciarprofessor()
    while True:
        print("\n\n[1]-Adicionar Professor\n[2]-Remover Professor\n[3]-Editar Professor\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao in [0,1,2,3]:
                utils.limpar()
                if opcao == 1:
                    funcoes_admin.adicionar_professor()
                    utils.titulogerenciarprofessor()
                if opcao == 2:
                    funcoes_admin.remover_professor()
                    utils.titulogerenciarprofessor()
                if opcao == 3:
                    funcoes_admin.editar_professor()
                    utils.titulogerenciarprofessor()
                if opcao == 0:
                    utils.limpar()
                    return
            else:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                utils.titulogerenciarprofessor()
                print("Digite um número do menu:\n")
        except ValueError:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            utils.titulogerenciarprofessor()
            print("Digite um número do menu:\n")

def menu_materiaisaula():
    '''Função para exibir o menu de materiais de aula'''
    while True:
        utils.limpar()
        titulomateriais = '\033[36mMATERIAIS DE AULA\033[m'
        print(titulomateriais.center(50, '='),'\n\n')
        print("Selecione uma opção:\n\n[1]-Realizar upload de materiais\n[2]-Realizar download de materiais\n[3]-Ver Materiais\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

        if opcao == 1:
            materiais.Materiais.upload()
        elif opcao == 2:
            materiais.Materiais.download()
        elif opcao == 3:
            materiais.Materiais.vermateriais()
        elif opcao == 0:
            utils.limpar()
            return
        else:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

def menu_dificuldade_periodo():
    '''Função para exibir o menu de nível dedificuldade do período'''
    while True:
        utils.limpar()
        titulodificuldade = '\033[36mNÍVEL DE DIFICULDADE DO PERÍODO\033[m'
        print(titulodificuldade.center(50, '='),'\n\n')
        print("Selecione uma opção:\n\n[1]-Ver dificuldade do período\n[2]-Adicionar disciplina\n[0]-Voltar")
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            continue

        if opcao == 1:
            avaliacoes.DificuldadePeriodo.dificuldadeperiodo()
        elif opcao == 2:
            avaliacoes.DificuldadePeriodo.adicionardisciplina()
        elif opcao == 0:
            utils.limpar()
            return
        else:
            utils.limpar()
            print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")