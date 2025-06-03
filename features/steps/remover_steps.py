from behave import given, when, then
from src.app import app as flask_app
from src.models.pessoa import Pessoa
from src.database import db
from datetime import date

def gerar_cpf_unico(nome):
    return ''.join([str(ord(c) % 10) for c in nome[:11]]).ljust(11, '0')[:11]

@given('que exista uma pessoa cadastrada com nome "{nome}" e sobrenome "{sobrenome}"')
def step_criar_pessoa(context, nome, sobrenome):
    with flask_app.app_context():
        # Remove possíveis duplicatas
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

@given('que não exista uma pessoa com ID 9999')
def step_pessoa_inexistente(context):
    pass  # O before_scenario já garantiu o banco limpo

@when('eu acesso a rota de remoção dessa pessoa')
@when('eu tento acessar a rota de remoção dessa pessoa')
def step_remover_pessoa(context):
    id_para_remover = getattr(context, 'pessoa_id', 9999)
    with flask_app.test_client() as client:
        context.response = client.get(
            f"/remover/{id_para_remover}",
            follow_redirects=True
        )

@then('o sistema deve exibir a mensagem "{mensagem}"')
def step_verifica_mensagem(context, mensagem):
    response_text = context.response.get_data(as_text=True)
    assert mensagem in response_text, (
        f'Mensagem esperada: "{mensagem}"\n'
        f'Mensagem recebida: {response_text[:500]}...'
    )