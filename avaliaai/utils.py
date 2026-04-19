import avaliaai.usuarios as usuarios
import os

def limpar():
    os.system('cls')

def menuinicial():
    tituloinicial = '\033[36mBEM-VINDO(A) AO AVALIAÍ!\033[m'
    print(tituloinicial.center(50,'='),'\n')
    print("\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )

def menudeescolha():
    print("Menu de Escolha:\n\n[1]-Checar Avaliações\n[2]-Fazer Avaliações\n"
    "[3]-Editar Dados\n[4]-Ver Dados\n[5]-Deletar Conta\n[0]-Voltar")
    while True:
        try:
            opcao = int(input(''))
            while opcao<0 or opcao>5:
                limpar()
                menudeescolha()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
                opcao = int(input(""))
            if opcao == 1:
                    print('')
            if opcao == 2:
                    print('')
            if opcao == 3:
                    print('')
            if opcao == 4:
                    print('')
            if opcao == 5:
                    print('')    
            if opcao == 0:limpar();menuinicial();break
            
        except ValueError:
            print('\033[31mOPÇÃO INVÁLIDA!\n\nDIGITE UM NÙMERO DO MENU:')



def titulocadastro():
    titulocadastro = '\033[36mCADASTRO DE USUÁRIO\033[m'
    print(titulocadastro.center(50, '='),'\n\n')

def titulologin():
    titulologin = '\033[36mLOGIN DE USUÁRIO\033[m'
    print(titulologin.center(50, '='),'\n\n')  



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
