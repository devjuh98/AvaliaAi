import avaliacoes
import json

class Professor:
    def __init__(self,nome,codigos):
        self.nome = nome
        self.codigos = codigos
    
    def para_dicionario(self):
        return{
            'nome': self.nome,
            'codigos': self.codigos
        }
    
    def cadastrar(self):

        '''Função para realizar o cadastro do professor,
        armazenando os dados em um json e em uma lista
        sem parâmetros de entrada e sem retorno.'''
        avaliacoes.professoreslist.append(self)
        with open(avaliacoes.ARQUIVOPROFESSORES, 'w', encoding='utf-8') as arq:
            json.dump([professor.para_dicionario() for professor in avaliacoes.professoreslist], arq, indent = 4, ensure_ascii=False)
    
    def editar_nome(self,novo_nome):
        '''Função para realizar a edição do nome do professor,
        recebe o nome do professor como parâmetro de entrada e sem retorno.'''
        for avaliacao in avaliacoes.avaliacoes_professores:
            if avaliacao.professor.lower() == self.nome.lower():
                avaliacao.professor = novo_nome
        with open(avaliacoes.ARQUIVOAVALIAPROF, 'w', encoding='utf-8') as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_professores], arq, indent=4, ensure_ascii=False)
        self.nome = novo_nome
        with open(avaliacoes.ARQUIVOPROFESSORES, 'w', encoding='utf-8') as arq:
            json.dump([professor.para_dicionario() for professor in avaliacoes.professoreslist], arq, indent = 4, ensure_ascii=False)
    
    def editar_abreviacoes(self, novas_abreviacoes):
        '''Função para realizar a edição dos códigos do professor,
        recebe as abreviações como parâmetro de entrada e sem retorno.'''
        self.codigos = novas_abreviacoes
        with open(avaliacoes.ARQUIVOPROFESSORES, 'w', encoding='utf-8') as arq:
            json.dump([professor.para_dicionario() for professor in avaliacoes.professoreslist], arq, indent = 4, ensure_ascii=False)
    
    def remover(self,avaliacao_professor):
        '''Função para realizar a remoção do professor,
        recebe o nome do professor como parâmetro de entrada e sem retorno.'''
        avaliacoes.professoreslist.remove(self)
        with open(avaliacoes.ARQUIVOPROFESSORES, 'w', encoding='utf-8') as arq:
            json.dump([professor.para_dicionario() for professor in avaliacoes.professoreslist], arq, indent = 4, ensure_ascii=False)
        for avaliacao in avaliacao_professor:
            avaliacoes.avaliacoes_professores.remove(avaliacao)
        with open(avaliacoes.ARQUIVOAVALIAPROF, 'w', encoding='utf-8') as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_professores], arq, indent=4, ensure_ascii=False)