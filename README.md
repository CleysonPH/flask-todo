# Flask Todo

Um curd de trefas feito com Flask e algumas extenções

- Flask
- Flask-SQLAlchemy

## Requisitos

- Python 3.5
- Pipenv

## Como começar

Clone e ente na pasta do projeto

```sh
git clone https://github.com/CleysonPH/flask-todo.git
cd flask_todo
```

Instale os requisitos do projeto com o pipenv

```sh
pipenv install
```

## Como rodar esse projeto

Primeiro crie o banco de dados

```sh
python

>>> form model import db
>>> db.create_all()
```

Logo em seguida basta executar o arquivo ```app.py```

```sh
python app.py
```

E então acessar a aplicação em http://localhost:5000/