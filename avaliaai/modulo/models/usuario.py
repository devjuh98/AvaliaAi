class Usuario:  
    def __init__(self, nome, email, senha, status='ativo'):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status

    def para_dicionario(self):
        return{
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'status': self.status
        }