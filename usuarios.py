import utils

usuarioslist = []
def cadastrar_usuario():
   
   
    while True:
       
        nome = input('Digite o nome do usuário: \n0 para sair\n')
        if nome.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validanome(nome):
            utils.limpar()
            print("Nome Cadastrado.\n")
            break
            
    while True:
        
        email = input('Digite o email do usuário: \n0 para sair\n')
        utils.limpar() 
        if email.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validaemail(email):
            print("Email Cadastrado.\n")
            break
           
    while True:
        
        senha = input('Digite a senha do usuário: \n0 para sair\n')
        utils.limpar() 
        if senha.strip() == '0':
            utils.limpar()
            utils.menuinicial()
            return
        if utils.validasenha(senha):
            utils.limpar()
            print("Senha Cadastrada.\n\nCadastro concluído com sucesso!")
            break
   
    usuarioslist.append({
        'nome': nome,
        'email': email,
        'senha': senha,
        'status': 'ativo'
    })

def usuario_login():
    print("Login")
       