# agenda-django

- Primeiramente clone o repositório, com o comando:

```
  git clone https://github.com/PedroRyago/agenda-django.git
```

- Em seguida entre na pasta do projeto, com o comando:

```
  cd agenda-django
```

- Logo após, rode o comando abaixo para gerar um ambiente virtual:

```
  python3 -m venv venv
```

- Rode o comando abaixo para ativar a virtual env:

```
  venv/Scripts/Activate
```


-  A seguir, instale as dependências do projeto com o comando:

```
  pip install -r requirements.txt
```

- Sincronize a base de dados:

```
  python manage.py migrate
```

- Crie um usuário (Administrador do sistema):

```
  python manage.py createsuperuser
```

- Por fim rode o comando abaixo para rodar o sistema:

```
  python manage.py runserver
```

- Pronto, agora você pode acessar o projeto no seu navegador, com o link:

```
  http://127.0.0.1:8000/
```
