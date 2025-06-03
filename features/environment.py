from src.app import app, db

def before_scenario(context, scenario):
    with app.app_context():
        db.drop_all()
        db.create_all()
        print(f"\n[DEBUG] Banco reiniciado para o cenário: {scenario.name}")

def after_scenario(context, scenario):
    with app.app_context():
        db.session.remove()