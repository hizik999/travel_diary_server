import json
from models import TicketModel


class Database:
    _tickets = []
    _filename = 'db.json'
        # TicketModel(id=1, title="None", type="Bug", status="Draft"),
        # TicketModel(id=2, title="None", type="Feature", status="Open"),
        # TicketModel(id=3, title="Do it", type="Epic", status="In progress"),
    
    def load_database(self):
        with open(self._filename, 'r') as f:
            self._tickets = [TicketModel.model_validate(obj) for obj in json.load(f)]


    def save_database(self):
        with open(self._filename, 'w') as f:
            json.dump([obj.model_dump() for obj in self._tickets], f, indent=4)

    @property
    def tickets(self):
        return self._tickets
    

    def append(self, item: TicketModel):
        self._tickets.append(item)
        self.save_database()