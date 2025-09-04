from flask import render_template, request, redirect, url_for
# from models import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models.task import Task
# from models.user import User
# from models.user import User, db


class TaskController:

    @staticmethod
    def list_tasks():
        # if request.method == 'GET':
        tasks = Task.query.all()
        return render_template('tasks.html', tasks=tasks)
        # TODO buscar todas as tarefas do banco de dados
        # tasks = None 
        # return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':

            title = request.form['title']
            status = request.form['status']
            description = request.form['description']
            user_id = request.form['user_id']


            existing_task= Task.query.filter_by(title=title).first()
            if existing_task:
                return render_template('contact.html', error="Task já existe", title=title)
            
            new_task = Task(title=title, status=status, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()


            return redirect(url_for("tasks"))

        return render_template("create_task.html")
  
    @staticmethod
    def update_task_status(task_id):
        # TODO buscar a tarefa pelo id
        # TODO: se existir, alternar status entre "Pendente" e "Concluído" e dar commit na alteração
        pass 

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        
        # TODO buscar a tarefa pelo id
        # TODO: se ela existir, remover do db.session e dar commit
        pass 
    
        return redirect(url_for("list_tasks"))