from datetime import date
from flask import render_template, redirect, url_for, request

from models import db, Todo
from utils import get_date_from_string


def configure(app):
    @app.errorhandler(404)
    def error_404(e):
        return render_template('404.html', title='Not Found'), 404


    @app.route('/')
    def home():
        todos = Todo.query.order_by(Todo.date).all()
        today = date.today()

        return render_template('home.html', title='Home', todos=todos, today=today)


    @app.route('/add/todo/', methods=['POST'])
    def add_todo():
        todo = Todo(
            request.form.get('todo-title'),
            get_date_from_string(request.form.get('todo-date')),
            request.form.get('todo-priority'),
        )

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('home'))


    @app.route('/edit/todo/<int:id>/', methods=['GET', 'POST'])
    def edit_todo(id):
        todo = Todo.query.get_or_404(id)
        if request.method == 'GET':
            return render_template('edit_todo.html', title='Edit Todo', todo=todo)

        todo.title = request.form.get('todo-title')
        todo.date = get_date_from_string(request.form.get('todo-date'))
        todo.priority = request.form.get('todo-priority')

        db.session.commit()
        
        return redirect(url_for('home'))


    @app.route('/remove/todo/<int:id>/')
    def remove_todo(id):
        todo = Todo.query.get_or_404(id)

        db.session.delete(todo)
        db.session.commit()

        return redirect(url_for('home'))
        