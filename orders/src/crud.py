from common.events.types.order_status import OrderStatus

from src import session
from src.models.orders import Order
from src.models.tickets import Ticket


def order_by_ticket_status(ticket_id, status=[]):
    order = (
        session.query(Order)
        .filter(Order.ticket_id == ticket_id, Order.ticket_id.in_(status))
        .first()
    )
    return order


def get_orders_by_user_id(user_id):
    orders = (
        session.query(Order, Ticket)
        .join(Ticket, Ticket.id == Order.ticket_id)
        .filter(Order.user_id == user_id)
        .all()
    )
    return orders


def create_order(odr):
    order = Order(**odr)
    session.add(order)
    session.commit()
    return order


def ticket_by_id(ticket_id):
    ticket = session.query(Ticket).filter_by(id=ticket_id).first()
    print(ticket, flush=True)
    return ticket


def order_by_reserved_ticket_id(ticket_id):
    status = (
        OrderStatus.Created,
        OrderStatus.AwaitingPayment,
        OrderStatus.Complete,
    )
    order = (
        session.query(Order)
        .filter(Order.ticket_id == ticket_id, Order.status.in_(status))
        .first()
    )
    return order


#
# Testing
#


def get_all_tickets():
    tickets = session.query(Ticket).all()
    return tickets


def create_ticket(tkt):
    print("tkt", tkt)
    ticket = Ticket(**tkt)
    session.add(ticket)
    session.commit()
    return ticket
