<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Banco | GameBox</title><link rel="stylesheet" href="/static/css/main.css">
</head>
<body>
  <header class="topbar"><a class="brand" href="/banco">GameBox</a>
    <div class="user-area"><span>Olá, {{username}}</span>
      <form action="/logout" method="post"><button class="button-secondary" type="submit">Sair</button></form>
    </div>
  </header>
  <main class="content">
    <h1>Catálogo de jogos</h1>
    <p class="subtitle">Lista de objetos cadastrados no banco de dados.</p>
    <section class="table-card">
      <table><thead><tr><th>ID</th><th>Nome do jogo</th><th>Plataforma</th></tr></thead>
      <tbody>
        % if objetos:
          % for objeto in objetos:
            <tr><td>{{objeto['id']}}</td><td>{{objeto['nome']}}</td><td>{{objeto['plataforma']}}</td></tr>
          % end
        % else:
          <tr><td colspan="3" class="empty">Nenhum jogo cadastrado.</td></tr>
        % end
      </tbody></table>
    </section>
  </main>
</body>
</html>
