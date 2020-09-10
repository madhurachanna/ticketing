import os


class Config:
    POSTGRES = {
        "user": os.environ['POSTGRES_USER'],
        "pw": os.environ['POSTGRES_PASSWORD'],
        "db": os.environ['POSTGRES_DB'],
        "port": os.environ['POSTGRES_PORT'],
        "host": os.environ['POSTGRES_HOST']
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgres://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    JWT_SECRET_KEY = os.environ['JWT_KEY']
