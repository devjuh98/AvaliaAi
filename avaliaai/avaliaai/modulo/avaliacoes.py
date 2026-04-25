import json,os
import usuarios as usuarios
import utils as utils

professoreslist = []
disciplinaslist = []
avaliacoes_disciplinas = []
avaliacoes_professores = []

ARQUIVODISCIPLINAS = os.path.join(os.path.dirname(__file__), 'disciplinas.json')
try:
    with open(ARQUIVODISCIPLINAS, 'r', encoding = 'utf-8') as arq:
        disciplinaslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    disciplinaslist = []

ARQUIVOPROFESSORES = os.path.join(os.path.dirname(__file__), 'professores.json')
try:
    with open(ARQUIVOPROFESSORES, 'r', encoding = 'utf-8') as arq:
        professoreslist = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    professoreslist = []

ARQUIVOAVALIADISC = os.path.join(os.path.dirname(__file__), 'avaliacoes_disciplinas.json')
try:
    with open(ARQUIVOAVALIADISC, 'r', encoding = 'utf-8') as arq:
        avaliacoes_disciplinas = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    avaliacoes_disciplinas = []

ARQUIVOAVALIAPROF = os.path.join(os.path.dirname(__file__), 'avaliacoes_professores.json')
try:
    with open(ARQUIVOAVALIAPROF, 'r', encoding = 'utf-8') as arq:
        avaliacoes_disciplinas = json.load(arq)
except(FileNotFoundError, json.JSONDecodeError):
    avaliacoes_disciplinas = []



def avaliadisciplina(usuariologado):
    utils.limpar()
    utils.tituloavaliardisciplina()
    while True:
        disciplinachada = False
        disciplinavaliada = False

        disciplinaprocurada = "".join(input('Digite uma disciplina ou digite 0 para voltar:\n').split())
        if disciplinaprocurada == '0':
            return
        for disciplina in disciplinaslist:
            if disciplinaprocurada == "".join(disciplina["nome"].lower().strip().split()) or disciplinaprocurada in disciplina["codigos"]:
                disciplinachada = True
                for avaliacao in avaliacoes_disciplinas:
                    if avaliacao['email'] == usuariologado['email'] and avaliacao['disciplina'] == disciplina['nome']:
                        disciplinavaliada = True
                        break

            if disciplinavaliada == False and disciplinachada == True:      
                utils.limpar()
                utils.tituloavaliardisciplina()
                print('Disciplina Encontrada!\n')
                while True:
                    try:
                        dificuldade = int(input('Digite um valor de 1 a 5 para avaliar nível de dificuldade ou 0 para cancelar:\nOBS:5-Muito Difícil e 1-Muito Fácil\n'))
                        if dificuldade == 0:break
                        if dificuldade not in [1,2,3,4,5]:
                            utils.limpar()
                            utils.tituloavaliardisciplina()
                            print('\033[31mVALOR INVÁLIDO\033[m\n') 
                        else:
                            utils.limpar()
                            utils.tituloavaliardisciplina()
                            while True:
                                try:
                                    carga = int(input('Digite um valor de 1 a 5 para avaliar nível de carga de trabalho ou 0 para voltar:\nOBS:5-Muita carga e 1-Pouquíssima carga\n'))
                                    if carga == 0:break
                                    if carga not in [1,2,3,4,5]:
                                        utils.limpar()
                                        utils.tituloavaliardisciplina()
                                        print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                    else:
                                        utils.limpar()
                                        utils.tituloavaliardisciplina()    
                                        while True:
                                            try:
                                                utilidade = int(input('Digite um valor de 1 a 5 para avaliar nível de utilidade do conteúdo ou 0 para voltar:\nOBS:5-Muito útil e 1-Pouquíssimo útil\n'))
                                                if utilidade == 0:break
                                                if utilidade not in [1,2,3,4,5]:
                                                    utils.limpar()
                                                    utils.tituloavaliardisciplina()
                                                    print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                                else:
                                                    utils.limpar()
                                                    utils.tituloavaliardisciplina()
                                                    avaliacoes_disciplinas.append({
                                                        'disciplina': disciplina['nome'],
                                                        'dificuldade': dificuldade,
                                                        'carga': carga,
                                                        'utilidade': utilidade,
                                                        'usuario': usuariologado['nome'],
                                                        'email': usuariologado['email']
                                                    })
                                                    with(open(ARQUIVOAVALIADISC, 'w', encoding = 'utf-8')) as arq:
                                                        json.dump(avaliacoes_disciplinas, arq, indent = 4, ensure_ascii=False)

                                                    while True:
                                                        try:
                        
                                                            reavaliar = int(input('\033[32mAvaliação concluída!\n\033[m Deseja avaliar outra disciplina?\n\n[1]-Sim\n[2]-Não\n'))
                                                            if reavaliar == 1:
                                                                utils.limpar()
                                                                utils.tituloavaliardisciplina()
                                                                break
                                                            if reavaliar == 2:
                                                                return
                                                            else:
                                                                utils.limpar()
                                                                utils.tituloavaliardisciplina()
                                                                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                                        except(ValueError):
                                                            utils.limpar()
                                                            utils.tituloavaliardisciplina()
                                                            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                                    break              
                                            except(ValueError):
                                                utils.limpar()
                                                utils.tituloavaliardisciplina()
                                                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                        break
                                except(ValueError):
                                    utils.limpar()
                                    utils.tituloavaliardisciplina()
                                    print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                            break
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaliardisciplina()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                break               
        utils.limpar()
        utils.tituloavaliardisciplina()
        if disciplinachada == False: print('\033[31mDisciplina não encontrada\033[m')#if fora do for
        if disciplinavaliada == True: print('\033[31mVocê já avaliou essa disciplina! Escolha outra!\033[m\n')#if fora do for

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

def avaliaprofessor(usuariologado):
    utils.limpar()
    utils.tituloavaliarprofessor()
    while True:
        professorachado = False
        professoravaliado = False

        professorprocurado = "".join(input('Digite um professor ou digite 0 para voltar:\n').lower().strip().split())
        if professorprocurado == '0':
            return
        for professor in professoreslist:
            if professorprocurado == "".join(professor["nome"].lower().strip().split()) or professorprocurado in professor["codigos"]:
                professorachado = True
                for avaliacao in avaliacoes_professores:
                    if avaliacao['email'] == usuariologado['email'] and avaliacao['professor'] == professor['nome']:
                        professoravaliado = True
                        break

            if professoravaliado == False and professorachado == True:        
                utils.limpar()
                utils.tituloavaliarprofessor()
                print('Professor Encontrado!\n')
                while True:
                    try:
                        dificuldadedaprova = int(input('Digite um valor de 1 a 5 para avaliar nível de dificuldade da avaliação ou 0 para cancelar:\nOBS:5-Muito Difícil e 1-Muito Fácil\n'))
                        if dificuldadedaprova == 0:break
                        if dificuldadedaprova not in [1,2,3,4,5]:
                            utils.limpar()
                            utils.tituloavaliarprofessor()
                            print('\033[31mVALOR INVÁLIDO\033[m\n') 
                        else:
                            utils.limpar()
                            utils.tituloavaliarprofessor()
                            while True:
                                try:
                                    didatica = int(input('Digite um valor de 1 a 5 para avaliar nível de didática ou 0 para voltar:\nOBS:5-Didática Excelente e 1-Péssima Didática\n'))
                                    if didatica == 0:break
                                    if didatica not in [1,2,3,4,5]:
                                        utils.limpar()
                                        utils.tituloavaliarprofessor()
                                        print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                    else:
                                        utils.limpar()
                                        utils.tituloavaliarprofessor()    
                                        while True:
                                            try:
                                                organizacao = int(input('Digite um valor de 1 a 5 para avaliar nível de organização do conteúdo ou 0 para voltar:\nOBS:5-Muito organizado e 1-Pouquíssimo organizado\n'))
                                                if organizacao == 0:break
                                                if organizacao not in [1,2,3,4,5]:
                                                    utils.limpar()
                                                    utils.tituloavaliarprofessor()
                                                    print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                                else:
                                                    utils.limpar()
                                                    utils.tituloavaliarprofessor()
                                                    avaliacoes_professores.append({
                                                        'professor': professor['nome'],
                                                        'dificuldade da avaliação': dificuldadedaprova,
                                                        'Didática': didatica,
                                                        'Organização': organizacao,
                                                        'usuario': usuariologado['nome'],
                                                        'email': usuariologado['email']
                                                    })
                                                    with(open(ARQUIVOAVALIAPROF, 'w', encoding = 'utf-8')) as arq:
                                                        json.dump(avaliacoes_professores, arq, indent = 4, ensure_ascii=False)

                                                    while True:
                                                        try:
                        
                                                            reavaliar = int(input('\033[32mAvaliação concluída!\n\033[m Deseja avaliar outro professor?\n\n[1]-Sim\n[2]-Não\n'))
                                                            if reavaliar == 1:
                                                                utils.limpar()
                                                                utils.tituloavaliarprofessor()
                                                                break
                                                            if reavaliar == 2:
                                                                return
                                                            else:
                                                                utils.limpar()
                                                                utils.tituloavaliarprofessor()
                                                                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                                        except(ValueError):
                                                            utils.limpar()
                                                            utils.tituloavaliarprofessor()
                                                            print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                                    break              
                                            except(ValueError):
                                                utils.limpar()
                                                utils.tituloavaliarprofessor()
                                                print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                                        break
                                except(ValueError):
                                    utils.limpar()
                                    utils.tituloavaliarprofessor()
                                    print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                            break
                    except(ValueError):
                        utils.limpar()
                        utils.tituloavaliarprofessor()
                        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n')
                break               
        utils.limpar()
        utils.tituloavaliarprofessor()
        if professorachado == False: print('\033[31mProfessor não encontrada\033[m')
        if professoravaliado == True: print('\033[31mVocê já avaliou esse professor! Escolha outro!\033[m\n')

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
