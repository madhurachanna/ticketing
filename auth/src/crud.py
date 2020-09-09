from src import session
import src.models as M


def get_user_by_email(email):
    print(email)
    user = session.query(M.User).filter_by(email=email).first()
    return user
