from flask import render_template, request, redirect, url_for
from app import db
from models.user import User
from models.task import Task

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_tasks():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']
            existing_tasks= Task.query.filter_by(title=title).first()
            if existing_tasks:
                return render_template('create_task.html', error="Task já existe", title=title)
            
            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("list_tasks"))

        users = User.query.all()
        return render_template("create_task.html", users=users)
  
    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get(task_id)
        task.status = "Concluido" if task.status == "Pendente" else task.status
        db.session.commit()

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
    
        return redirect(url_for("list_tasks"))