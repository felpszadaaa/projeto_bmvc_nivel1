class CatalogItem:
    """Objeto cadastrado no banco: catálogo de jogos."""
    def __init__(self, id, nome, plataforma):
        self.id = int(id)
        self.nome = nome
        self.plataforma = plataforma

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'plataforma': self.plataforma}
