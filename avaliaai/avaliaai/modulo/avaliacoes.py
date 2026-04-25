import json,os
import avaliaai.modulo.usuarios as usuarios
import avaliaai.modulo.utils as utils

disciplinaslist = []

ARQUIVODISCIPLINAS = os.path.join(os.path.dirname(__file__), 'disciplinas.json')
try:
    with open(ARQUIVODISCIPLINAS, 'r', encoding = 'utf-8') as arq:
        disciplinaslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    disciplinaslist = []

avaliacaolist = []

def avaliadisciplina():
    disciplinachada = False
    utils.limpar()
    utils.tituloavaldisc()
    while True:
        
        disciplinaprocurada = input('Digite uma disciplina ou digite 0 para voltar:\n')
        if disciplinaprocurada == '0':
            return
        for disciplina in disciplinaslist:
            if disciplinaprocurada == disciplina["nome"] or disciplinaprocurada in disciplina["codigos"]:
                disciplinaachada = True
                utils.limpar()
                utils.tituloavaldisc()
                print('Disciplina Encontrda!\n')
                while True:
                    try:
                        dificuldade = int(input('Digite um valor de 1 a 5 para avalir nível de dificuldade ou 0 para cancelar:\nOBS:5-Muito Difícil e 1-Muito Fácil\n'))
                        if dificuldade == 0:disciplinaachada = False;return
                        if dificuldade not in [1,2,3,4,5]:
                            utils.limpar()
                            utils.tituloavaldisc()
                            print('\033[31mVALOR INVÁLIDO\033[m\n') 
                        else:break
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaldisc()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                utils.limpar()
                utils.tituloavaldisc()
                while True:
                    try:
                        carga = int(input('Digite um valor de 1 a 5 para avalir nível de carga de trabalho ou 0 para voltar:\nOBS:5-Muita carga e 1-Pouquíssima carga\n'))
                        if carga == 0:disciplinaachada = False;return
                        if carga not in [1,2,3,4,5]:
                            utils.limpar()
                            utils.tituloavaldisc()
                            print('\033[31mVALOR INVÁLIDO\033[m\n') 
                        else:break
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaldisc()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                utils.limpar()
                utils.tituloavaldisc()    
                while True:
                    try:
                        utilidade = int(input('Digite um valor de 1 a 5 para avalir nível de utilidade do conteúdo ou 0 para voltar:\nOBS:5-Muito útil e 1-Pouquíssimo útil\n'))
                        if utilidade == 0:disciplinaachada = False;return
                        if utilidade not in [1,2,3,4,5]:
                            utils.limpar()
                            utils.tituloavaldisc()
                            print('\033[31mVALOR INVÁLIDO\033[m\n') 
                        else:break
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaldisc()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')    
                    
                avaliacaolist.append({'disciplina':disciplina["nome"],
                                        'dificuldade':dificuldade,
                                        'carga':carga,
                                        'utilidade':utilidade})
                utils.limpar()
                utils.tituloavaldisc()
                while True:
                    try:
                        
                        reavaliar = int(input('Avaliação concluída! Deseja avaliar outra disciplina?\n\n[1]-Sim\n[2]-Não\n'))
                        if reavaliar == 1:
                            utils.limpar()
                            utils.tituloavaldisc()
                            break
                        if reavaliar == 2:
                            return
                        else:
                            utils.limpar()
                            utils.tituloavaldisc()
                            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaldisc()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                break
        
        utils.limpar()
        utils.tituloavaldisc()
        if disciplinachada == False: print('\033[31mDisciplina não encontrada\033[m')

# Função para checar avaliações de disciplinas
def checardisciplina():
    while True:
        titulochecardisciplina = '\033[36mAVALIAÇÕES DE DISCIPLINAS\033[m'
        print(titulochecardisciplina.center(50,'='), '\n\n')
        procurardisciplina = input("Digite o nome da disciplina que deseja checar ou digite 0 para voltar:\n")

        if procurardisciplina == "0":
            return
            
        disciplinaencontrada = None
        for disciplina in disciplinaslist:
            if procurardisciplina.lower() == disciplina["nome"].lower() or procurardisciplina.lower() in [c.lower() for c in disciplina["codigos"]]:
                disciplinaencontrada = disciplina
                break
        if not disciplinaencontrada:
            utils.limpar()
            print("\033[31mDISCIPLINA INEXISTENTE![m\n")
            continue

        avaliacaoencontrada = [av for av in avaliacaolist if av["disciplina"] == disciplinaencontrada["nome"]]
        if not avaliacaoencontrada:
            utils.limpar()
            print(f"\033[31mA disciplina {disciplinaencontrada["nome"]} não possui nenhuma avaliação ainda!\033[m")
        else:
            utils.limpar()
            print(f"\nAvaliações da disciplina {disciplinaencontrada["nome"]}:")
            for av in avaliacaoencontrada:
                print(f"Dificuldade: {av["dificuldade"]}")
                print(f"Carga de trabalho: {av["carga"]}")
                print(f"Utilidade do conteúdo: {av["utilidade"]}\n")

        while True:
            try:
                escolha = int(input("Deseja checar outra disciplina?\n1-Sim\n2-Não\n"))
                if escolha == 1:
                    utils.limpar()
                    break
                if escolha == 2:
                    return
                else:
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            except ValueError:
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
