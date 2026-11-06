# GameBox — Projeto Modelagem Utilizando BMVC (Nível 1)

Projeto desenvolvido a partir da estrutura BMVC. O tema é um catálogo de jogos.


- **Portal:** login de usuários usando o modelo `UserAccount`.
- **Banco:** página protegida por autenticação que apresenta os objetos cadastrados (READ).
- **CREATE e DELETE:** operações realizadas pela API via cURL em terminal Linux/Windows.
- **Objeto cadastrado:** `CatalogItem`, com os atributos obrigatórios `nome` e `plataforma`, além de um identificador `id`.
- **Persistência:** dados armazenados em arquivos JSON dentro de `app/controllers/db/`.

## Como executar

Na pasta raiz do projeto, com Python3 instalado:

```bash
python3 -m pip install bottle
python3 route.py
```

Abra `http://localhost:8080/portal` no navegador.

**Login de demonstração**

- Usuário: `aluno`
- Senha: `123456`

Depois do login, o sistema redireciona para `/banco`, onde a lista de jogos é exibida.

### 1. Login e armazenamento do cookie de sessão

```bash
curl -i -c cookies.txt -X POST http://localhost:8080/portal \
  -d "username=aluno" -d "password=123456"
```

O arquivo `cookies.txt` guarda o cookie necessário para autenticar as operações.

### 2. CREATE — cadastrar um jogo

```bash
curl -i -b cookies.txt -X POST http://localhost:8080/api/objetos \
  -H "Content-Type: application/json" \
  -d '{"nome":"God of War Ragnarök","plataforma":"PlayStation 5"}'
```

### 3. READ — consultar os objetos pela API (além da página /banco)

```bash
curl -i -b cookies.txt http://localhost:8080/api/objetos
```

O READ exigido também está implementado na página `/banco`, que lista os registros cadastrados.

### 4. DELETE — excluir um jogo

Use o `id` retornado no CREATE. Por exemplo, se o ID for `3`:

```bash
curl -i -b cookies.txt -X DELETE http://localhost:8080/api/objetos/3
```

### 5. Verificar a exclusão

```bash
curl -b cookies.txt http://localhost:8080/api/objetos
```

A página não deverá mais conter o objeto excluído após executar tal procedimento. A página `/banco` também ira mostrar a lista atualizada ao recarregar.

## Estrutura BMVC

```text
route.py                         # Rotas HTTP e endpoints da API
app/
  controllers/
    application.py               # Controlador e regras de autenticação
    datarecord.py                # Persistência JSON e administração dos dados
    db/
      user_accounts.json         # Contas de acesso
      catalog_items.json         # Objetos do catálogo
  models/
    user_account.py              # Modelo UserAccount
    catalog_item.py              # Modelo CatalogItem
  views/html/
    portal.tpl                   # Tela de login
    banco.tpl                    # Listagem (READ)
    helper.tpl                   # Ajuda original do BMVC
  static/
    css/main.css
```

## Observações

- O login de demonstração está no arquivo `app/controllers/db/user_accounts.json`; altere a senha antes de qualquer uso real.
- As sessões ficam na memória no servidor e são perdidas quando ele é reiniciado.
- O cookie está configurado para funcionar em `localhost` por HTTP (`secure=False`). Em produção, use HTTPS e `secure=True`.
