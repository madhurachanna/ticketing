from src import session
from src.models.orders import Order


def order_by_ticket_status(ticket_id, status=[]):
    if len(status) > 0:
        order = session.query(Order).filter_by(ticket_id=ticket_id).first()
        return order
    order = (
        session.query(Order)
        .filter(Order.ticket_id == ticket_id, Order.ticket_id.in_(status))
        .first()
    )
    return order


def create_new_order(odr):
    order = Order(**odr)
    session.add(order)
    session.commit(order)
    return order
