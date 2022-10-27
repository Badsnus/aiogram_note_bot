from datetime import datetime

import databases
import orm

from data.config import DATABASE_URL

database = databases.Database(DATABASE_URL)
models = orm.ModelRegistry(database=database)


class User(orm.Model):
    tablename = "user"
    registry = models
    fields = {
        'id': orm.Integer(primary_key=True),
        "user_id": orm.BigInteger(index=True, unique=True),
    }


class Note(orm.Model):
    tablename = "note"
    registry = models
    fields = {
        'id': orm.Integer(primary_key=True),
        "user": orm.ForeignKey(User, on_delete=orm.CASCADE),
        'name': orm.String(max_length=100),
        'description': orm.String(max_length=1500),
        'date': orm.DateTime(default=datetime.now()),
        'completed': orm.Boolean(default=False)
    }
