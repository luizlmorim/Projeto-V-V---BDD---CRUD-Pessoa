<h1>CRUD de Pessoas com Flask + Testes BDD</h1>

<p>Este projeto é um sistema web de cadastro, listagem, edição e remoção de pessoas,
desenvolvido com Flask e banco de dados SQLite, aplicando o ciclo completo de testes com
Behavior-Driven Development (BDD) usando o Behave.</p>

<h2>Funcionalidades</h2>

✅ Cadastro de nova pessoa (com validações de nome, CPF e data)

📝 Edição de dados existentes

📄 Listagem de pessoas cadastradas

🗑 Remoção de registros

🧪 Testes BDD automatizados com Behave + Flask Test Client

<h2>Testes BDD (Behavior Driven Development)</h2>
Os testes estão organizados por funcionalidade, usando a
linguagem Gherkin para simular o comportamento real do usuário:

📁 features/

cadastrar: testes para criação com validações (nome vazio, CPF inválido, etc.)

editar: testes para atualização com base em bugs reais identificados

remover: testes para exclusão e tratamento de erro para ID inexistente

ler: testes para visualização de registros e mensagem quando não houver d
