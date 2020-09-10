from src import db, bcrypt
from src.utils.short_uuid import genereate_uuid


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.String(15), primary_key=True, default=genereate_uuid)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    pw_hash = db.Column(db.String(80), nullable=False)

    def set_password(self, password):
        self.pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.pw_hash, password)
