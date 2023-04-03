from crud import CRUD

class Query():
    def __init__(self, config):
        self.crud = CRUD(config)
