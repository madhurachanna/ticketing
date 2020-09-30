from src import session
from src.models.tickets import Ticket


def ticket_by_id(ticket_id):
    ticket = session.query(Ticket).filter_by(id=ticket_id).first()
    print(ticket, flush=True)
    return ticket
