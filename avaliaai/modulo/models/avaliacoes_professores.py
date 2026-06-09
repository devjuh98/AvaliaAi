import avaliacoes
import json


class Avaliacoes_professores:
    def __init__(self, professor, dificuldade, didatica, organizacao, usuario, avaliador, indice_avaliador):
        self.professor = professor
        self.dificuldade = dificuldade
        self.didatica = didatica
        self.organizacao = organizacao
        self.usuario = usuario
        self.avaliador = avaliador
        self.indice_avaliador = indice_avaliador

    def para_dicionario(self):
        return{
            'professor': self.professor,
            'dificuldade da avaliação': self.dificuldade,
            'didática': self.didatica,
            'organização': self.organizacao,
            'usuario': self.usuario,
            'avaliador': self.avaliador,
            'indice_avaliador': self.indice_avaliador
        }

    def avaliar(self):
        '''Função para realizar a avaliação de um professor,
        recebe o usuário logado como parâmetro de entrada e sem retorno.'''
        avaliacoes.avaliacoes_professores.append(self)
        with(open(avaliacoes.ARQUIVOAVALIAPROF, 'w', encoding = 'utf-8')) as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_professores], arq, indent = 4, ensure_ascii=False)

    def checar(self,avaliacoesencontradas):
        dificuldade_media = sum(int(av.dificuldade) for av in avaliacoesencontradas) / len(avaliacoesencontradas)
        didatica_media = sum(int(av.didatica) for av in avaliacoesencontradas) / len(avaliacoesencontradas)
        organizacao_media = sum(int(av.organizacao) for av in avaliacoesencontradas) / len(avaliacoesencontradas)

        inteiras = int(dificuldade_media)
        resto = dificuldade_media - inteiras
        if resto != 0:
            estrelas_dificuldade = inteiras*'⭐' + '✯'
        else:
            estrelas_dificuldade = inteiras*'⭐'
        
        inteiras = int(didatica_media)
        resto = didatica_media - inteiras
        if resto != 0:
            estrelas_didatica = inteiras*'⭐' + '✯'
        else:
            estrelas_didatica = inteiras*'⭐'

        inteiras = int(organizacao_media)
        resto = organizacao_media - inteiras
        if resto != 0:
            estrelas_organizacao = inteiras*'⭐' + '✯'
        else:
            estrelas_organizacao = inteiras*'⭐'

        print(f"\nMédia de avaliações do professor {self.professor}:\n")
        print(f"Média de dificuldade da avaliação: {dificuldade_media:.2f} | {estrelas_dificuldade}")
        print(f"Média de didática: {didatica_media:.2f} | {estrelas_didatica}")
        print(f"Média de organização: {organizacao_media:.2f} | {estrelas_organizacao}\n")

        print(f"\nAvaliações do professor {self.professor}:\n")
        for av in avaliacoesencontradas:
            print(f"Usuário: {av.usuario} ({av.avaliador})")
            print(f"Dificuldade da avaliação: {av.dificuldade} | {'⭐'*av.dificuldade}")
            print(f"Didática: {av.didatica} | {'⭐'*av.didatica}")
            print(f"Organização: {av.organizacao} | {'⭐'*av.organizacao}\n")