from models import TicketModel


class Database:
    _tickets = [
        {
            'id': 1,
            'title': 'Ticket 1',
            'status': 'In progress',
        },
        {
            'id': 2,
            'title': 'Ticket 2',
            'status': 'Ready'
        },
        {
            'id': 3,
            'title': 'Ticket 3',
            'status': 'Draft'
        }   
    ]

    @property
    def tickets(self):
        return self._tickets