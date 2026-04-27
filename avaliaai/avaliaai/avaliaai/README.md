# 📚 AvaliAí

## 📖 Descrição

O **AvaliAí** é uma comunidade acadêmica desenvolvida com foco nos estudantes da UFRPE, especialmente do curso de **Bacharelado em Sistemas de Informação (BSI)**.

A plataforma permite que estudantes avaliem e consultem avaliações de **professores e disciplinas**, ajudando a compartilhar experiências acadêmicas e auxiliar outros alunos na escolha de disciplinas e docentes.

---

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

  ## 👤 Autores

- Nome: Guilherme Vasconcellos e Julia Galindo
- Curso: Bacharelado em Sistemas de Informação (BSI)
- Instituição: UFRPE

---

## 📌 Observações

- Nome de usuário é apenas identificador público
- E-mail deve ser institucional (@ufrpe.br)
- Projeto voltado para uso acadêmico