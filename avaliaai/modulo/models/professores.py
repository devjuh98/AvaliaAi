class Professor:
    def __init__(self,nome,codigos):
        self.nome = nome
        self.codigos = codigos
    
    def para_dicionario(self):
        return{
            'nome': self.nome,
            'codigos': self.codigos
        }