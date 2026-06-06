import utils
import avaliacoes
from models.disciplinas import Disciplina

def indices():
    utils.limpar()
    while True:
        utils.titulotaxas()
        lista_avaliacoes = []
        disciplina_achada = None
        disciplina_procurada = input("Qual disciplina deseja ver as taxas (0 para voltar)?\n")
        if disciplina_procurada == '0':
            utils.limpar()
            return
        if not disciplina_procurada:
            utils.limpar()
            print("\033[31mNome da disciplina não pode ser vazio.\033[m\n")
            continue
        for disciplina in avaliacoes.disciplinaslist:
            if disciplina.nome == disciplina_procurada or disciplina_procurada in disciplina.codigos:
                disciplina_achada = disciplina
        if disciplina_achada != None:
            for avaliacao in avaliacoes.avaliacoes_disciplinas:
                if avaliacao.disciplina == disciplina_achada.nome:
                    lista_avaliacoes.append(avaliacao)
        else:
            utils.limpar()
            print("\033[31mDisciplina não encontrada.\033[m\n")
            continue
        utils.limpar()
        utils.titulotaxas()
        disciplina_achada.mostrar_taxas(lista_avaliacoes)
        opcao = input("Deseja ver as taxas de outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
        while opcao not in ['1','2']:
            utils.limpar()
            utils.titulotaxas()
            disciplina_achada.mostrar_taxas(lista_avaliacoes)
            opcao = input("Deseja ver as taxas de outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
        if opcao == '1':
            utils.limpar()
        else:
            utils.limpar()
            return

