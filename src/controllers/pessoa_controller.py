import re
from datetime import datetime, date
from flask import flash  # <- import necessário
from src.models.pessoa import Pessoa
from src.database import db

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False

    return True

class PessoaController:
    @staticmethod
    def salvar_pessoa(nome, sobrenome, cpf, data_nascimento):
        # Validação: nome obrigatório
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome é obrigatório")

        # Validação: nome até 50 caracteres
        if len(nome.strip()) > 50:
            raise ValueError("Nome excede o limite de caracteres")

        # Validação: sobrenome obrigatório
        if not sobrenome or len(sobrenome.strip()) == 0:
            raise ValueError("O sobrenome é obrigatório.")

        # Validação: CPF deve conter exatamente 11 dígitos numéricos
        cpf = cpf.strip()
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos")

        # Validação: CPF válido
        if not validar_cpf(cpf):
            raise ValueError("CPF inválido")

        # Validação: data de nascimento não pode ser futura
        try:
            data_nasc = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            if data_nasc > date.today():
                raise ValueError("Data de nascimento inválida")
        except ValueError:
            raise ValueError("Data de nascimento inválida")

        # Criação e salvamento da pessoa
        nova_pessoa = Pessoa(
            nome=nome.strip(),
            sobrenome=sobrenome.strip(),
            cpf=cpf,
            data_de_nascimento=data_nascimento
        )
        db.session.add(nova_pessoa)
        db.session.commit()

        # Mensagem de sucesso
        flash("Pessoa cadastrada com sucesso!", "success")

    @staticmethod
    def atualizar_pessoa(pessoa, nome, sobrenome, cpf, data_nascimento):
        if not nome.strip():
            raise ValueError("Nome é obrigatório")
        if len(nome) > 50:
            raise ValueError("O nome deve ter no máximo 50 caracteres.")
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome.strip()):
            raise ValueError("O nome deve conter apenas letras.")

        if not sobrenome.strip():
            raise ValueError("O sobrenome é obrigatório.")

        if not validar_cpf(cpf.strip()):
            raise ValueError("CPF inválido")

        # Valida data de nascimento
        try:
            data_obj = date.fromisoformat(data_nascimento)
            if data_obj > date.today():
                raise ValueError("Data de nascimento inválida")
        except ValueError:
            raise ValueError("Data de nascimento inválida")

        # Atualiza os dados
        pessoa.nome = nome.strip()
        pessoa.sobrenome = sobrenome.strip()
        pessoa.cpf = cpf.strip()
        pessoa.data_de_nascimento = data_nascimento
        db.session.commit()
