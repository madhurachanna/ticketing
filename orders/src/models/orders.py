from datetime import datetime, timedelta
from common.utils.short_uuid import genereate_uuid
from common.events.types.order_status import OrderStatus

from src import db


class Order(db.Model):

    __tablename__ = "order"

    id = db.Column(db.String(15), primary_key=True, default=genereate_uuid)
    user_id = db.Column(db.String(20), nullable=False)
    status = db.Column(
        db.Enum(OrderStatus), nullable=False, default=OrderStatus.Created
    )
    expires_at = db.Column(
        db.DateTime, default=(datetime.now() + timedelta(minutes=15))
    )
    ticket_id = db.Column(db.String(15), db.ForeignKey("ticket.id"), nullable=False)
    version = db.Column(db.Integer(), default=1)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "status": self.status.value,
            "expires_at": self.expires_at,
            "version": self.version,
            "ticket_id": self.ticket_id,
        }
