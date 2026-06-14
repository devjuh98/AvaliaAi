import avaliacoes
import json
from models.avaliacoes_disciplinas import Avaliacoes_disciplinas
import matplotlib.pyplot as plt

class Disciplina:
    def __init__(self,nome,codigos,periodo = None):
        self.nome = nome
        self.codigos = codigos
        self.periodo = periodo
    
    def para_dicionario(self):
        return{
            'nome': self.nome,
            'codigos': self.codigos,
            'periodo': self.periodo
        }
    def cadastrar(self):
        '''Função para realizar o cadastro da disciplina,
        armazenando os dados em um json e em uma lista
        sem parâmetros de entrada e sem retorno.'''
        
        avaliacoes.disciplinaslist.append(self)
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
    
    def editar_nome(self,novo_nome):
        '''Função para realizar a edição do nome do professor,
        recebe o nome do professor como parâmetro de entrada e sem retorno.'''
        for avaliacao in avaliacoes.avaliacoes_disciplinas:
            if avaliacao.disciplina.lower() == self.nome.lower():
                avaliacao.disciplina = novo_nome
        
        with open(avaliacoes.ARQUIVOAVALIADISC, 'w', encoding='utf-8') as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_disciplinas], arq, indent=4, ensure_ascii=False)
        
        self.nome = novo_nome
        
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
    
    def editar_abreviacoes(self, novas_abreviacoes):
        '''Função para realizar a edição dos códigos do professor,
        recebe as abreviações como parâmetro de entrada e sem retorno.'''
        self.codigos = novas_abreviacoes
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
    
    def editar_periodo(self, novo_periodo):
        '''Função para realizar a edição do número do período, recebe o número do período como parâmetro e sem retorno.'''
        self.periodo = novo_periodo
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([Disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent=4, ensure_ascii=False)
    
    def remover(self,avaliacoes_disciplina):
        '''Função para realizar a remoção da disciplina,
        recebe o nome da disciplina como parâmetro de entrada e sem retorno.'''
        avaliacoes.disciplinaslist.remove(self)
        with open(avaliacoes.ARQUIVODISCIPLINAS, 'w', encoding='utf-8') as arq:
            json.dump([disciplina.para_dicionario() for disciplina in avaliacoes.disciplinaslist], arq, indent = 4, ensure_ascii=False)
        for avaliacao in avaliacoes_disciplina:
            avaliacoes.avaliacoes_disciplinas.remove(avaliacao)
        with open(avaliacoes.ARQUIVOAVALIADISC, 'w', encoding='utf-8') as arq:
            json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes.avaliacoes_disciplinas], arq, indent=4, ensure_ascii=False)

    def mostrar_taxas(self,avaliacoes):
        reprovacao = 0
        aprovacao = 0
        if len(avaliacoes) == 0:
            print("Não há avaliações suficientes para geras taxas de reprovação ou aprovação\n")
            return
        for avaliacao in avaliacoes:
            if avaliacao.situacao_academica == 'Reprovado':
                reprovacao += 1
            elif avaliacao.situacao_academica == 'Aprovado':
                aprovacao += 1
        reprovacao_taxa = reprovacao/(reprovacao+aprovacao)
        aprovacao_taxa = aprovacao/(reprovacao+aprovacao)
        print(f"Disciplina: {self.nome}\n\n")
        print(f"Índice de reprovação: {reprovacao_taxa*100}%")
        print(f"Índice de aprovação: {aprovacao_taxa*100}%\n")
        if reprovacao + aprovacao == 0:
            print("Não há avaliações concluídas para gerar gráfico")
        else:
            plt.pie(
            [aprovacao, reprovacao],
            labels=['Aprovados', 'Reprovados'],
            autopct='%1.1f%%',
            colors=['green', 'red']
            )
            plt.title(f"Índices de aprovação e reprovação\n{self.nome}")
            plt.show() 

