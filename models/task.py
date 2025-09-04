# from models import db
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from sqlalchemy.orm import relationship

class Task(db.Model):
    __tablename__ = "tasks"


    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), default='Pendente',nullable=False)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)




    # # TODO: Define os campos e o relacionamento da tabela Task
    # id = Column(String,nullabel = False, Primarykey = True)
    # title = Column(String, nullabel=False)
    # description = Column(String, nullable= True)
    # user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    # status = Column(String, default='Pendente')
    user = relationship("User", back_populates="task")

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"