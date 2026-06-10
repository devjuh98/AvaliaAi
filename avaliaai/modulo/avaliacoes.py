import json,os
import usuarios as usuarios
import utils as utils
from models.disciplinas import Disciplina
from models.professores import Professor
from models.avaliacoes_disciplinas import Avaliacoes_disciplinas
from models.avaliacoes_professores import Avaliacoes_professores
from collections import defaultdict

professoreslist = []
disciplinaslist = []
avaliacoes_disciplinas = []
avaliacoes_professores = []

ARQUIVODISCIPLINAS = os.path.join(os.path.dirname(__file__),'data', 'disciplinas.json')
try:
    with open(ARQUIVODISCIPLINAS, 'r', encoding = 'utf-8') as arq:
        for dados in json.load(arq):
            disciplinacadastrada = Disciplina(
                dados['nome'], 
                dados['codigos'])
            disciplinaslist.append(disciplinacadastrada)
except(FileNotFoundError, json.JSONDecodeError):
    disciplinaslist = []

ARQUIVOPROFESSORES = os.path.join(os.path.dirname(__file__),'data', 'professores.json')
try:
    with open(ARQUIVOPROFESSORES, 'r', encoding = 'utf-8') as arq:
        for dados in json.load(arq):
            professorcadastrado = Professor(
                dados['nome'], 
                dados['codigos'])
            professoreslist.append(professorcadastrado)
except(FileNotFoundError, json.JSONDecodeError):
    professoreslist = []

ARQUIVOAVALIADISC = os.path.join(os.path.dirname(__file__),'data', 'avaliacoes_disciplinas.json')
try:
    with open(ARQUIVOAVALIADISC, 'r', encoding = 'utf-8') as arq:
        for dados in json.load(arq):
            avaliacaodisciplina = Avaliacoes_disciplinas(
                dados['disciplina'], 
                dados['dificuldade'],
                dados['carga'],
                dados['utilidade'],
                dados['usuario'],
                dados['avaliador'],
                dados['indice_avaliador'],
                dados['situacao_academica'])
            avaliacoes_disciplinas.append(avaliacaodisciplina)
except(FileNotFoundError, json.JSONDecodeError):
    avaliacoes_disciplinas = []

ARQUIVOAVALIAPROF = os.path.join(os.path.dirname(__file__),'data', 'avaliacoes_professores.json')
try:
    with open(ARQUIVOAVALIAPROF, 'r', encoding = 'utf-8') as arq:
        for dados in json.load(arq):
            avaliacaoprofessor = Avaliacoes_professores(
                dados['professor'],
                dados['dificuldade da avaliação'],
                dados['didática'],
                dados['organização'],
                dados['usuario'],
                dados['avaliador'],
                dados['indice_avaliador'])
            avaliacoes_professores.append(avaliacaoprofessor)
except(FileNotFoundError, json.JSONDecodeError):
    avaliacoes_professores = []



def avaliadisciplina(usuariologado):
    '''Função para realizar a avaliação de uma disciplina,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    utils.limpar()
    utils.tituloavaliardisciplina()
    while True:
        disciplinachada = False
        disciplinavaliada = False

        disciplinaprocurada = "".join(input('Digite uma disciplina ou digite 0 para voltar:\n').lower().strip().split())
        if disciplinaprocurada == '0':
            return
        for disciplina in disciplinaslist:
            if disciplinaprocurada == "".join(disciplina.nome.lower().split()) or disciplinaprocurada in disciplina.codigos:
                disciplinachada = True
                for avaliacao in avaliacoes_disciplinas:
                    if avaliacao.avaliador == usuariologado.nome_real and avaliacao.indice_avaliador == usuariologado.indice_nome and avaliacao.disciplina == disciplina.nome:
                        disciplinavaliada = True
                        break

            if disciplinavaliada == False and disciplinachada == True:      
                utils.limpar()
                utils.tituloavaliardisciplina()
                print('DISCIPLINA ENCONTRADA!\n')
                while True:
                    try:
                        print(f'Avaliando disciplina {disciplina.nome}:\n')
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
                                    print(f'Avaliando disciplina {disciplina.nome}:\n')
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
                                                print(f'Avaliando disciplina {disciplina.nome}:\n')
                                                utilidade = int(input('Digite um valor de 1 a 5 para avaliar nível de utilidade do conteúdo ou 0 para voltar:\nOBS:5-Muito útil e 1-Pouquíssimo útil\n'))
                                                if utilidade == 0:break
                                                if utilidade not in [1,2,3,4,5]:
                                                    utils.limpar()
                                                    utils.tituloavaliardisciplina()
                                                    print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                                else:
                                                    situacao_academica = None
                                                    utils.limpar()
                                                    utils.tituloavaliardisciplina()
                                                    situacao = input("Qual a sua situação em relação a disciplina?:"
                                                                     "\n[1]-Reprovado\n[2]-Aprovado\n[3]-Cursando\n\n")
                                                    while situacao not in ['1','2','3']:
                                                        utils.limpar()
                                                        utils.tituloavaliardisciplina()
                                                        print('\033[31mOPÇÃO INVÁLIDA\033[m\n')
                                                        situacao = input("Qual a sua situação em relação a disciplina?:"
                                                                     "\n[1]-Reprovado\n[2]-Aprovado\n[3]-Cursando\n\n")
                                                    if situacao == 1:
                                                        utils.limpar() 
                                                        situacao_academica = 'Reprovado'
                                                    elif situacao == 2:
                                                        utils.limpar()  
                                                        situacao_academica = 'Approvado'
                                                    else:
                                                        utils.limpar()  
                                                        situacao_academica = 'Cursando'

                                                    nova_avaliacao = Avaliacoes_disciplinas(disciplina.nome,dificuldade,carga,utilidade,usuariologado.nome,usuariologado.nome_real,usuariologado.indice_nome,situacao_academica)
                                                    nova_avaliacao.avaliar()
                                                    '''
                                                    avaliacoes_disciplinas.append({
                                                        'disciplina': disciplina['nome'],
                                                        'dificuldade': dificuldade,
                                                        'carga': carga,
                                                        'utilidade': utilidade,
                                                        'usuario': usuariologado.nome,
                                                        'email': usuariologado.email
                                                    })
                                                    '''

                                                    while True:
                                                        try:
                        
                                                            reavaliar = int(input('\033[32mAvaliação concluída!\n\033[mDeseja avaliar outra disciplina?\n\n[1]-Sim\n[2]-Não\n'))
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

def avaliaprofessor(usuariologado):
    '''Função para realizar a avaliação de um professor,
    recebe o usuário logado como parâmetro de entrada e sem retorno.'''
    utils.limpar()
    utils.tituloavaliarprofessor()
    while True:
        professorachado = False
        professoravaliado = False

        professorprocurado = "".join(input('Digite um professor ou digite 0 para voltar:\n').lower().strip().split())
        if professorprocurado == '0':
            return
        for professor in professoreslist:
            if professorprocurado == "".join(professor.nome.lower().split()) or professorprocurado in professor.codigos:
                professorachado = True
                for avaliacao in avaliacoes_professores:
                    if avaliacao.avaliador == usuariologado.nome_real and usuariologado.indice_nome == avaliacao.indice_avaliador and avaliacao.professor == professor.nome:
                        professoravaliado = True
                        break

            if professoravaliado == False and professorachado == True:        
                utils.limpar()
                utils.tituloavaliarprofessor()
                print('PROFESSOR ENCONTRADO!\n')
                while True:
                    try:
                        print(f'Avaliando professor {professor.nome}:\n')
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
                                    print(f'Avaliando professor {professor.nome}:\n')
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
                                                print(f'Aaliando professor {professor.nome}:\n')
                                                organizacao = int(input('Digite um valor de 1 a 5 para avaliar nível de organização do conteúdo ou 0 para voltar:\nOBS:5-Muito organizado e 1-Pouquíssimo organizado\n'))
                                                if organizacao == 0:break
                                                if organizacao not in [1,2,3,4,5]:
                                                    utils.limpar()
                                                    utils.tituloavaliarprofessor()
                                                    print('\033[31mVALOR INVÁLIDO\033[m\n') 
                                                else:
                                                    utils.limpar()
                                                    utils.tituloavaliarprofessor()
                                                    nova_avaliacao = Avaliacoes_professores(professor.nome,dificuldadedaprova,didatica,organizacao,usuariologado.nome,usuariologado.nome_real,usuariologado.indice_nome)
                                                    nova_avaliacao.avaliar()
                                                    #avaliacoes_professores.append(nova_avaliacao)
                                                    '''
                                                    avaliacoes_professores.append({
                                                        'professor': professor['nome'],
                                                        'dificuldade da avaliação': dificuldadedaprova,
                                                        'Didática': didatica,
                                                        'Organização': organizacao,
                                                        'usuario': usuariologado.nome,
                                                        'email': usuariologado.email
                                                    })
                                                    '''

                                                    while True:
                                                        try:
                        
                                                            reavaliar = int(input('\033[32mAvaliação concluída!\n\033[mDeseja avaliar outro professor?\n\n[1]-Sim\n[2]-Não\n'))
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

def checardisciplina():
    '''Função para checar avaliações de disciplinas,
    sem parâmetros de entrada e sem retorno.'''
    while True:
        utils.limpar()
        titulochecardisciplina = '\033[36mAVALIAÇÕES DE DISCIPLINAS\033[m'
        print(titulochecardisciplina.center(50,'='), '\n\n')
        procurardisciplina = "".join(input("Digite o nome da disciplina que deseja checar ou digite 0 para voltar:\n").lower().strip().split())

        if procurardisciplina == "0":
            return
            
        disciplinaencontrada = None
        for disciplina in disciplinaslist:
            if procurardisciplina == "".join(disciplina.nome.lower().split()) or procurardisciplina in [c for c in disciplina.codigos]:
                disciplinaencontrada = disciplina
                break
        if not disciplinaencontrada:
            print("\033[31mDISCIPLINA INEXISTENTE!\033[m\n")
            input("Pressione Enter para continuar...")
            continue

        avaliacaoencontrada = [av for av in avaliacoes_disciplinas if av.disciplina == disciplinaencontrada.nome]
        if not avaliacaoencontrada:
            utils.limpar()
            print(f"\033[31mA disciplina {disciplinaencontrada.nome} não possui nenhuma avaliação ainda!\033[m")
        else:
            utils.limpar()
            avaliacaoencontrada[0].checar(avaliacaoencontrada)        

        while True:
            try:
                escolha = int(input("Deseja checar outra disciplina?\n1-Sim\n2-Não\n"))
                if escolha == 1:
                    utils.limpar()
                    break
                elif escolha == 2:
                    return
                else:
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            except ValueError:
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

def checarprofessor():
    '''Função para checar avaliações de professores,
    sem parâmetros de entrada e sem retorno.'''
    while True:
        utils.limpar()
        titulochecarprofessor = '\033[36mAVALIAÇÕES DE PROFESSORES\033[m'
        print(titulochecarprofessor.center(50,'='), '\n\n')
        procurarprofessor = "".join(input("Digite o nome do professor que deseja checar ou digite 0 para voltar:\n").lower().strip().split())

        if procurarprofessor == "0":
            return
            
        professorencontrado = None
        for professor in professoreslist:
            if procurarprofessor == "".join(professor.nome.lower().split()) or procurarprofessor in [c for c in professor.codigos]:
                professorencontrado = professor
                break
        if not professorencontrado:
            print("\033[31mPROFESSOR INEXISTENTE![m\n")
            input("Pressione Enter para continuar...")
            continue

        avaliacaoencontrada = [av for av in avaliacoes_professores if av.professor == professorencontrado.nome]
        if not avaliacaoencontrada:
            utils.limpar()
            print(f"\033[31mO professor {professorencontrado.nome} não possui nenhuma avaliação ainda!\033[m")
        else:
            utils.limpar()
            avaliacaoencontrada[0].checar(avaliacaoencontrada)

        while True:
            try:
                escolha = int(input("Deseja checar outro professor?\n1-Sim\n2-Não\n"))
                if escolha == 1:
                    utils.limpar()
                    break
                elif escolha == 2:
                    return
                else:
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
            except ValueError:
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

class DificuldadePeriodo:
    
    def calcular_dificuldade_media_disciplina():
        dificuldades = defaultdict(list)
        for av in avaliacoes_disciplinas:
            dificuldades[av.disciplina].append(int(av.dificuldade))
        
        medias = {disc: sum(vals)/len(vals) for disc, vals in dificuldades.items()}
        return medias
    
    def calcular_dificuldade_periodo(numero_periodo):
        medias = DificuldadePeriodo.calcular_dificuldade_media_disciplina()
        with open(ARQUIVODISCIPLINAS, 'r', encoding='utf-8') as arq:
            disciplinas = json.load(arq)
        
        filtradas = [d for d in disciplinas if int(d.get("periodo", 0)) == numero_periodo]

        dificuldades = []
        for d in filtradas:
            if d['nome'] in medias:
                dificuldades.append(medias[d['nome']])
                print(f"{d['nome']}: {medias[d['nome']]:.2f}")
        
        if not dificuldades:
            print("\033[31mNenhuma avaliação encontrada para este período!\033[m")
            return
        
        media_periodo = sum(dificuldades) / len(dificuldades)
        nivel = round(media_periodo)
        print(f"\n\033[36mNível médio de dificuldade do período {numero_periodo}: {nivel} (1=Muito Fácil, 2=Fácil, 3=Regular, 4=Difícil, 5=Muito Difícil)\033[m\n")
    
    def calcular_dificuldade_extra(numero_periodo, disciplina_extra):
        medias = DificuldadePeriodo.calcular_dificuldade_media_disciplina()
        with open(ARQUIVODISCIPLINAS, 'r', encoding='utf-8') as arq:
            disciplinas = json.load(arq)
        
        filtradas = [d for d in disciplinas if int(d.get("periodo", 0)) == numero_periodo]

        dificuldades = []
        nomes_disciplinas = [d['nome'] for d in filtradas]

        for d in filtradas:
            if d['nome'] in medias:
                dificuldades.append(medias[d['nome']])
                print(f"{d['nome']}: {medias[d['nome']]:.2f}")
        
        disciplina_encontrada = next((d for d in disciplinas if d['nome'].lower() == disciplina_extra.lower()), None)
        if disciplina_encontrada:
            if disciplina_encontrada['nome'] in medias:
                dificuldades.append(medias[disciplina_encontrada['nome']])
                print(f"\nDisciplina extra adicionada: {disciplina_encontrada['nome']} - {medias[disciplina_encontrada['nome']]:.2f}")
            else:
                print("\033[31mA disciplina extra não possui avaliações registradas!\033[m")
        else:
            print("\033[31mDisciplina extra não encontrada!\033[m")
        
        if not dificuldades:
            print("\033[31mNenhuma avaliação encontrada para este período!\033[m")
            return
        
        media_periodo = sum(dificuldades) / len(dificuldades)
        nivel = round(media_periodo)
        print(f"\n\033[36mNível médio de dificuldade do período {numero_periodo} com disciplina extra: {nivel} (1=Muito Fácil, 2=Fácil, 3=Regular, 4=Difícil, 5=Muito Difícil)\033[m\n")

    def dificuldadeperiodo():
        '''Função para exibir o nível de dificuldade do período,
        sem parâmetros de entrada e sem retorno.'''
        utils.limpar()
        titulodificuldade = '\033[36mNÍVEL DE DIFICULDADE DO PERÍODO\033[m'
        print(titulodificuldade.center(50, '='),'\n\n')
        periodo = print("Digite o número do período que deseja consultar ou digite 0 para voltar:\n\n[1]-1º Período\n[2]-2º Período\n[3]-3º Período\n[4]-4º Período\n[5]-5º Período\n[6]-6º Período\n[7]-7º Período\n[8]-8º Período\n[9]-9º Período\n")
        while True:
            try:
                periodo = int(input("Digite a opção desejada:\n"))
                if periodo == 0:
                    return
                if periodo not in range(1,10):
                    utils.limpar()
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                else:
                    utils.limpar()
                    print(titulodificuldade.center(50, '='),'\n\n')
                    DificuldadePeriodo.calcular_dificuldade_periodo(periodo)
            except ValueError:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

    def adicionardisciplina():
        
        utils.limpar()
        titulodificuldade = '\033[36mADICIONAR DISCIPLINA\033[m'
        print(titulodificuldade.center(50, '='),'\n\n')
        opcao = print("Digite o número do período que deseja adicionar disciplina ou digite 0 para voltar:\n\n[1]-1º Período\n[2]-2º Período\n[3]-3º Período\n[4]-4º Período\n[5]-5º Período\n[6]-6º Período\n[7]-7º Período\n[8]-8º Período\n[9]-9º Período\n")
        while True:
            try:
                opcao = int(input("Digite a opção desejada:\n"))
                if opcao == 0:
                    return
                if opcao not in range(1, 10):
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                    continue

                disciplina_extra = input("Digite a disciplina que queira adicionar ao período:\n").strip()
                if not disciplina_extra:
                    print(("\033[31mNenhuma disciplina informada!\033[m\n"))
                    return
                
                DificuldadePeriodo.calcular_dificuldade_extra(opcao, disciplina_extra)
            except ValueError:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                

        
        