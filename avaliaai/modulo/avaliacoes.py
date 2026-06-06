import json,os
import usuarios as usuarios
import utils as utils
from models.disciplinas import Disciplina
from models.professores import Professor
from models.avaliacoes_disciplinas import Avaliacoes_disciplinas
from models.avaliacoes_professores import Avaliacoes_professores

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
        #disciplinaslist = json.load(arq)
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
        #professoreslist = json.load(arq)
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
        #avaliacoes_disciplinas = json.load(arq)
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
        #avaliacoes_professores = json.load(arq)
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
                                                    #avaliacoes_disciplinas.append(nova_avaliacao)
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
                                                    #with(open(ARQUIVOAVALIADISC, 'w', encoding = 'utf-8')) as arq:
                                                        #json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes_disciplinas], arq, indent = 4, ensure_ascii=False)

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
                                                    #with(open(ARQUIVOAVALIAPROF, 'w', encoding = 'utf-8')) as arq:
                                                        #json.dump([avaliacao.para_dicionario() for avaliacao in avaliacoes_professores], arq, indent = 4, ensure_ascii=False)

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
            #dificuldade_media = sum(int(av.dificuldade) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #carga_media = sum(int(av.carga) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #utilidade_media = sum(int(av.utilidade) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #print(f"\nMédia de avaliações da disciplina {disciplinaencontrada.nome}:\n")
            #print(f"Média de dificuldade: {dificuldade_media:.2f}")
            #print(f"Média de carga de trabalho: {carga_media:.2f}")
            #print(f"Média de utilidade do conteúdo: {utilidade_media:.2f}\n")

            #print(f"\nAvaliações da disciplina {disciplinaencontrada.nome}:\n")
            #for av in avaliacaoencontrada:
                #print(f"Usuário: {av.usuario}")
                #print(f"Dificuldade: {av.dificuldade}")
                #print(f"Carga de trabalho: {av.carga}")
                #print(f"Utilidade do conteúdo: {av.utilidade}\n")

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
            #dificuldadeav_media = sum(int(av.dificuldade) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #didatica_media = sum(int(av.didatica) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #organizacao_media = sum(int(av.organizacao) for av in avaliacaoencontrada) / len(avaliacaoencontrada)
            #print(f"\nMédia de avaliações do professor {professorencontrado.nome}:\n")
            #print(f"Média de dificuldade da avaliação: {dificuldadeav_media:.2f}")
            #print(f"Média de didática: {didatica_media:.2f}")
            #print(f"Média de organização: {organizacao_media:.2f}")
            
            #print(f"\nAvaliações do professor {professorencontrado.nome}:\n")
            #for av in avaliacaoencontrada:
                #print(f"Usuário: {av.usuario}")
                #print(f"Dificuldade da avaliação: {av.dificuldade}")
                #print(f"Didática: {av.didatica}")
                #print(f"Organização: {av.organizacao}\n")

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
