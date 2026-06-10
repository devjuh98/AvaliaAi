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

### 👤 Usuário

1. Cadastro, login ou sair
2. Menu principal:

   * Fazer avaliação
   * Checar avaliações
   * Editar dados
   * Ver dados
   * Deletar conta
   * Materiais de aula
   * Índice de aprovação e reprovação
   * Nível de dificuldade do período
   * Voltar

#### Fazer avaliação:

* Escolher entre:

  * Professor
  * Disciplina

#### Checar avaliações:

* Escolher entre:

  * Professor
  * Disciplina

#### Editar dados:

* Alterar:

  * Nome de usuário
  * Senha
  * E-mail

#### Ver dados:

* Exibir informações da conta

#### Deletar conta:

* Remover conta do sistema

#### Materiais de aula:

* Usuário pode:

  * Fazer upload de materiais
  * Fazer download de materiais compartilhados

#### Índice de aprovação e reprovação:

* Usuário pode:

  * Escolher a disciplina
  * Consultar as taxas de aprovação e reprovação da disciplina
  * Visualizar gráficos estatísticos com as porcentagens correspondentes

#### Nível de dificuldade do período:

* Usuário pode:

  * Selecionar um período acadêmico
  * Consultar o nível de dificuldade estimado

---

### 👨‍💼 Administrador

1. Login como administrador
2. Menu principal:

   * Fazer avaliação
   * Checar avaliações
   * Editar dados
   * Ver dados
   * Deletar conta
   * Materiais de aula
   * Índice de aprovação e reprovação
   * Nível de dificuldade do período
   * Gerenciar disciplinas
   * Gerenciar professores
   * Voltar

#### Gerenciar disciplinas:

* Administrador pode:

  * Adicionar disciplinas
  * Editar disciplinas existentes
  * Remover disciplinas

#### Gerenciar professores:

* Administrador pode:

  * Adicionar professores
  * Editar professores existentes
  * Remover professores

> O administrador possui acesso a todas as funcionalidades disponíveis para usuários comuns, além de recursos adicionais voltados ao gerenciamento das informações acadêmicas presentes no sistema.

---
# 📚 AvaliAí

## 📖 Descrição

O **AvaliAí** é uma comunidade acadêmica desenvolvida com foco nos estudantes da UFRPE, especialmente do curso de **Bacharelado em Sistemas de Informação (BSI)**.

A plataforma permite que estudantes avaliem e consultem avaliações de **professores e disciplinas**, ajudando a compartilhar experiências acadêmicas e auxiliar outros alunos na escolha de disciplinas e docentes.

---

# 🚀 Releases

## ✨ Release 1 – Funcionalidades Essenciais

### 🔐 Autenticação

* Cadastro de usuário
* Login
* E-mail institucional obrigatório (`@ufrpe.br`)

### 🧑‍💻 Gestão de conta

* Visualizar dados da conta
* Editar nome de usuário, senha e e-mail
* Deletar conta

### ⭐ Avaliações

#### 👨‍🏫 Professores

* Avaliação de dificuldade das provas
* Avaliação da didática
* Avaliação da organização

#### 📘 Disciplinas

* Avaliação do nível de dificuldade
* Avaliação da carga de trabalho
* Avaliação da utilidade do conteúdo

### 🔎 Consulta de avaliações

* Buscar avaliações de professores
* Buscar avaliações de disciplinas
* Visualizar médias das avaliações

---

## 🚀 Release 2

### ✨ Novas funcionalidades implementadas

#### 👨‍💼 Administração

* Login de administrador
* Menu exclusivo para administradores
* Gerenciamento de recursos do sistema

---

#### 📚 Materiais de aula

* Upload de provas, trabalhos e materiais de estudo
* Download de materiais compartilhados por outros usuários
* Compartilhamento de conteúdos organizados pela comunidade acadêmica

---

#### 📊 Análises acadêmicas

* Visualização do nível de dificuldade do período
* Cálculo dos índices de aprovação e reprovação das disciplinas
* Geração automática de gráficos de pizza utilizando Matplotlib
* Exibição das porcentagens correspondentes aos índices calculados
* Utilização das cores verde para aprovação e vermelho para reprovação, facilitando a interpretação visual dos dados

---

#### 🏗️ Melhorias na arquitetura

* Migração da estrutura procedural para Programação Orientada a Objetos (POO)
* Implementação de classes específicas para entidades do sistema
* Melhor organização e manutenção do código-fonte

---


## 🎯 Objetivo

O AvaliAí tem como objetivo facilitar a troca de experiências entre estudantes, permitindo decisões mais informadas sobre professores e disciplinas dentro da universidade.

## 🛠️ Tecnologias

O projeto foi desenvolvido majoritariamente em Python puro, utilizando bibliotecas padrão da linguagem e algumas bibliotecas externas para funcionalidades específicas.

Bibliotecas padrão utilizadas:
- json → utilizado como banco de dados (usuários, professores, disciplinas e avaliações)
- os → utilizado para limpar o terminal
- msvcrt → utilizado para ocultar a senha digitada (exibindo asteriscos)
- tkinter → utilizado para criar GUIs 

Biblioteca externa:
- matplotlib → utilizada para geração de gráficos estatísticos de aprovação e reprovação das disciplinas
---

## 📁 Estrutura do projeto

O sistema foi organizado em módulos separados, visando facilitar a manutenção, organização e expansão do código-fonte.

```text
avaliai/
│
├── modulo/
│   │
│   ├── data/
│   │   ├── avaliacoes_disciplinas.json
│   │   ├── avaliacoes_professores.json
│   │   ├── disciplinas.json
│   │   ├── download.json
│   │   ├── professores.json
│   │   ├── upload.json
│   │   └── usuarios.json
│   │
│   ├── models/
│   │   ├── admin.py
│   │   ├── avaliacoes_disciplinas.py
│   │   ├── avaliacoes_professores.py
│   │   ├── disciplinas.py
│   │   ├── professores.py
│   │   └── usuario.py
│   │
│   ├── avaliacoes.py
│   ├── calculo_taxas.py
│   ├── funcoes_admin.py
│   ├── main.py
│   ├── materiais.py
│   ├── menus.py
│   ├── usuarios.py
│   └── utils.py
│
├── README.md
└── .gitignore
```

### Descrição dos componentes

- **main.py**  
  Responsável por iniciar a execução do sistema e controlar o fluxo principal do programa.

- **menus.py**  
  Contém os menus e interfaces de interação com o usuário.

- **usuarios.py**  
  Reúne as funcionalidades relacionadas ao cadastro, autenticação e gerenciamento das contas dos usuários.

- **avaliacoes.py**  
  Implementa as funções responsáveis pela realização e consulta das avaliações de professores e disciplinas e pela consulta de dificuldade do período.

- **materiais.py**  
  Gerencia o compartilhamento e acesso aos materiais acadêmicos disponibilizados pelos usuários.

- **funcoes_admin.py**  
  Contém funcionalidades exclusivas dos administradores do sistema.

- **calculo_taxas.py**  
  Responsável pelo cálculo dos índices estatísticos, como taxas de aprovação e reprovação das disciplinas.

- **utils.py**  
  Agrupa funções auxiliares, incluindo validações de dados, mascaramento de senha e recursos de apoio à interface do terminal.

- **models/**  
  Diretório destinado às classes utilizadas pelo sistema, implementadas utilizando os conceitos de Programação Orientada a Objetos (POO).

- **data/**  
  Diretório responsável pelo armazenamento persistente das informações do sistema por meio de arquivos JSON.
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

### 🎥 Vídeos explicativos RELEASE 1

- 🎬 Vídeo geral do projeto (Guilherme Vasconcellos Valois):
  [Assistir vídeo](https://youtu.be/-62mFNtz07E)

- 🎬 Vídeo geral do projeto (Julia Galindo de Carvalho Cardoso):
  [Assistir vídeo](https://youtu.be/Cv8_vHOg6wU?si=IhqB3ZmCY3UzSWX_)

---

### 🎥 Vídeos explicativos RELEASE 2

- 🎬 Vídeo geral do projeto (Guilherme Vasconcellos Valois):
  [Assistir vídeo](https://youtu.be/NjiN7mETmbg)

- 🎬 Vídeo geral do projeto (Julia Galindo de Carvalho Cardoso):
  [Assistir vídeo]()

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