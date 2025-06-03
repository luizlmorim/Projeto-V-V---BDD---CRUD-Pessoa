# language: pt
Funcionalidade: Cadastro de pessoas
  Como usuário do sistema
  Eu quero cadastrar uma nova pessoa
  Para que seus dados sejam salvos corretamente

  Cenário: Cadastro com dados válidos
    Dado que eu preenchi o formulário com nome "João", sobrenome "Silva", CPF "12345678901" e data de nascimento "2000-01-01"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem "Pessoa cadastrada com sucesso!"

  Cenário: Cadastro com CPF inválido
    Dado que eu preenchi o formulário com nome "Maria", sobrenome "Oliveira", CPF "12345678454" e data de nascimento "1995-05-10"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem de erro "CPF inválido"

  Cenário: Cadastro com nome vazio
    Dado que eu preenchi o formulário com nome " ", sobrenome "Lima", CPF "12345678909" e data de nascimento "1990-01-01"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem de erro "Nome é obrigatório"

  Cenário: Cadastro com data futura
    Dado que eu preenchi o formulário com nome "Ana", sobrenome "Souza", CPF "12345378901" e data de nascimento "2090-01-01"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem de erro "Data de nascimento inválida"

  Cenário: Cadastro com nome acima do limite de caracteres
    Dado que eu preenchi o formulário com nome "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", sobrenome "Lima", CPF "12345678902" e data de nascimento "1990-01-01"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem de erro "Nome excede o limite de caracteres"

  Cenário: Cadastro com CPF acima de 11 caracteres
    Dado que eu preenchi o formulário com nome "Pedro", sobrenome "Santos", CPF "1234567890193" e data de nascimento "1995-05-05"
    Quando eu envio o formulário de cadastro
    Então o sistema deve exibir a mensagem de erro "CPF deve conter exatamente 11 dígitos"

