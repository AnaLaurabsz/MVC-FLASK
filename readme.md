# 🚀 Gerenciador de Tarefas - Aplicação Web com Flask e MVC
Aplicação web para cadastro e listagem de jogos, desenvolvida em Python com o framework Flask. O projeto segue a arquitetura **MVC (Model-View-Controller)** para organizar o código de forma clara e escalável.

O sistema conta com autenticação de usuários, permitindo que apenas usuários logados possam cadastrar novos jogos.


## ✨ Funcionalidades Principais

A aplicação permite o gerenciamento completo de Usuários e Tarefas associadas a eles, implementando um relacionamento de "um-para-muitos" (um usuário pode ter várias tarefas).

* **Gerenciamento de Usuários:**
    * Listagem de usuários:  Visualização de todos os usuários cadastrados no banco de dados .
    * Criação de usuários Formulário para adicionar novos usuários ao sistema.

* **Gerenciamento de Tarefas:**
    * Listagem de tarefas:  Visualização de todos os usuários cadastrados no banco de dados .
    * Criação de tarefas: Formulário para adicionar novos usuários ao sistema.
    *Atualização de tarefas: Permite alterar o status de uma tarefa entre 'Pendente' e 'Concluído' diretamente da lista.
    * Exclusão de tarefas: Permite remover uma tarefa do banco de dados.



## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * **Python**
    * **Flask**: Framework web para a construção da aplicação.
* **Banco de Dados:**
    * **SQLite**: Sistema de gerenciamento de banco de dados relacional.
    * **SQLAlchemy**: Mapeador (ORM), permite interagir com bancos de dados SQL usando Python.
* **Frontend:**
    * HTML5
    * CSS3 (em breve)

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto em sua máquina local.


### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/AnaLaurabsz/MVC-FLASK.git](https://github.com/AnaLaurabsz/MVC-FLASK.git)
    cd MVC-FLASK
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python run.py
    ```

6.  Acesse a aplicação em seu navegador no endereço: `http://127.0.0.1:5000`

## 📁 Estrutura do Projeto (MVC)

O projeto está organizado seguindo o padrão Model-View-Controller:

* **`models/` (Model):** Contém as classes que representam as tabelas do banco de dados (`Task`, `Usuario`). É a camada de dados da aplicação.

* **`views.py` e `user_view.py` (Controller):** Contém a lógica da aplicação, definindo as rotas (URLs) e controlando o fluxo entre os Models e as Views.

* **`templates/` (View):** Contém os arquivos HTML que são renderizados para o usuário. É a camada de apresentação.
* **`run.py`:** Ponto de entrada da aplicação. Inicializa o Flask e as configurações.
