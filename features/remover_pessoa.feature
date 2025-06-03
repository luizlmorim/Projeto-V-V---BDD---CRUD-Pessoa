# language: pt
Funcionalidade: Remoção de pessoas
  Como usuário do sistema
  Eu quero remover uma pessoa cadastrada
  Para eliminar dados desnecessários ou incorretos

  Cenário: Remover uma pessoa existente
    Dado que exista uma pessoa cadastrada com nome "Elisa" e sobrenome "Pereira"
    Quando eu acesso a rota de remoção dessa pessoa
    Então o sistema deve exibir a mensagem "Pessoa removida com sucesso!"

  Cenário: Tentar remover uma pessoa inexistente
    Dado que não exista uma pessoa com ID 9999
    Quando eu tento acessar a rota de remoção dessa pessoa
    Então o sistema deve exibir a mensagem "Erro ao remover"
