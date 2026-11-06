from bottle import template, request
from app.controllers.datarecord import DataRecord

class Application:
    """Controlador principal da aplicação BMVC."""
    def __init__(self):
        self.pages = {'portal': self.portal, 'banco': self.banco}
        self.models = DataRecord()

    def render(self, page, *args, **kwargs):
        content = self.pages.get(page, self.portal)
        return content(*args, **kwargs)

    def get_session_id(self):
        return request.get_cookie('session_id')

    def get_authenticated_username(self):
        user = self.models.get_user(self.get_session_id())
        return user.username if user else None

    def is_authenticated(self):
        return self.models.get_user(self.get_session_id()) is not None

    def authenticate_user(self, username, password):
        session_id = self.models.check_user(username, password)
        if session_id:
            return session_id, username
        return None, None

    def logout_user(self):
        self.models.logout(self.get_session_id())

    def portal(self, error=None):
        return template('app/views/html/portal', error=error)

    def banco(self, username):
        return template('app/views/html/banco', username=username,
                        objetos=self.models.list_items())

    def list_items(self):
        return self.models.list_items()

    def create_item(self, nome, plataforma):
        return self.models.create_item(nome, plataforma)

    def delete_item(self, item_id):
        return self.models.delete_item(item_id)
