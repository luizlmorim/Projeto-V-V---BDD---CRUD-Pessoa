from behave import given, when, then
from src.app import app as flask_app
from src.models.pessoa import Pessoa
from src.database import db
from datetime import date

@given('que existem pessoas cadastradas no sistema')
def step_criar_pessoas(context):
    with flask_app.app_context():
        # Limpa dados existentes
        Pessoa.query.delete()
        
        # Cadastra pessoas com CPFs únicos
        pessoas = [
            Pessoa(nome="João", sobrenome="Silva", cpf="11122233344", data_de_nascimento=date(1990, 1, 1)),
            Pessoa(nome="Maria", sobrenome="Santos", cpf="22233344455", data_de_nascimento=date(1985, 5, 10))
        ]
        db.session.add_all(pessoas)
        db.session.commit()

@given('que não existam pessoas cadastradas no sistema')
def step_limpar_pessoas(context):
    with flask_app.app_context():
        Pessoa.query.delete()
        db.session.commit()

@when('eu acesso a página de listagem')
def step_acessar_listagem(context):
    with flask_app.test_client() as client:
        context.response = client.get("/listar")

@then('o sistema deve exibir o nome "{nome}"')
def step_verificar_nome(context, nome):
    assert nome in context.response.get_data(as_text=True)

@then('o CPF "{cpf}"')
def step_verificar_cpf(context, cpf):
    assert cpf in context.response.get_data(as_text=True)

@then('sistema deve exibir a mensagem "{mensagem}"')
def step_verificar_mensagem_vazia(context, mensagem):
    assert mensagem in context.response.get_data(as_text=True)