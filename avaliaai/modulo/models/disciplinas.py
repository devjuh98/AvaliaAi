import avaliacoes
import json
class Disciplina:
    def __init__(self,nome,codigos):
        self.nome = nome
        self.codigos = codigos
    
    def para_dicionario(self):
        return{
            'nome': self.nome,
            'codigos': self.codigos
        }
    def cadastrar(self):
        '''Função para realizar o cadastro da disciplina,
        armazenando os dados em um json e em uma lista
        sem parâmetros de entrada e sem retorno.'''
        avaliacoes.disciplinaslist.append(self)
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
    
    def remover(self,avaliacoes_disciplina):
        '''Função para realizar a remoção da disciplina,
        recebe o nome da disciplina como parâmetro de entrada e sem retorno.'''
        avaliacoes.disciplinaslist.remove(self)
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
        for avaliacao in avaliacoes_disciplina:
            avaliacoes.avaliacoes_disciplina.remove(avaliacao)
        with open(avaliacoes.ARQUIVOAVALIACOESDISCIPLINA, 'w', encoding='utf-8') as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_disciplinas], arq, indent=4, ensure_ascii=False)