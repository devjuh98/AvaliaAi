class Avaliacoes_disciplinas:
    def __init__(self, disciplina, dificuldade, carga, utilidade, usuario, email):
        self.disciplina = disciplina
        self.dificuldade = dificuldade
        self.carga = carga
        self.utilidade = utilidade
        self.usuario = usuario
        self.email = email

    def para_dicionario(self):
        return{
            'disciplina': self.disciplina,
            'dificuldade': self.dificuldade,
            'carga': self.carga,
            'utilidade': self.utilidade,
            'usuario': self.usuario,
            'email': self.email
        }