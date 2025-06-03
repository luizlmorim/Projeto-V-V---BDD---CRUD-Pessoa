from behave import given, when, then
from src.app import app as flask_app
from src.models.pessoa import Pessoa
from src.database import db
from datetime import date

def gerar_cpf_unico(nome):
    """Gera CPF único baseado no nome"""
    return ''.join([str(ord(c) % 10) for c in nome[:11]]).ljust(11, '0')[:11]

@given('que TENHA uma pessoa cadastrada com nome "{nome}" e sobrenome "{sobrenome}"')
def step_setup_pessoa(context, nome, sobrenome):
    with flask_app.app_context():
        # Remove pessoas existentes com mesmo nome
        Pessoa.query.filter_by(nome=nome).delete()
        
        pessoa = Pessoa(
            nome=nome,
            sobrenome=sobrenome,
            cpf=gerar_cpf_unico(nome),
            data_de_nascimento=date(1990, 1, 1)
        )
        db.session.add(pessoa)
        db.session.commit()
        context.pessoa_id = pessoa.id

@when('eu altero o nome para "{nome}", o sobrenome para "{sobrenome}", o CPF para "{cpf}" e a data de nascimento para "{data_nascimento}"')
def step_editar_pessoa(context, nome, sobrenome, cpf, data_nascimento):
    with flask_app.test_client() as client:
        context.response = client.post(
            f"/editar/{context.pessoa_id}",
            data={
                "nome": nome,
                "sobrenome": sobrenome,
                "cpf": cpf,
                "data_nascimento": data_nascimento
            },
            follow_redirects=True
        )

@then('o sistema deve atualizar a pessoa e exibir a mensagem "{mensagem}"')
def step_mensagem_sucesso(context, mensagem):
    response_text = context.response.get_data(as_text=True)
    assert mensagem in response_text, (
        f'Mensagem esperada: "{mensagem}"\nMensagem recebida: {response_text[:500]}...'
    )

@then('o sistema deve exibir a mensagem de erro "{mensagem}"')
def step_mensagem_erro(context, mensagem):
    response_text = context.response.get_data(as_text=True)
    assert mensagem in response_text, (
        f'Mensagem esperada: "{mensagem}"\nMensagem recebida: {response_text[:500]}...'
    )
