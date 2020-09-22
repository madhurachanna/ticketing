import os
from datetime import timedelta


class Config:
    POSTGRES = {
        "user": os.environ["POSTGRES_USER"],
        "pw": os.environ["POSTGRES_PASSWORD"],
        "db": os.environ["POSTGRES_DB"],
        "port": os.environ["POSTGRES_PORT"],
        "host": os.environ["POSTGRES_HOST"],
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgres://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )

    ACCESS_EXPIRES = timedelta(minutes=15)
    # REFRESH_EXPIRES = timedelta(days=30)

    JWT_SECRET_KEY = os.environ["JWT_KEY"]
    # JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
