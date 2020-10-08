from common.utils.short_uuid import genereate_uuid

from src import db


class Ticket(db.Model):

    __tablename__ = "ticket"

    id = db.Column(db.String(15), primary_key=True, default=genereate_uuid)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    version = db.Column(db.Integer(), default=1)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "version": self.version,
        }
