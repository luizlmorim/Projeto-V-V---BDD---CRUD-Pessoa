from flask import Flask, render_template, request, redirect, url_for, flash
from src.models.pessoa import Pessoa
from src.controllers.pessoa_controller import PessoaController
from src.database import db, init_app
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Gera uma chave segura
#app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Inicializa o banco de dados
init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_pessoa():
    if request.method == 'POST':
        try:
            PessoaController.salvar_pessoa(
                request.form['nome'],
                request.form['sobrenome'],
                request.form['cpf'],
                request.form['data_nascimento']
            )
            flash('Pessoa cadastrada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as e:
            flash(str(e), 'danger')  # Aqui está a correção principal

    max_date = date.today().isoformat()
    min_date = "1900-01-01"
    return render_template('cadastrar.html', max_date=max_date, min_date=min_date)



@app.route('/listar')
def listar_pessoas():
    pessoas = Pessoa.query.all()
    return render_template('listar.html', pessoas=pessoas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    if request.method == 'POST':
        try:
            PessoaController.atualizar_pessoa(
                pessoa,
                request.form['nome'],
                request.form['sobrenome'],
                request.form['cpf'],
                request.form['data_nascimento']
            )
            flash('Pessoa atualizada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except ValueError as e:
            flash(str(e), 'danger')
        except Exception as e:
            flash(f'Erro inesperado: {str(e)}', 'danger')

    max_date = date.today().isoformat()
    return render_template('editar.html', pessoa=pessoa, max_date=max_date)



@app.route('/remover/<int:id>')
def remover_pessoa(id):
    try:
        pessoa = Pessoa.query.get_or_404(id)
        db.session.delete(pessoa)
        db.session.commit()
        flash('Pessoa removida com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover: {str(e)}', 'danger')
    return redirect(url_for('listar_pessoas'))

if __name__ == '__main__':
    app.run(debug=True)