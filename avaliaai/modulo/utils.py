import usuarios as usuarios
import avaliacoes as avaliacoes
import os
import msvcrt

def limpar():
    os.system('cls')

def titulocadastro():
    titulocadastro = '\033[36mCADASTRO DE USUÁRIO\033[m'
    print(titulocadastro.center(50, '='),'\n\n')

def titulologin():
    titulologin = '\033[36mLOGIN DE USUÁRIO\033[m'
    print(titulologin.center(50, '='),'\n\n')  

def tituloavaliar():
    tituloavaliar = '\033[36mFAZER AVALIAÇÃO\033[m'
    print(tituloavaliar.center(50, '='),'\n\n')

def tituloavaliardisciplina():
    tituloavaldisc = '\033[36mAVALIAR DISCIPLINA\033[m'
    print(tituloavaldisc.center(50, '='),'\n\n')

def tituloavaliarprofessor():
    tituloavalprof = '\033[36mAVALIAR PROFESSOR\033[m'
    print(tituloavalprof.center(50, '='),'\n\n')

def titulogerenciardisciplina():
    titulogerenciadisc = '\033[36mGERENCIAR DISCIPLINA\033[m'
    print(titulogerenciadisc.center(50, '='),'\n\n')

def titulogerenciarprofessor():
    titulogerenciaprof = '\033[36mGERENCIAR PROFESSOR\033[m'
    print(titulogerenciaprof.center(50, '='),'\n\n')

def tituloadicionardisciplina():
    tituloadicionadisc = '\033[36mADICIONAR DISCIPLINA\033[m'
    print(tituloadicionadisc.center(50, '='),'\n\n')

def tituloadicionarprofessor():
    tituloadicionaprof = '\033[36mADICIONARAR PROFESSOR\033[m'
    print(tituloadicionaprof.center(50, '='),'\n\n')

def tituloremoverdisciplina():
    tituloremovedisc = '\033[36mREMOVER DISCIPLINA\033[m'
    print(tituloremovedisc.center(50, '='),'\n\n')

def tituloremoverprofessor():
    tituloremoveprof = '\033[36mREMOVER PROFESSOR\033[m'
    print(tituloremoveprof.center(50, '='),'\n\n')

def tituloeditardisciplina():
    tituloeditadisc = '\033[36mEDITAR DISCIPLINA\033[m'
    print(tituloeditadisc.center(50, '='),'\n\n')

def tituloeditarprofessor():
    tituloeditaprof = '\033[36mEDITAR PROFESSOR\033[m'
    print(tituloeditaprof.center(50, '='),'\n\n')

def titulotaxas():
    titulotaxas = '\033[36mTAXAS DE REPROVAÇÂO E APROVAÇÂO\033[m'
    print(titulotaxas.center(50, '='),'\n\n')

def validanome_real(nome_real):
    '''Valida o nome real do usuário de acordo com os critérios estabelecidos. 
    Recebe o parâmetro nome_real a e retorna True(válido) ou False (Inválido).'''
    contador = 0
    nomerealtrip = nome_real.strip()
   
    if not nomerealtrip:
        limpar()
        titulocadastro()
        print("\033[31mNOME REAL NÃO PODE SER VAZIO.\n\033[m")
        return False
    if sum(caracter.isalpha() for caracter in nomerealtrip) < 3:
        limpar()
        titulocadastro()
        print("\033[31mNOME REAL DEVE CONTER NO MÍNIMO 3 LETRAS.\n\033[m")
        return False
    if not 6 <=len(nomerealtrip) <= 50:
        limpar()
        titulocadastro()
        print("\033[31mNOME REAL DEVE CONTER ENTRE 6 E 50 CARACTERES.\n\033[m")
        return False
    if not all(caracter.isalpha() or caracter.isspace() for caracter in nomerealtrip):
        limpar()
        titulocadastro()
        print("\033[31mNOME REAL SÓ DEVE CONTER LETRAS E ESPAÇOS.\n\033[m")
        return False
    if '  ' in nomerealtrip:
        limpar()
        titulocadastro()
        print("\033[31mNOME REAL NÃO DEVE CONTER ESPAÇOS DUPLOS.\n\033[m")
        return False
    return True
def validanome(nome):
    '''Valida o nome do usuário de acordo com os critérios estabelecidos. 
    Recebe o parâmetro nome a e retorna True(válido) ou False (Inválido).'''
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
    '''Valida o email do usuário de acordo com os critérios estabelecidos. 
    Recebe o parâmetro nome a e retorna True(válido) ou False (Inválido).'''
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
    acentos = set('áéíóúãõâêîôûàèìòùäëïöü')
    if any(caracter in acentos for caracter in emailtrip):
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
        print("\033[31mE-MAIL DEVE CONTER APENAS UM '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') < 1:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER '.' ENTRE NOME E SOBRENOME.\n\033[m")
        return False
    
    nomeparte1, nomeparte2 = nome.split('.')

    if not sum(caracter.isalpha() for caracter in nomeparte1) >= 2 or not sum(caracter.isalpha() for caracter in nomeparte2) >= 2:
        limpar()
        titulocadastro()
        print("\033[31mE-MAIL DEVE CONTER PELO MENOS 2 LETRAS ANTES E DEPOIS DO '.'.\n\033[m")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario.email == email:
            limpar()
            titulocadastro()
            print("\033[31mJÁ EXISTE UM CADASTRO COM ESSE E-MAIL.\n\033[m")
            return False

   
    return True
       
def validasenha(senha):
    '''Valida a senha do usuário de acordo com os critérios estabelecidos. 
    Recebe o parâmetro nome a e retorna True(válido) ou False (Inválido).'''
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

def validanome_editar(novo_nome):
    '''Função para validar o novo nome do usuário durante a edição,
    recebe o novo nome como parâmetro de entrada e retorna True(válido) ou False (Inválido).'''
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

def validaemail_editar(novo_email):
    '''Função para validar o novo email do usuário durante a edição,
    recebe o novo email como parâmetro de entrada e retorna True(válido) ou False'''
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
    acentos = set('áéíóúãõâêîôûàèìòùäëïöü')
    if any(caracter in acentos for caracter in emailtrip):
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
        print("\033[31mE-MAIL DEVE CONTER APENAS UM '.' ANTES DO '@'.\n\033[m")
        return False
    if nome.count('.') < 1:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER '.' ENTRE NOME E SOBRENOME.\n\033[m")
        return False
    
    nomeparte1, nomeparte2 = nome.split('.')

    if not sum(caracter.isalpha() for caracter in nomeparte1) >= 2 or not sum(caracter.isalpha() for caracter in nomeparte2) >= 2:
        limpar()
        tituloeditar = '\033[36mEDITAR EMAIL\033[m'
        print(tituloeditar.center(50, '='),'\n\n')
        print("\033[31mE-MAIL DEVE CONTER PELO MENOS 2 LETRAS ANTES E DEPOIS DO '.'.\n\033[m")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario.email == novo_email:
            limpar()
            tituloeditar = '\033[36mEDITAR EMAIL\033[m'
            print(tituloeditar.center(50, '='),'\n\n')
            print("\033[31mJÁ EXISTE UM CADASTRO COM ESSE E-MAIL.\n\033[m")
            return False
        
    return True

def validasenha_editar(nova_senha):
    '''Função para validar a nova senha do usuário durante a edição,
    recebe a nova senha como parâmetro de entrada e retorna True(válido) ou False(Inválido).'''
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

def senha_com_asterisco():
    '''Função que mostra asteríscos ao digitar a senha, 
    não tem parâmetros de entrada e retorna a senha.'''
    senha = ""
    print("", end="", flush=True)

    while True:
        tecla = msvcrt.getch()

        if tecla == b'\r':  # Enter
            print()
            break

        elif tecla == b'\x08':  # Backspace
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)

        elif tecla in (b'\x00', b'\xe0'):  
            msvcrt.getch()  # ignora teclas especiais (setas, etc.)

        else:
            try:
                char = tecla.decode("utf-8")
            except:
                continue  # ignora caracteres inválidos

            senha += char
            print("*", end="", flush=True)

    return senha

def ver_senha_com_asterisco(senha):
    '''Função para exibir a senha do usuário com asteriscos,
    recebe a senha como parâmetro de entrada e retorna a senha com asteriscos.'''
    return "*" * len(senha)