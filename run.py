from app import create_app, db

app = create_app()

# Opcional: para criar as tabelas ao iniciar
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5002)