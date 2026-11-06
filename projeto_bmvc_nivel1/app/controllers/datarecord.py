import json
import uuid
from pathlib import Path
from app.models.user_account import UserAccount
from app.models.catalog_item import CatalogItem

DB_DIR = Path(__file__).resolve().parent / 'db'
USERS_FILE = DB_DIR / 'user_accounts.json'
ITEMS_FILE = DB_DIR / 'catalog_items.json'

class DataRecord:
    """Administrador dos dados JSON e das sessões autenticadas."""
    def __init__(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)
        self.authenticated_users = {}
        self.user_accounts = []
        self.items = []
        self.read_users()
        self.read_items()

    def read_users(self):
        if not USERS_FILE.exists():
            USERS_FILE.write_text(json.dumps([
                {'username': 'aluno', 'password': '123456'}
            ], ensure_ascii=False, indent=2), encoding='utf-8')
        data = json.loads(USERS_FILE.read_text(encoding='utf-8'))
        self.user_accounts = [UserAccount(**entry) for entry in data]

    def read_items(self):
        if not ITEMS_FILE.exists():
            ITEMS_FILE.write_text(json.dumps([
                {'id': 1, 'nome': 'Minecraft', 'plataforma': 'PC'},
                {'id': 2, 'nome': 'FIFA 25', 'plataforma': 'PlayStation'}
            ], ensure_ascii=False, indent=2), encoding='utf-8')
        data = json.loads(ITEMS_FILE.read_text(encoding='utf-8'))
        self.items = [CatalogItem(**entry) for entry in data]

    def check_user(self, username, password):
        for user in self.user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())
                self.authenticated_users[session_id] = user
                return session_id
        return None

    def get_user(self, session_id):
        return self.authenticated_users.get(session_id)

    def logout(self, session_id):
        self.authenticated_users.pop(session_id, None)

    def save_items(self):
        data = [item.to_dict() for item in self.items]
        ITEMS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    def list_items(self):
        return [item.to_dict() for item in self.items]

    def create_item(self, nome, plataforma):
        next_id = max((item.id for item in self.items), default=0) + 1
        item = CatalogItem(next_id, nome, plataforma)
        self.items.append(item)
        self.save_items()
        return item.to_dict()

    def delete_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                self.save_items()
                return True
        return False
