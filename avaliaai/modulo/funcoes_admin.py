import avaliacoes
import utils
from models.disciplinas import Disciplina
from models.professores import Professor

def adicionar_disciplina():
    while True:
        nome_disciplina = input("Digite o nome da nova disciplina ou 0 para voltar:\n").strip().lower()
        existe = False
        if nome_disciplina == '0':
            utils.limpar()
            break
        elif not nome_disciplina:
            utils.limpar()
            print("\033[31mNome da disciplina não pode ser vazio.\033[m\n")
            continue
        elif not all(caracter.isalnum() or caracter == '-' or caracter == ' ' for caracter in nome_disciplina):
            utils.limpar()
            print("\033[31mNome da disciplina deve conter apenas letras, números ou hífens.\033[m\n")
            continue
        elif '--' in nome_disciplina or '  ' in nome_disciplina:
            utils.limpar()
            print("\033[31mNome da disciplina não pode conter hífens ou espaços consecutivos.\033[m\n")
            continue
        elif len(nome_disciplina) < 4 or len(nome_disciplina) > 60:
            utils.limpar()
            print("\033[31mNome da disciplina deve conter entre 4 e 60 caracteres.\033[m\n")
            continue
        for disciplina in avaliacoes.disciplinaslist:
            if disciplina.nome.lower() == nome_disciplina or nome_disciplina in disciplina.codigos:
                utils.limpar()
                existe = True
                print("\033[31mDisciplina já existe.\033[m\n")
                break
        if existe == False:
            utils.limpar()
            codigos = []
            while True:
                    
                existente = False
                codigo = input("Digite as abreviações da nova disciplina:\n"
                               "Digite 0 quando não tiver mais abreviações para a disciplina\n").strip().lower()
                if codigo == '0':
                    break
                elif not codigo:
                    utils.limpar()
                    print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                    continue
                elif not all(caracter.isalnum() or caracter == ' ' for caracter in codigo):
                    utils.limpar()
                    print("\033[31mAbreviação deve conter apenas letras e números\033[m\n")
                    continue
                elif len(codigo) < 2 or len(codigo) > 7:
                    utils.limpar()
                    print("\033[31mAbreviação deve conter entre 2 e 7 caracteres.\033[m\n")
                    continue
                elif '  ' in codigo:
                    utils.limpar()
                    print("\033[31mAbreviação não pode conter espaços consecutivos.\033[m\n")
                    continue
                for codigo_existente in avaliacoes.disciplinaslist:
                    if codigo in codigo_existente.codigos:
                        existente = True
                        utils.limpar()
                        print(f"\033[31mAbreviação já existe para a disciplina {codigo_existente.nome}.\033[m\n")
                        break
                if existente == False:
                    utils.limpar()
                    codigos.append(codigo)
            nome_list = nome_disciplina.split()
            for nome in nome_list:
                nome_disciplina = nome_disciplina.replace(nome, nome.capitalize())
                
            nova_disciplina = Disciplina(nome_disciplina,codigos)
            nova_disciplina.cadastrar()
            print("\033[32mDisciplina cadastrada com sucesso!\033[m\n")
            utils.limpar()
            opcao  = input("Deseja cadastrar outra diciplina?\n[1]-Sim\n[2]-Não\n")
            while opcao not in ['1','2']:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
                opcao  = input("Deseja cadastrar outra diciplina?\n[1]-Sim\n[2]-Não\n")
            if opcao == '1':
                utils.limpar()
                break
                utils.limpar()
                return
                
            break
           
        

def editar_disciplina():
        print()
    
def remover_disciplina():
    while True:
        avaliacoes_feitas = []
        disciplina_achada = None
        nome_disciplina = input("Digite o nome da disciplina a ser removida ou 0 para voltar: \n").strip().lower()
        if nome_disciplina == '0':
            break
        if not nome_disciplina:
            print("\033[31mNome da disciplina não pode ser vazio.\033[m")

        for disciplina in avaliacoes.disciplinaslist:
            if disciplina.nome.lower() == nome_disciplina or nome_disciplina in disciplina.codigos:
                disciplina_achada = disciplina.nome.lower()
                for avaliacao in avaliacoes.avaliacoes_disciplinas:
                    if avaliacao.disciplina.lower() == disciplina_achada:
                        avaliacoes_feitas.append(avaliacao)
                disciplina.remover(avaliacoes_feitas)
                utils.limpar()
                print("\033[32mDisciplina removida com sucesso!\033[m\n")
                break
        if disciplina_achada == None:
            utils.limpar()
            print("\033[31mDisciplina não encontrada.\033[m\n")

def adicionar_professor():

     while True:
        nome_professor = input("Digite o nome do novo professor ou 0 para voltar: \n").strip()
        if nome_professor == '0':
            break
        elif not nome_professor:
            print("\033[31mNome do professor não pode ser vazio.\033[m\n")
            continue
        elif not all(caracter.isalpha() or caracter == ' ' for caracter in nome_professor):
            print("\033[31mNome do professor não pode conter números.\033[m\n")
            continue
        elif len(nome_professor) < 4 or len(nome_professor) > 50:
            print("\033[31mNome do professor deve conter entre 4 e 50 caracteres.\033[m\n")
            continue
        for professor in avaliacoes.professoreslist:
            if professor.nome.lower() == nome_professor or nome_professor in professor.codigos:
                print("\033[31mProfessor já existe.\033[m\n")
                break
        else:
            
            codigos = []
            while True:
                existente = False
                codigo = input("Digite as abreviações do novo professor:\n"
                               "Digite 0 quando não tiver mais abreviações para o professor\n").strip().lower()
                if codigo == '0':
                    break
                elif not codigo:
                    print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                    continue
                elif not all(caracter.isalpha() or caracter == ' ' for caracter in codigo):
                    print("\033[31mAbreviação deve conter apenas letras e ou espaços\033[m\n")
                    continue
                elif len(codigo) < 2 or len(codigo) > 20:
                    print("\033[31mAbreviação deve conter entre 2 e 20 caracteres.\033[m\n")
                    continue
                elif '  ' in codigo:
                    print("\033[31mAbreviação não pode conter espaços consecutivos.\033[m\n")
                    continue
                for codigo_existente in avaliacoes.professoreslist:
                    if codigo in codigo_existente.codigos:
                        existente = True
                        print(f"\033[31mAbreviação já existe para o professor {codigo_existente.nome}.\033[m\n")
                        break
                if existente == False:
                    codigos.append(codigo)
            novo_professor = Professor(nome_professor,codigos)
            novo_professor.cadastrar()
            break
           

def editar_professor():
    print()

def remover_professor():
     
     while True:
        avaliacoes_feitas = []
        nome_professor = input("Digite o nome do professor a ser removido ou 0 para voltar: \n").strip().lower()
        if nome_professor == '0':
            break
        if not nome_professor:
            print("\033[31mNome do professor não pode ser vazio.\033[m\n")
        
        for professor in avaliacoes.professoreslist:
            if professor.nome.lower() == nome_professor or nome_professor in professor.codigos:
                professor_achado = professor.nome.lower()
                for avaliacao in avaliacoes.avaliacoes_professores:
                    if avaliacao.professor.lower() == professor_achado:
                        avaliacoes_feitas.append(avaliacao)
                professor.remover(avaliacoes_feitas)
                print("\033[32mProfessor removido com sucesso!\033[m\n")
                break
        print("\033[31mProfessor não encontrado.\033[m\n")
        
