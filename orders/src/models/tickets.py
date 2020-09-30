from common.utils.short_uuid import genereate_uuid
from common.events.types.order_status import OrderStatus

from src import db

from src.crud.orders import order_by_ticket_status


class Ticket(db.Model):

    __tablename__ = "ticket"

    id = db.Column(db.String(15), primary_key=True, default=genereate_uuid)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    version = db.Column(db.Integer(), default=1)

    def is_reserved(self):
        status = [
            OrderStatus.Created,
            OrderStatus.AwaitingPayment,
            OrderStatus.Complete,
        ]
        order = order_by_ticket_status(self.id, status)
        print(order)
        return "order"

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "version": self.version,
        }
