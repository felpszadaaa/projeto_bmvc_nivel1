import os
from bottle import Bottle, run, request, response, redirect, static_file
from app.controllers.application import Application

app = Bottle()
ctl = Application()

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.get('/')
@app.get('/portal')
def portal():
    return ctl.portal()

@app.post('/portal')
def action_portal():
    username = request.forms.get('username', '').strip()
    password = request.forms.get('password', '')
    session_id, authenticated_username = ctl.authenticate_user(username, password)
    if session_id:
        response.set_cookie('session_id', session_id, httponly=True,
                            secure=False, samesite='Lax', max_age=3600, path='/')
        redirect('/banco')
    return ctl.portal(error='Usuário ou senha inválidos.')

@app.get('/banco')
def banco():
    username = ctl.get_authenticated_username()
    if not username:
        redirect('/portal')
    return ctl.banco(username)

@app.post('/logout')
def logout():
    ctl.logout_user()
    response.delete_cookie('session_id', path='/')
    redirect('/portal')

# API do recurso banco: CREATE e DELETE são realizados via cURL.
@app.get('/api/objetos')
def api_read():
    if not ctl.is_authenticated():
        response.status = 401
        return {'erro': 'Faça login para acessar o banco.'}
    return {'objetos': ctl.list_items()}

@app.post('/api/objetos')
def api_create():
    if not ctl.is_authenticated():
        response.status = 401
        return {'erro': 'Faça login para acessar o banco.'}
    data = request.json or {}
    nome = str(data.get('nome', '')).strip()
    plataforma = str(data.get('plataforma', '')).strip()
    if not nome or not plataforma:
        response.status = 400
        return {'erro': 'Informe nome e plataforma.'}
    item = ctl.create_item(nome, plataforma)
    response.status = 201
    return {'mensagem': 'Objeto cadastrado com sucesso.', 'objeto': item}

@app.delete('/api/objetos/<item_id:int>')
def api_delete(item_id):
    if not ctl.is_authenticated():
        response.status = 401
        return {'erro': 'Faça login para acessar o banco.'}
    if ctl.delete_item(item_id):
        return {'mensagem': 'Objeto removido com sucesso.', 'id': item_id}
    response.status = 404
    return {'erro': 'Objeto não encontrado.'}

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=int(os.environ.get('PORT', '8080')), debug=True, reloader=False)
