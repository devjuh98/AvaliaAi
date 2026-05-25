import menus 
import usuarios 
import utils
import json

class Usuario:  
    def __init__(self, nome, email, senha, status='ativo'):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status

    def para_dicionario(self):
        return{
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'status': self.status
        }
    
    def cadastrar(self):
        '''Função para realizar o cadastro do usuário,
        armazenando os dados em um json e em uma lista
        sem parâmetros de entrada e sem retorno.'''
        usuarios.usuarioslist.append(self)
        with open(usuarios.ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
            json.dump([usuario.para_dicionario() for usuario in usuarios.usuarioslist], arq, indent = 4, ensure_ascii=False)
        
    def editar_nome(self, novo_nome):
        '''Função para editar o nome do usuário,
        recebe o usuário logado e o novo nome como parâmetros de entrada e retorna True (Atualizado) ou False (Não atualizado).'''
        for usuario in usuarios.usuarioslist:
            if usuario.email == self.email:
                usuario.nome = novo_nome.strip()
                with open(usuarios.ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
                    json.dump([usuario.para_dicionario() for usuario in usuarios.usuarioslist], arq, indent = 4, ensure_ascii=False)
                print("\033[32mNome atualizado com sucesso!\n\033[m")
                input("Pressione Enter para voltar ao menu...")
                return True
        return False
    
    def editar_email(self, novo_email):
        '''Função para editar o email do usuário,
        recebe o usuário logado e o novo email como parâmetros de entrada e retorna True (Atualizado) ou False (Não atualizado).'''
        for usuario in usuarios.usuarioslist:
            if usuario.email == self.email:
                usuario.email = novo_email.strip().lower()
                with open(usuarios.ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
                    json.dump([usuario.para_dicionario() for usuario in usuarios.usuarioslist], arq, indent = 4, ensure_ascii=False)
                print("\033[32mEmail atualizado com sucesso!\n\033[m")
                input("Pressione Enter para voltar ao menu...")
                return True
        return False
    
    def editar_senha(self, nova_senha):
        '''Função para editar a senha do usuário,
        recebe o usuário logado e a nova senha como parâmetros de entrada e retorna True (Atualizada) ou False (Não atualizada).'''
        for usuario in usuarios.usuarioslist:
            if usuario.email == self.email:
                usuario.senha = nova_senha.strip()
                with open(usuarios.ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
                    json.dump([usuario.para_dicionario() for usuario in usuarios.usuarioslist], arq, indent = 4, ensure_ascii=False)
                print("\033[32mSenha atualizada com sucesso!\n\033[m")
                input("Pressione Enter para voltar ao menu...")
                return True
        return False
    
    def deletar_conta(self):
        '''Função para deletar a conta do usuário,
        recebe o usuário logado como parâmetro de entrada e retorna True (Deletada) ou False (Não deletada).'''
        for usuario in usuarios.usuarioslist:
            if usuario.email == self.email:
                usuarios.usuarioslist.remove(usuario)
                with open(usuarios.ARQUIVOUSUARIOS, 'w', encoding='utf-8') as arq:
                    json.dump([usuario.para_dicionario() for usuario in usuarios.usuarioslist], arq, indent = 4, ensure_ascii=False)
                print("\033[32mCONTA DELETADA COM SUCESSO!\n\033[m")
                return True
        return False
    
    def ver_dados(self):
        '''Função para exibir os dados do usuário logado,
        recebe o usuário logado como parâmetro de entrada e sem retorno.'''
        utils.limpar()
        print("\033[34mINFORMAÇÕES DO USUÁRIO:\n\033[m")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}") 
        print(f"Senha: {utils.ver_senha_com_asterisco(self.senha)}")
        print(f"Status: {self.status}")
        print("\n\033[32mDigite 0 para voltar ao menu.\n\033[m")
        while True:
            opcao = input()
            if opcao.strip() == '0':
                utils.limpar()
                return
            else:
                print("\033[31mOpção inválida. Digite 0 para voltar ao menu.\n\033[m")