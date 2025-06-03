# language: pt
Funcionalidade: Listagem de pessoas
  Como usuário do sistema
  Eu quero visualizar a lista de pessoas cadastradas
  Para verificar os dados registrados

  Cenário: Lista com pessoas cadastradas
    Dado que existem pessoas cadastradas no sistema
    Quando eu acesso a página de listagem
    Então o sistema deve exibir o nome "João da Silva"
    E o CPF "12345078901"

  Cenário: Lista vazia
    Dado que não existam pessoas cadastradas no sistema
    Quando eu acesso a página de listagem
    Então o sistema deve exibir a mensagem "Nenhuma pessoa cadastrada"
