import menus as menus
import json, os
import utils as utils
import avaliacoes as avaliacoes
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)
UPLOADS = os.path.join(DATA_DIR, 'upload.json')

if not os.path.exists(UPLOADS):
    with open(UPLOADS, 'w', encoding='utf-8') as arq:
        json.dump([], arq, indent=4, ensure_ascii=False)
        
DOWNLOADS = os.path.join(DATA_DIR, 'download.json')

if not os.path.exists(DOWNLOADS):
    with open(DOWNLOADS, 'w', encoding='utf-8') as arq:
        json.dump([], arq, indent=4, ensure_ascii=False)

Linkazul = '\033[4;34m'
Reset = '\033[0m'

class Materiais:

    print("UPLOADS:", UPLOADS)
    print("Gravou com sucesso!")
    print("DOWNLOADS:", DOWNLOADS)
    print("Gravou com sucesso!")

    def abrirexplorador():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        caminho = filedialog.askopenfilename(
            parent=root,
            title="Selecione o arquivo PDF",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        root.destroy()
        return caminho
            
    def carregar_json(caminho):
        if not os.path.exists(caminho):
            return[]
        try:
            with open(caminho, 'r', encoding='utf-8') as arq:
                return json.load(arq)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def salvar_json(caminho, dados):
        try:
            with open(caminho, 'w', encoding='utf-8') as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"\033[31mErro ao salvar arquivo: {e}\033[m\n")

    def upload_arquivo(tipo_material, disciplina, professor):
            print(f"\n{Linkazul}[Selecione o arquivo para upload...]{Reset}")
            arquivo = Materiais.abrirexplorador()
            print(f"\nArquivo selecionado: {arquivo}\n")

            caminho = Path(arquivo)
            
            if caminho.is_file():
                nome_arquivo = caminho.name
                carregar = Materiais.carregar_json(UPLOADS)
                novo_material = {
                    'tipo': tipo_material,
                    'disciplina': disciplina,
                    'professor': professor,
                    'arquivo': str(caminho)
                }
                carregar.append(novo_material)
                Materiais.salvar_json(UPLOADS, carregar)
                print(f"\n\033[32m{tipo_material} adicionado(a) com sucesso!\033[m\n")
            else:
                print("\n\033[31mUpload cancelado!\033[m\n")

    def registrar_download(caminho_json_download, nome_arquivo, caminho_origem):
        downloads_atuais = Materiais.carregar_json(caminho_json_download)
        if not isinstance(downloads_atuais, list):
            downloads_atuais = []
        
        novo_registro = {
            "id": len(downloads_atuais) + 1,
            "nome": nome_arquivo,
            "caminho": caminho_origem,
            "status": "disponível_para_download"
        }

        downloads_atuais.append(novo_registro)

        Materiais.salvar_json(caminho_json_download, downloads_atuais)
        print(f"\n\033[32mSucesso: {nome_arquivo} foi adicionado ao histórico de downloads!\033[m\n")

    def upload():
        tituloupload = '\033[36mUPLOAD DE MATERIAIS\033[m'
        print(tituloupload.center(50, '='),'\n\n')
        opcao = print("Selecione o tipo de material que deseja fazer upload:\n\n[1]-Prova\n[2]-Lista de exercícios\n[3]-Trabalho")
        while True:
            try:
                opcao = int(input("\nDigite a opção desejada: "))
            except ValueError:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                continue

            if opcao in [1, 2, 3]:
                tipo = 'Prova' if opcao == 1 else 'Lista de exercícios' if opcao == 2 else 'Trabalho'

                while True:
                    disciplina = input(f"\nDigite o nome da disciplina do(a) {tipo.lower()}: ")
                    professor = input(f"\nDigite o nome do professor do(a) {tipo.lower()} (opcional): ")

                    verificar_disciplina = Materiais.carregar_json(avaliacoes.ARQUIVODISCIPLINAS)
                    nomes_disciplinas = [d['nome'].strip().lower() for d in verificar_disciplina]
                    codigos_disciplinas = []
                    for d in verificar_disciplina:
                        for codigo in d['codigos']:
                            codigos_disciplinas.append(codigo.strip().lower())

                    entrada = disciplina.strip().lower()
                    if entrada not in nomes_disciplinas and entrada not in codigos_disciplinas:
                        print("\033[31mDISCIPLINA NÃO ENCONTRADA!\033[m\n")
                        continue

                    if not professor.strip():
                        professor = "Não informado"        

                    Materiais.upload_arquivo(tipo, disciplina, professor)

            elif opcao == 0:
                utils.limpar()
                break

            else:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                continue
                    
    def download():
        titulodownload = '\033[36mDOWNLOAD DE MATERIAIS\033[m'
        print(titulodownload.center(50, '='),'\n\n')
        materiais = Materiais.carregar_json(UPLOADS)
        
        if not materiais:
            print("\033[31mNenhum material disponível para download!\033[m\n")
            return
        
        opcao = print("Selecione o tipo de material que deseja fazer download:\n\n[1]-Prova\n[2]-Lista de exercícios\n[3]-Trabalho")
        while True:
            try:
                opcao = int(input("\nDigite a opção desejada: "))
            except ValueError:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                continue

            if opcao in [1, 2, 3]:
                tipo = 'Prova' if opcao == 1 else 'Lista de exercícios' if opcao == 2 else 'Trabalho'
                disciplina = input(f"\nDigite o nome da disciplina do(a) {tipo.lower()}: ")

                filtrarmateriais = [m for m in materiais if m['tipo'] == tipo and m['disciplina'].strip().lower() == disciplina.strip().lower()]

                if not filtrarmateriais:
                    print("\033[31mNenhum material encontrado para a disciplina informada!\033[m")
                    continue

                print(f"\nMateriais disponíveis para {tipo} de {disciplina}:\n")
                for i, m in enumerate(filtrarmateriais, start=1):
                    print(f"{i}. {m['arquivo']} - Professor: {m['professor']}")

                try:
                    escolha = int(input("\nDigite o número do material que deseja baixar: "))
                except ValueError:
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")
                    continue

                if 1 <= escolha <= len(filtrarmateriais):
                    selecionado = filtrarmateriais[escolha - 1]
                    caminho_arquivo = selecionado['arquivo']

                    historico = Materiais.carregar_json(DOWNLOADS)
                    historico.append(selecionado)
                    Materiais.salvar_json(DOWNLOADS, historico)
                    print("\033[32mHistórico atualizado com sucesso!\033[m\n")

                    print(f"\n\033[32mAbrindo arquivo: {caminho_arquivo}\033[m\n")
                    os.startfile(caminho_arquivo)
                    print(f"\n\033[32m{tipo} de {disciplina} baixado com sucesso!\033[m\n")
                else:
                    print("\033[31mNÚMERO INVÁLIDO!\033[m\n")
            
            elif opcao == 0:
                utils.limpar()
                break
            else:
                utils.limpar()
                print("\033[31mOPÇÃO INVÁLIDA!\033[m\n")

    def vermateriais():
        utils.limpar()
        titulover = '\033[36mVER MATERIAIS\033[m'
        print(titulover.center(50, '='),'\n\n')
        
        historico = Materiais.carregar_json(DOWNLOADS)

        if not historico:
            print("\033[31mNenhum material baixado ainda!\033[m\n")
            return
        
        for i, m in enumerate(historico, start=1):
            print(f"{i}. {m['tipo']} - {m['disciplina']} - {m['professor']} - {m['arquivo']}")
        input("\nPressione Enter para voltar ao menu...")
