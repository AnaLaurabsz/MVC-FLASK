from app import db

class Task(db.Model):
    __tablename__ = "tasks"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False, default="Pendente")
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"