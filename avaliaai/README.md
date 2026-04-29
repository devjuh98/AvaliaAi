# 📚 AvaliAí

## 📖 Descrição

O **AvaliAí** é uma comunidade acadêmica desenvolvida com foco nos estudantes da UFRPE, especialmente do curso de **Bacharelado em Sistemas de Informação (BSI)**.

A plataforma permite que estudantes avaliem e consultem avaliações de **professores e disciplinas**, ajudando a compartilhar experiências acadêmicas e auxiliar outros alunos na escolha de disciplinas e docentes.

---

## ✨ Release 1

## ⚙️ Funcionalidades

### 🔐 Autenticação
- Cadastro de usuário
- Login
- E-mail institucional obrigatório (@ufrpe.br)

---

### 🧑‍💻 Gestão de conta
- Visualizar dados da conta
- Editar nome de usuário, senha e e-mail
- Deletar conta

> ⚠️ O nome de usuário não precisa ser o nome real, ele serve como identidade pública na plataforma.

---

### ⭐ Avaliações
- Avaliar professores
- Avaliar disciplinas

#### 👨‍🏫 Avaliação de professores:
O usuário digita o professor e atribui notas de **1 a 5** para:
- Dificuldade de avaliação
- Didática
- Organização

Após a avaliação, é possível continuar avaliando outro professor.

---

#### 📘 Avaliação de disciplinas:
O usuário digita a disciplina e atribui notas de **1 a 5** para:
- Nível de dificuldade
- Carga de trabalho
- Utilidade do conteúdo

Após a avaliação, é possível continuar avaliando outra disciplina.

---

### 🔎 Consulta de avaliações
- Buscar avaliações de professores ou disciplinas
- Exibição das avaliações existentes
- Cálculo da média das notas atribuídas pelos estudantes

---

## 🧭 Fluxo do sistema

1. Cadastro, login ou sair
2. Menu principal:
   - Fazer avaliação
   - Checar avaliações
   - Editar dados
   - Ver dados
   - Deletar conta
   - Voltar

### Fazer avaliação:
- Escolher entre:
  - Professor
  - Disciplina

### Checar avaliações:
- Escolher entre:
  - Professor
  - Disciplina

### Editar dados:
- Alterar:
  - Nome de usuário
  - Senha
  - Email

### Ver dados:
- Exibir informações da conta

### Deletar conta:
- Remover conta do sistema

---

## 🎯 Objetivo

O AvaliAí tem como objetivo facilitar a troca de experiências entre estudantes, permitindo decisões mais informadas sobre professores e disciplinas dentro da universidade.

## 🛠️ Tecnologias

O projeto foi desenvolvido em **Python puro**, sem uso de bibliotecas externas.

Bibliotecas padrão utilizadas:
- json → utilizado como banco de dados (usuários, professores, disciplinas e avaliações)
- os → utilizado para limpar o terminal
- msvcrt → utilizado para ocultar a senha digitada (exibindo asteriscos)

---

## 📁 Estrutura do projeto

O sistema foi organizado em múltiplos arquivos para melhor organização e separação de responsabilidades:

```
avaliaai/
│
├── modulo/
│ ├── main.py # Inicialização do programa
│ ├── usuarios.py # Cadastro, login e gestão de conta
│ ├── avaliacoes.py # Avaliações de professores e disciplinas
│ ├── menus.py # Menus e interface do sistema
│ ├── utils.py # Funções auxiliares e validações
│ │
│ ├── usuarios.json
│ ├── professores.json
│ ├── disciplinas.json
│ ├── avaliacoes_professores.json
│ └── avaliacoes_disciplinas.json
│
├── README.md
└── .gitignore
```

- main.py  
  Responsável por iniciar o programa e exibir o menu principal

- usuarios.py  
  Funções relacionadas ao usuário:
  - cadastro
  - login
  - edição de dados
  - visualização de dados
  - deleção da conta

- avaliacoes.py  
  Funções para:
  - fazer avaliações de professores e disciplinas
  - consultar avaliações existentes

- menus.py  
  Contém os menus e interfaces de interação com o usuário

- utils.py  
  Funções auxiliares como:
  - exibição de títulos
  - validações (senha, nome de usuário e e-mail)

- arquivos JSON  
  Funcionam como banco de dados do sistema:
  - usuários
  - professores
  - disciplinas
  - avaliações

---

## ▶️ Como executar o projeto

1. Clone o repositório:
git clone https://github.com/devjuh98/AvaliaAi.git

2. Acesse a pasta do projeto:
cd avaliaai/modulo

3. Execute o programa:
python main.py

---

## 👤 Autores

- Nome: Guilherme Vasconcellos e Julia Galindo
- Curso: Bacharelado em Sistemas de Informação (BSI)
- Instituição: UFRPE

---

## ⚠️ Compatibilidade

Este projeto foi desenvolvido para ambiente **Windows**, pois utiliza:

- `msvcrt` → para ocultar a senha digitada
- `os.system("cls")` → para limpeza do terminal

Em outros sistemas operacionais (Linux/Mac), pode ser necessário adaptar essas funcionalidades.

---

## 📌 Observações

- Nome de usuário é apenas identificador público
- E-mail deve ser institucional (@ufrpe.br)
- Projeto voltado para uso acadêmico

## 📂 Documentação e materiais:

### Fluxograma e tabela de releases:

https://drive.google.com/drive/folders/1vs4vysRpAu1jHy6zEYa825FsklT6P2o7?usp=sharing

### 🎥 Vídeos explicativos

- 🎬 Vídeo geral do projeto (Guilherme Vasconcellos Valois):
  [Assistir vídeo](https://youtu.be/-62mFNtz07E)

- 🎬 Vídeo geral do projeto (Julia Galindo de Carvalho Cardoso):
  [Assistir vídeo](COLOQUE_O_LINK_AQUI)

---

## 🚀 Futuras Releases

### 🔄 Release 2

Novas funcionalidades planejadas para expandir o sistema:

#### 👨‍💼 Administração
- Login de administrador
- Menu exclusivo para administradores

#### 📚 Materiais de aula
- Upload de provas e trabalhos
- Download de materiais compartilhados por outros usuários

#### 📊 Análises acadêmicas
- Visualização do nível de dificuldade do período
- Estatísticas de:
  - Aprovação
  - Reprovação

---

### 🌟 Release 3

A definir