import usuarios
import os

def limpar():
    os.system('cls')

def menuinicial():
    print("\n\033[36mBem-vindo(a) ao AvaliAí!\033[m""\nSelecione uma opção:\n\n[1]-Cadastro\n[2]-Login\n[0]-Sair\n" )


def validanome(nome):
    nometrip = nome.strip()
   
    if not nometrip:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome não pode ser vazio.\n\033[m")
        return False
    if sum(caracter.isalpha() for caracter in nometrip) < 3:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome deve conter no mínimo 3 letras.\n\033[m")
        return False
    if not 6 <=len(nometrip) <= 20:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome deve conter entre 6 e 20 caracteres.\n\033[m")
        return False
    if ' ' in nometrip:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome não pode conter espaços.\n\033[m")
        return False
    if nometrip[0].isdigit():
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome não pode começar com um número.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter in "_.-" for caracter in nometrip):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO nome não deve ter caracteres especiais além de '-', '_' e '.'.\n\033[m")
        return False
    
    
    return True

def validaemail(email):
    emailtrip = email.strip()
   
    if not emailtrip:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email não pode ser vazio.\n\033[m")
        return False
    if emailtrip.count('@') != 1:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email deve conter domínio '@ufrpe.br'.\n\033[m")
        return False
   
    nome, dominio = emailtrip.split('@')
   
    
    if not dominio == 'ufrpe.br':
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email deve conter dominio '@ufrpe.br'.\n\033[m")
        return False
    if not nome:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email deve conter algo antes do '@'.\n\033[m")
        return False
    if nome.isdigit():
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email não pode conter apenas números antes do '@'.\n\033[m")
        return False
    if " " in nome:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email não pode conter espaços vazios.\n\033[m")
        return False
    if not all(caracter.isalnum() or caracter == '.' for caracter in nome):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email só deve conter caracteres alfanuméricos ou o caracterer '.' antes do '@'.\n\033[m")
        return False
    if nome[0] == '.' or nome[-1] == '.':
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email não pode começar ou terminar com '.' antes do '@'.\n\033[m")
        return False
    if nome.count('.') > 1:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email não pode conter mais que um '.' antes do '@'.\n\033[m")
        return False
    if nome.count('.') < 1:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email deve conter '.' entre nome e sobrenome.\n\033[m")
        return False
    
    nomeparte1, nomeparte2 = nome.split('.')

    if not sum(caracter.isalpha() for caracter in nomeparte1) >= 2 or not sum(caracter.isalpha() for caracter in nomeparte2) >= 2:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mO email deve conter no mínimo 2 letras antes e depois do '.'.\n\033[m")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario['email'].lower() == email.lower():
            limpar()
            print(usuarios.titulocadastro.center(50, '='),'\n')
            print("\033[31mEmail já existe. Por favor, escolha outro email.\n\033[m")
            return False

   
    return True
       
def validasenha(senha):
    senhatrip = senha.strip()
   
    if not senhatrip:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha não pode ser vazia.\n\033[m")
        return False
    if len(senhatrip) < 8:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter no mínimo 8 caracteres.\n\033[m")
        return False
    if len(senhatrip) > 12:
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter no máximo 12 caracteres.\n\033[m")
        return False
    if not any(caracter.isupper() for caracter in senhatrip):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter pelo menos uma letra maiúscula.\n\033[m")
        return False
    if not any(caracter.islower() for caracter in senhatrip):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter pelo menos uma letra minúscula.\n\033[m")
        return False
    if  all(caracter.isalnum() for caracter in senhatrip):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter pelo menos um caracter especial.\n\033[m")
        return False
    if not any(caracter.isdigit() for caracter in senhatrip):
        limpar()
        print(usuarios.titulocadastro.center(50, '='),'\n')
        print("\033[31mA senha deve conter pelo menos um número.\n\033[m")
        return False
    
   
    return True
