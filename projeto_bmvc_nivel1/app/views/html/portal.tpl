<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal | GameBox</title><link rel="stylesheet" href="/static/css/main.css">
</head>
<body class="login-page">
  <main class="card login-card">
    <span class="eyebrow">BMVC · NÍVEL 1</span>
    <h1>GameBox</h1><p class="subtitle">Entre para acessar o catálogo de jogos.</p>
    % if error:
      <p class="error">{{error}}</p>
    % end
    <form action="/portal" method="post">
      <label for="username">Usuário</label>
      <input id="username" name="username" type="text" required autocomplete="username">
      <label for="password">Senha</label>
      <input id="password" name="password" type="password" required autocomplete="current-password">
      <button type="submit">Entrar</button>
    </form>
    <p class="hint">Acesso de demonstração: <strong>aluno</strong> / <strong>123456</strong></p>
  </main>
</body>
</html>
