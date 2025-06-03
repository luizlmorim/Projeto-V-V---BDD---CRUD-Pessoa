# language: pt
Funcionalidade: Edição de pessoas
  Como usuário do sistema
  Eu quero editar os dados de uma pessoa cadastrada
  Para manter as informações sempre atualizadas

  Cenário: Edição com dados válidos
    Dado que exista uma pessoa cadastrada com nome "Carlos" e sobrenome "Silva"
    Quando eu altero o nome para "Carlos Henrique", o sobrenome para "Souza", o CPF para "98765432100" e a data de nascimento para "1995-10-10"
    Então o sistema deve atualizar a pessoa e exibir a mensagem "Pessoa atualizada com sucesso!"

  Cenário: Edição com campo nome vazio
    Dado que exista uma pessoa cadastrada com nome "Luciana" e sobrenome "Alves"
    Quando eu altero o nome para " ", o sobrenome para "Alves", o CPF para "17345678901" e a data de nascimento para "1985-02-15"
    Então o sistema deve exibir a mensagem de erro "Nome é obrigatório"

  Cenário: Edição com CPF inválido
    Dado que exista uma pessoa cadastrada com nome "Bruno" e sobrenome "Ferraz"
    Quando eu altero o nome para "Bruno", o sobrenome para "Ferraz", o CPF para "77788877714" e a data de nascimento para "1980-08-20"
    Então o sistema deve exibir a mensagem de erro "CPF inválido"

  Cenário: Edição com data futura
    Dado que exista uma pessoa cadastrada com nome "Paula" e sobrenome "Melo"
    Quando eu altero o nome para "Paula", o sobrenome para "Melo", o CPF para "122233344" e a data de nascimento para "2100-01-01"
    Então o sistema deve exibir a mensagem de erro "Data de nascimento inválida"
