from flask import render_template, request, redirect, url_for
from models.user import User, db
class UserController:

    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    @staticmethod
    def create_users():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template('create_users', error="Usuário com este e-mail já existe", name=name, email=email)

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('create_user.html')