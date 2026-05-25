import avaliacoes
import json

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
    
    def avaliar(self):
        '''Função para realizar a avaliação de uma disciplina,
        recebe o usuário logado como parâmetro de entrada e sem retorno.'''
        avaliacoes.avaliacoes_disciplinas.append(self)
        with(open(avaliacoes.ARQUIVOAVALIADISC, 'w', encoding = 'utf-8')) as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_disciplinas], arq, indent = 4, ensure_ascii=False)
    
    def checar(self,avaliacoesencontradas):
        dificuldade_media = sum(int(av.dificuldade) for av in avaliacoesencontradas) / len(avaliacoesencontradas)
        carga_media = sum(int(av.carga) for av in avaliacoesencontradas) / len(avaliacoesencontradas)
        utilidade_media = sum(int(av.utilidade) for av in avaliacoesencontradas) / len(avaliacoesencontradas)
        print(f"\nMédia de avaliações da disciplina {self.disciplina}:\n")
        print(f"Média de dificuldade: {dificuldade_media:.2f}")
        print(f"Média de carga de trabalho: {carga_media:.2f}")
        print(f"Média de utilidade do conteúdo: {utilidade_media:.2f}\n")

        print(f"\nAvaliações da disciplina {self.disciplina}:\n")
        for av in avaliacoesencontradas:
            print(f"Usuário: {av.usuario}")
            print(f"Dificuldade: {av.dificuldade}")
            print(f"Carga de trabalho: {av.carga}")
            print(f"Utilidade do conteúdo: {av.utilidade}\n")