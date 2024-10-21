import json
from models import TicketModel


class Database:
    _tickets = []
        # TicketModel(id=1, title="None", type="Bug", status="Draft"),
        # TicketModel(id=2, title="None", type="Feature", status="Open"),
        # TicketModel(id=3, title="Do it", type="Epic", status="In progress"),
    
    def load_database(self):
        with open('db.json') as f:
            self._tickets = [TicketModel.model_validate(obj) for obj in json.load(f) ]

    @property
    def tickets(self):
        self.load_database()
        return self._tickets