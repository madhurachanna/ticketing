from src import session
from src.models.user import User


def add_new_user(usr):
    user = User(username=usr.username, email=usr.email)
    user.set_password(usr.password)
    session.add(user)
    session.commit()
    return user.serialize()


def get_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    return user
