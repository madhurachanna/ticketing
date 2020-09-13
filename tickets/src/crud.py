from src import session
from src.models.ticket import Ticket
from src.errors.not_found_error import NotFoundError


def add_new_ticket(tkt):
    ticket = Ticket(**tkt)
    session.add(ticket)
    session.commit()
    return ticket.serialize()


def get_tickets():
    tickets = session.query(Ticket).all()
    return [i.serialize() for i in tickets]


def get_ticket(id):
    ticket = session.query(Ticket).filter_by(id=id).first()
    if ticket:
        return ticket.serialize()
    raise NotFoundError()
