import usuarios
import os

def limpar():
    os.system('cls')

def menuinicial():
    print("Escolha a opção que deseja:\n1-Cadastro\n2-Login\n0-Sair\n" )

aluno = {'nome': '','email': '','senha': ''}
alunos = []

def validanome(nome):
    nometrip = nome.strip()
   
    if not nometrip:
        limpar()
        print("O nome não pode ser vazio.\n")
        return False
    if sum(caracter.isalpha() for caracter in nometrip) < 3:
        limpar()
        print("O nome deve conter no mínimo 3 letras.\n")
        return False
    if not 6 <=len(nometrip) <= 20:
        limpar()
        print("O nome deve conter entre 6 e 20 caracteres.\n")
        return False
    if ' ' in nometrip:
        limpar()
        print("O nome não pode conter espaços.\n")
        return False
    if nometrip.isdigit():
        limpar()
        print("O nome não pode conter apenas números.\n")
        return False
    if nometrip[0].isdigit():
        limpar()
        print("O nome não pode começar com um número.\n")
        return False
    if not all(caracter.isalnum() or caracter in "_.-" for caracter in nometrip):
        limpar()
        print("O nome não deve ter caracteres especiais além de '-', '_' e '.'.\n")
        return False
    
    
    return True

def validaemail(email):
    emailtrip = email.strip()
   
    if not emailtrip:
        limpar()
        print("O email não pode ser vazio.\n")
        return False
    if emailtrip.count('@') != 1:
        limpar()
        print("O email deve conter domínio '@gmail.com' ou '@ufrpe.br'.\n")
        return False
   
    nome, dominio = emailtrip.split('@')
    
    if not dominio in ['gmail.com', 'ufrpe.br\n']:
        limpar()
        print("O email deve conter dominio '@gmail.com' ou '@ufrpe.br'.\n")
        return False
    if not nome:
        limpar()
        print("O email deve conter algo antes do '@'.\n")
        return False
    if nome.isdigit():
        limpar()
        print("O email não pode conter apenas números antes do '@'.\n")
        return False
    if " " in nome:
        limpar()
        print("O email não pode conter espaços vazios.\n")
        return False
    if not all(caracter.isalnum() or caracter in '_-.' for caracter in nome):
        limpar()
        print("O email só deve conter caracteres alfanuméricos ou os caracteres especiais '_', '-' ou '.' antes do '@'.\n")
        return False
    if nome[0] in '._-' or nome[-1] in '._-':
        limpar()
        print("O email não pode começar com '_', '-' ou '.' antes do '@'.\n")
        return False
    if '..' in nome or '__' in nome or '--' in nome:
        limpar()
        print("O email não pode conter sequências de caracteres especiais('_', '-' ou '.') antes do '@'.\n")
        return False
    if not 6 <= len(nome) <= 20:
        limpar()
        print("O email deve conter entre 6 e 20 caracteres antes do '@'.\n")
        return False
    if not sum(caracter.isalpha() for caracter in nome) >= 1:
        limpar()
        print("O email deve conter no mínimo 1 letra antes do '@'.\n")
        return False
    for usuario in usuarios.usuarioslist:
        if usuario['email'] == email:
            limpar()
            print("Email já existe. Por favor, escolha outro email.\n")
            return False

   
    return True
       
def validasenha(senha):
    senhatrip = senha.strip()
   
    if not senhatrip:
        limpar()
        print("A senha não pode ser vazia.\n")
        return False
    if len(senhatrip) < 8:
        limpar()
        print("A senha deve conter no mínimo 8 caracteres.\n")
        return False
    if len(senhatrip) > 12:
        limpar()
        print("A senha deve conter no máximo 12 caracteres.\n")
        return False
    if not any(caracter.isupper() for caracter in senhatrip):
        limpar()
        print("A senha deve conter pelo menos uma letra maiúscula.\n")
        return False
    if not any(caracter.islower() for caracter in senhatrip):
        limpar()
        print("A senha deve conter pelo menos uma letra minúscula.\n")
        return False
    if  all(caracter.isalnum() for caracter in senhatrip):
        limpar()
        print("A senha deve conter pelo menos um caracter especial.\n")
        return False
    if not any(caracter.isdigit() for caracter in senhatrip):
        limpar()
        print("A senha deve conter pelo menos um número.\n")
        return False
    
   
    return True
