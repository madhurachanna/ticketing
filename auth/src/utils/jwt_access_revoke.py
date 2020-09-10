from src import revoked_store
from src.config import Config


def set_jwt_access_revoke(jti, val):
    revoked_store.set(jti, val, Config.ACCESS_EXPIRES * 1.2)
