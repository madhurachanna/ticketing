from src import revoked_store
from src.config import Config


def add_token_to_blacklist(jti, val):
    revoked_store.set(jti, val, Config.ACCESS_EXPIRES * 1.2)
