from src import db
from src.utils.short_uuid import genereate_uuid


class Ticket(db.Model):

    __tablename__ = "ticket"

    id = db.Column(db.String(15), primary_key=True, default=genereate_uuid)
    user_id = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "price": self.price,
        }
