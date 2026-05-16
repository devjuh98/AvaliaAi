class Avaliacoes_professores:
    def __init__(self, professor, dificuldade, didatica, organizacao, usuario, email):
        self.professor = professor
        self.dificuldade = dificuldade
        self.didatica = didatica
        self.organizacao = organizacao
        self.usuario = usuario
        self.email = email

    def para_dicionario(self):
        return{
            'professor': self.professor,
            'dificuldade da avaliação': self.dificuldade,
            'didática': self.didatica,
            'organização': self.organizacao,
            'usuario': self.usuario,
            'email': self.email
        }