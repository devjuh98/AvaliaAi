import avaliacoes
import utils
from models.disciplinas import Disciplina
from models.professores import Professor

def adicionar_disciplina():
    utils.limpar()
    while True:
        utils.tituloadicionardisciplina()
        nome_disciplina = input("Digite o nome da nova disciplina ou 0 para voltar:\n\n").strip().lower()
        existe_disciplina = False
        if nome_disciplina == '0':
            utils.limpar()
            break
        elif not nome_disciplina:
            utils.limpar()
            print("\033[31mNome da disciplina não pode ser vazio.\033[m\n")
            continue
        elif not all(caracter.isalnum() or caracter == '-' or caracter == ' ' for caracter in nome_disciplina):
            utils.limpar()
            print("\033[31mNome da disciplina deve conter apenas letras, números, espaços ou hífens.\033[m\n")
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
                existe_disciplina = True
                print("\033[31mDisciplina já existe.\033[m\n")
                break
        if existe_disciplina == False:
            utils.limpar()
            nome_list = nome_disciplina.split()
            for nome in nome_list:
                nome_disciplina = nome_disciplina.replace(nome, nome.capitalize())
            codigos = []
            while True:
                utils.tituloadicionardisciplina()
                codigo_existente = False
                print(f"Nome da disciplina: {nome_disciplina}\n")
                print("Abreviações:", end = "")
                for ver_codigos in codigos:
                    if ver_codigos == codigos[0]:
                        print(f" {ver_codigos},", end = "")
                    elif ver_codigos == codigos[-1]:
                        print(f" {ver_codigos}", end = "")
                    else:
                        print(f" {ver_codigos},", end = "")
                print("\n")

                codigo = input("Digite as abreviações da nova disciplina:\n"
                               "Digite 0 quando não houver mais abreviações para a disciplina\n\n").strip().lower()
                if codigo == '0':
                    utils.limpar()
                    break
                elif not codigo:
                    utils.limpar()
                    print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                    continue
                elif not all(caracter.isalnum() for caracter in codigo):
                    utils.limpar()
                    print("\033[31mAbreviação deve conter apenas letras e números\033[m\n")
                    continue
                elif len(codigo) < 2 or len(codigo) > 7:
                    utils.limpar()
                    print("\033[31mAbreviação deve conter entre 2 e 7 caracteres.\033[m\n")
                    continue
                elif codigo in codigos:
                    utils.limpar()
                    print("\033[31mAbreviação já adicionada para esta disciplina.\033[m\n")
                    continue
                for disciplina in avaliacoes.disciplinaslist:
                    if codigo in disciplina.codigos:
                        codigo_existente = True
                        utils.limpar()
                        print(f"\033[31mAbreviação já existe para a disciplina {disciplina.nome}.\033[m\n")
                        break
                if codigo_existente == False:
                    utils.limpar()
                    codigos.append(codigo)
            
                
            nova_disciplina = Disciplina(nome_disciplina,codigos)
            nova_disciplina.cadastrar()
            utils.tituloadicionardisciplina()
            print("\033[32mDisciplina cadastrada com sucesso!\033[m\n") 
            opcao  = input("Deseja cadastrar outra diciplina?\n[1]-Sim\n[2]-Não\n")
            while opcao not in ['1','2']:
                utils.limpar()
                utils.tituloadicionardisciplina()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
                opcao  = input("Deseja cadastrar outra diciplina?\n[1]-Sim\n[2]-Não\n")
            if opcao == '1':
                utils.limpar()
            if opcao == '2':
                utils.limpar()
                return
           
def editar_disciplina():
    utils.limpar()
    while True:
        disciplina_achada = None
        utils.tituloeditardisciplina()
        nome = input("Digite o nome da disciplina que deseja editar (0 para voltar):\n\n").strip().lower()
        if nome == '0':
            utils.limpar()
            break
        if not nome:
            utils.limpar()
            print("\033[31mNome não pode ser vazio.\033[m")
            continue
        
        for disciplina in avaliacoes.disciplinaslist:
            if disciplina.nome.lower() == nome or nome in disciplina.codigos:
                disciplina_achada = disciplina
                break
        if disciplina_achada == None:
            utils.limpar()
            print("\033[31mDisciplina não encontrada.\033[m")
            continue
        else:
            utils.limpar()
            while True:
                utils.tituloeditardisciplina()
                print(f"Disciplina: {disciplina_achada.nome}")
                opcao = input("O que deseja editar(0 para voltar)?\n[1]-Nome\n[2]-Abreviações\n[0]-Voltar\n\n")
                if opcao == '0':
                    utils.limpar()
                    break
                elif opcao == '1':
                    utils.limpar()
                    while True:
                        
                        utils.tituloeditardisciplina()
                        print(f"Nome atual: {disciplina_achada.nome}\n")
                        novo_nome = input("Qual o novo nome da disciplina (0 para voltar)?\n\n")
                        existe = False
                        if novo_nome == '0':
                            utils.limpar()
                            break
                        elif not novo_nome:
                            utils.limpar()
                            print("\033[31mNome da disciplina não pode ser vazio.\033[m\n")
                            continue
                        elif not all(caracter.isalnum() or caracter == ' ' or caracter == '-' for caracter in novo_nome):
                            utils.limpar()
                            print("\033[31mNome da disciplina só deve conter letras, número, espaços ou hífens.\033[m\n")
                            continue
                        elif '  ' in novo_nome or '--' in novo_nome:
                            utils.limpar()
                            print("\033[31mNome da disciplina não pode conter hífens ou espaços consecutivos.\033[m\n")
                        elif len(novo_nome) < 4 or len(novo_nome) > 60:
                            utils.limpar()
                            print("\033[31mNome da disciplina deve conter entre 4 e 60 caracteres.\033[m\n")
                            continue
                        for disciplina in avaliacoes.disciplinaslist:
                            if disciplina.nome.lower() == novo_nome and disciplina.nome != disciplina_achada.nome:
                                existe = True
                                utils.limpar()
                                print("\033[31mNome da disciplina já existe.\033[m\n")
                                break
                        if existe == False:
                            utils.limpar()
                            nome_list = novo_nome.split()
                            for nome in nome_list:
                                novo_nome = novo_nome.replace(nome, nome.capitalize())
                            disciplina_achada.editar_nome(novo_nome)
                            utils.limpar()
                            print("\033[32mEditada com sucesso!\033[m\n")
                            utils.tituloeditardisciplina()
                            opcao = input("Deseja editar outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
                            while opcao not in ['1','2']:
                                utils.limpar()
                                print("\033[31mOpção Inválida\033[m\n")
                                utils.tituloeditardisciplina()
                                opcao = input("Deseja editar outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
                            if opcao == '1':
                                utils.limpar()
                                break
                            else:
                                utils.limpar()
                                return
                    break
                elif opcao == '2':
                    codigos = []
                    utils.limpar()
                    while True:
                        
                        utils.tituloeditardisciplina()
                        codigo_existente = False
                        print(f"Códigos atuais de {disciplina_achada.nome}: ",end = '')
                        for c in disciplina_achada.codigos:
                            if c == disciplina_achada.codigos[-1]:
                                print(f"{c}\n")
                            else:
                                print(f"{c},",end = '')
                        print("Novas Abreviações:", end = '')
                        for ver_codigos in codigos:
                            if ver_codigos == codigos[0]:
                                print(f" {ver_codigos},", end = '')
                            elif ver_codigos == codigos[-1]:
                                print(f" {ver_codigos}", end = '')
                            else:
                                print(f" {ver_codigos},", end = '')
                        print("\n")

                        codigo = input("Digite as abreviações da nova disciplina(0 para voltar):\n"
                               "Digite 'fim' quando não houver mais abreviações para a disciplina\n\n").strip().lower()
                        if codigo == '0':
                            utils.limpar()
                            break                     
                        elif codigo.lower().strip() == 'fim':
                            disciplina_achada.editar_abreviacoes(codigos)
                            utils.limpar()
                            print("\033[32mEditada com sucesso!\033[m\n")
                            utils.tituloeditardisciplina()
                            opcao = input("Deseja editar outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
                            while opcao not in ['1','2']:
                                utils.limpar()
                                print("\033[31mOpção Inválida\033[m\n")
                                utils.tituloeditardisciplina()
                                opcao = input("Deseja editar outra disciplina?\n[1]-Sim\n[2]-Não\n\n")
                            if opcao == '1':
                                utils.limpar()
                                break
                            else:
                                utils.limpar()
                                return
                                
                        elif not codigo:
                            utils.limpar()
                            print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                            continue
                        elif not all(caracter.isalnum() for caracter in codigo):
                            utils.limpar()
                            print("\033[31mAbreviação deve conter apenas letras e números\033[m\n")
                            continue
                        elif len(codigo) < 2 or len(codigo) > 7:
                            utils.limpar()
                            print("\033[31mAbreviação deve conter entre 2 e 7 caracteres.\033[m\n")
                            continue
                        elif codigo in codigos:
                            utils.limpar()
                            print("\033[31mAbreviação já adicionada para esta disciplina.\033[m\n")
                            continue
                        for disciplina in avaliacoes.disciplinaslist:
                            if codigo in disciplina.codigos and disciplina_achada.nome != disciplina.nome:
                                codigo_existente = True
                                utils.limpar()
                                print(f"\033[31mAbreviação já existe para a disciplina {disciplina.nome}.\033[m\n")
                                break
                        if codigo_existente == False:
                            utils.limpar()
                            codigos.append(codigo)
                    break
                else:
                    utils.limpar()
                    print("\033[31mOpção Inválida\033[m\n")
def remover_disciplina():
    utils.limpar()
    while True:
        utils.tituloremoverdisciplina()
        avaliacoes_feitas = []
        disciplina_achada = None
        nome_disciplina = input("Digite o nome da disciplina a ser removida ou 0 para voltar:\n\n").strip().lower()
        if nome_disciplina == '0':
            utils.limpar()
            break
        if not nome_disciplina:
            utils.limpar()
            print("\033[31mNome da disciplina não pode ser vazio.\033[m")
            continue

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
    utils.limpar()
    while True:
        utils.tituloadicionarprofessor()
        nome_professor = input("Digite o nome completo do novo professor ou 0 para voltar:\n\n").strip().lower()
        existe = False
        if nome_professor == '0':
            utils.limpar()
            break
        elif not nome_professor:
            print("\033[31mNome do professor não pode ser vazio.\033[m\n")
            continue
        elif not all(caracter.isalpha() or caracter == ' ' for caracter in nome_professor):
            print("\033[31mNome do professor deve conter apenas letras e espaços\033[m\n")
            continue
        elif len(nome_professor) < 4 or len(nome_professor) > 50:
            print("\033[31mNome do professor deve conter entre 4 e 50 caracteres.\033[m\n")
            continue
        for professor in avaliacoes.professoreslist:
            if professor.nome.lower() == nome_professor:
                existe = True
                print("\033[31mProfessor já existe.\033[m\n")
                break
        if existe == False:
            utils.limpar()
            codigos = []
            nome_list = nome_professor.split()
            for nome in nome_list:
                nome_professor = nome_professor.replace(nome, nome.capitalize())
            while True:
                utils.tituloadicionarprofessor()
                codigo_existente = False
                print(f"Nome do professor: {nome_professor}\n")
                print("Abreviações:", end  = '')
                for ver_codigos in codigos:
                    if ver_codigos == codigos[0]:
                        print(f" {ver_codigos},", end = "")
                    elif ver_codigos == codigos[-1]:
                        print(f" {ver_codigos}", end = "")
                    else:
                        print(f" {ver_codigos},", end = "")
                print("\n")
                
                codigo = ''.join(input("Digite as abreviações do novo professor:\n"
                               "Digite 0 quando não tiver mais abreviações para o professor\n\n").strip().lower().split())
                if codigo == '0':
                    utils.limpar()
                    break
                elif not codigo:
                    utils.limpar()
                    print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                    continue
                elif not all(caracter.isalpha() for caracter in codigo):
                    utils.limpar()
                    print("\033[31mAbreviação de professor deve conter apenas letras\033[m\n")
                    continue
                elif len(codigo) < 2 or len(codigo) > 20:
                    utils.limpar()
                    print("\033[31mAbreviação deve conter entre 2 e 20 caracteres.\033[m\n")
                    continue
                elif codigo in codigos:
                    utils.limpar()
                    print("\033[31mAbreviação já adicionada para este professor.\033[m\n")
                    continue
                for professor in avaliacoes.professoreslist:
                    if codigo in professor.codigos:
                        codigo_existente = True
                        utils.limpar()
                        print(f"\033[31mAbreviação já existe para o professor {professor.nome}.\033[m\n")
                        break
                if codigo_existente == False:
                    utils.limpar()
                    codigos.append(codigo)
            
            novo_professor = Professor(nome_professor,codigos)
            novo_professor.cadastrar()
            utils.tituloadicionarprofessor()
            print("\033[32mProfessor cadastrado com sucesso!\033[m\n")
            opcao  = input("Deseja cadastrar outro professor?\n[1]-Sim\n[2]-Não\n")
            while opcao not in ['1','2']:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\nDigite um número do menu:\n")
                opcao  = input("Deseja cadastrar outro professor?\n[1]-Sim\n[2]-Não\n")
            if opcao == '1':
                utils.limpar()
            else:
                utils.limpar()
                return          

def editar_professor():
    utils.limpar()
    while True:
        professor_achado = None
        utils.tituloeditarprofessor()
        nome = input("Digite o nome do professor que deseja editar (0 para voltar):\n\n").strip().lower()
        if nome == '0':
            utils.limpar()
            break
        if not nome:
            utils.limpar()
            print("\033[31Nome não pode ser vazio.\033[m")
            continue
        for professor in avaliacoes.professoreslist:
            if professor.nome.lower() == nome or nome in professor.codigos:
                professor_achado = professor
                break
        if professor_achado == None:
            utils.limpar()
            print("\033[31Professor não encontrado.\033[m")
            continue
        else:
            while True:
                utils.limpar()
                utils.tituloeditarprofessor()
                print(f"Professor: {professor_achado.nome}")
                opcao = input("O que deseja editar(0 para voltar)?\n[1]-Nome\n[2]-Abreviações\n[0]-Voltar")
                if opcao == '0':
                    utils.limpar()
                    break
                elif opcao == '1':
                    utils.limpar()
                    while True:         
                        utils.tituloeditarprofessor()
                        print(f"Nome atual: {professor_achado.nome}")
                        novo_nome = input("Qual o novo nome do  (0 para voltar)?\n\n")
                        existe = False
                        if novo_nome == '0':
                            utils.limpar()
                            break
                        elif not novo_nome:
                            utils.limpar()
                            print("\033[31mNome do professor não pode ser vazio.\033[m\n")
                            continue
                        elif not all(caracter.isalpha() or caracter == ' ' for caracter in novo_nome):
                            utils.limpar()
                            print("\033[31mNome do professor não pode conter números.\033[m\n")
                            continue
                        elif len(novo_nome) < 4 or len(novo_nome) > 50:
                            utils.limpar()
                            print("\033[31mNome do professor deve conter entre 4 e 50 caracteres.\033[m\n")
                            continue
                        for professor in avaliacoes.professoreslist:
                            if professor.nome.lower() == novo_nome and professor.nome.lower != professor_achado.nome:
                                utils.limpar()
                                existe = True
                                print("\033[31mProfessor já existe.\033[m\n")
                                break
                        if existe == False:
                            utils.limpar()
                            nome_list = novo_nome.split()
                            for nome in nome_list:
                                novo_nome = novo_nome.replace(nome, nome.capitalize())
                            professor_achado.editar_nome(novo_nome)
                            print("\033[31mEditado com sucesso!\033[m\n")
                            utils.tituloeditarprofessor()
                            opcao = input("Deseja editar outro professor?\n[1]-Sim\n[2]-Não\n\n")
                            while opcao not in ['1','2']:
                                utils.limpar()
                                print("\033[31mOpção Inválida\033[m\n")
                                utils.tituloeditarprofessor()
                                opcao = input("Deseja editar outro professor?\n[1]-Sim\n[2]-Não\n\n")
                            if opcao == '1':
                                utils.limpar()
                                break
                            else:
                                utils.limpar()
                                return
                    break
                elif opcao == '2':
                    codigos = []
                    utils.limpar()
                    while True:               
                        utils.tituloeditarprofessor()
                        codigo_existente = False
                        print(f"Códigos atuais: do professor {professor_achado.nome}:", end = '')
                        for c in professor.codigos:
                            if c == professor.codigos[-1]:
                                print(f"{c}\n")
                            else:
                                print(f"{c},",end = '')
                        print("\n")
                        print("Novas Abreviações:", end = '')
                        for ver_codigos in codigos:
                            if ver_codigos == codigos[0]:
                                print(f" {ver_codigos},", end = "")
                            elif ver_codigos == codigos[-1]:
                                print(f" {ver_codigos}", end = "")
                            else:
                                print(f" {ver_codigos},", end = "")
                        print("\n")

                        codigo = input("Digite as abreviações da nova disciplina:\n"
                               "Digite 0 quando não houver mais abreviações para a disciplina\n\n").strip().lower()
                        if codigo == '0':
                            utils.limpar()
                            break
                        elif codigo.lower().strip() == 'fim':
                            professor_achado.editar_abreviacoes(codigos)
                            utils.limpar()
                            print("\033[32mEditado com sucesso!\033[mzn")
                            utils.tituloeditarprofessor()
                            opcao = input("Deseja editar outro professor?\n[1]-Sim\n[2]-Não\n\n")
                            while opcao not in ['1','2']:
                                utils.limpar()
                                print("\033[31mOpção Inválida\033[m\n")
                                utils.tituloeditarprofessor()
                                opcao = input("Deseja editar outro professor?\n[1]-Sim\n[2]-Não\n\n")
                            if opcao == '1':
                                utils.limpar()
                                break
                            else:
                                utils.limpar()
                                return
                        elif not codigo:
                            utils.limpar()
                            print("\033[31mAbreviação não pode ser vazia.\033[m\n")
                            continue
                        elif not all(caracter.isalnum() for caracter in codigo):
                            utils.limpar()
                            print("\033[31mAbreviação de professor deve conter apenas letras\033[m\n")
                            continue
                        elif len(codigo) < 2 or len(codigo) > 20:
                            utils.limpar()
                            print("\033[31mAbreviação deve conter entre 2 e 20 caracteres.\033[m\n")
                            continue
                        elif codigo in codigos:
                            utils.limpar()
                            print("\033[31mAbreviação já adicionada para este professor.\033[m\n")
                            continue
                        for professor in avaliacoes.professoreslist:
                            if codigo in professor.codigos and professor_achado.nome != professor.nome:
                                codigo_existente = True
                                utils.limpar()
                                print(f"\033[31mAbreviação já existe para o professor {professor.nome}.\033[m\n")
                                break
                        if codigo_existente == False:
                            utils.limpar()
                            codigos.append(codigo)        
                    break
                else:
                    utils.limpar()
                    print("\033[31mOpção Inválida\033[m\n")
                 
def remover_professor():
    utils.limpar()
    while True:
        utils.tituloremoverprofessor()
        avaliacoes_feitas = []
        professor_achado = None
        nome_professor = input("Digite o nome do professor a ser removido ou 0 para voltar: \n").strip().lower()
        if nome_professor == '0':
            utils.limpar()
            break
        if not nome_professor:
            utils.limpar()
            print("\033[31mNome do professor não pode ser vazio.\033[m\n")
            continue
        
        for professor in avaliacoes.professoreslist:
            if professor.nome.lower() == nome_professor or nome_professor in professor.codigos:
                professor_achado = professor.nome.lower()
                for avaliacao in avaliacoes.avaliacoes_professores:
                    if avaliacao.professor.lower() == professor_achado:
                        avaliacoes_feitas.append(avaliacao)
                professor.remover(avaliacoes_feitas)
                utils.limpar()
                print("\033[32mProfessor removido com sucesso!\033[m\n")
                break
        if professor_achado == None:
            utils.limpar()
            print("\033[31mProfessor não encontrado.\033[m\n")
        
