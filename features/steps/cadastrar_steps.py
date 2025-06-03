from behave import given, when, then
from src.app import app as flask_app
from src.models.pessoa import Pessoa


@given('que eu preenchi o formulário com nome "{nome}", sobrenome "{sobrenome}", CPF "{cpf}" e data de nascimento "{data_nascimento}"')
def step_preencher_formulario(context, nome, sobrenome, cpf, data_nascimento):
    # Armazena os dados no contexto para uso posterior
    context.form_data = {
        'nome': nome,
        'sobrenome': sobrenome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    }

@when("eu envio o formulário de cadastro")
def step_enviar_formulario(context):
    with flask_app.test_client() as client:
        response = client.post("/cadastrar", data=context.form_data, follow_redirects=True)
        context.response = response
        
        # Debug: imprime o status e parte do conteúdo da resposta para ajudar a identificar problemas
        print(f"Status code: {response.status_code}")
        print(f"Resposta (resumo): {response.get_data(as_text=True)[:500]}")  # Imprime os primeiros 500 caracteres do HTML

@then('o sistema tem que exibir a mensagem de erro "{mensagem}"')
def step_verificar_mensagem(context, mensagem):
    response_text = context.response.get_data(as_text=True)
    print(f"Checando mensagem esperada: '{mensagem}' no HTML...")
    print(f"Conteúdo da resposta: {response_text[:500]}")  # Mostra parte do conteúdo para facilitar o debug
    assert mensagem in response_text, f'''
     Mensagem esperada: "{mensagem}"
     Mensagem recebida: {response_text}
    '''

