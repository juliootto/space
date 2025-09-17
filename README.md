# Projeto Space Website

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 🚀 Sobre o Projeto

**Space** é um site com temática espacial que desenvolvi para demonstrar minhas habilidades com o framework Django e tecnologias front-end. Este projeto foi criado como uma peça para o meu portfólio de desenvolvedor.

Nessa aplicação o usuário pode fazer um cadastro e após o login pode acessar uma galeria de imagens de artefatos espaciais.

**Acesse o site:** [space.juliootto.online](https://space.juliootto.online/)

## ✨ Funcionalidades Principais

* **Página Inicial:** Galeria dee imagens espaciais, onde o usuário tem que estar logado para acessar.
* **Login:** Autenticação d um usuário anteriormente cadastrado.
* **Cadastro:** Cadastro de um novo usuário.
* **Logout:** Logout do usuário autenticado.
* **Busca:** Sistema de busca de imagens espaciais.
* **Edição de Fotografias:** Funcionalidade para alterar os detalhes das fotografias.
* **Exclusão de Fotografias:** Funcionalidade para remover fotografias.
* **Armazenamento em Nuvem:** Assets e mídias armazenados no Cloudinary.
* **Login Social:** Opção de login com OAuth2.0 do Google e GitHub.


## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Backend:**
    * Python
    * Django
* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
    * Python
* **Banco de Dados:**
    SQLite

## ⚙️ Como Executar o Projeto Localmente

Para clonar e executar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/juliootto/space.git
    cd space
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **(Opcional) Crie um superusuário para acessar o painel de administração:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Abra seu navegador e acesse `http://127.0.0.1:8000/`. Para o painel admin, acesse `http://127.0.0.1:8000/admin`.

## 👨‍🚀 Autor

Projeto desenvolvido por **Julio Otto**.

* LinkedIn: [https://www.linkedin.com/in/julio-cezar-otto-junior-b184502/](https://www.linkedin.com/in/julio-cezar-otto-junior-b184502/)
* GitHub: [https://github.com/juliootto](https://github.com/juliootto)
* Email: juliootto@gmail.com
