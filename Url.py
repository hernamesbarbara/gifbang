#!/usr/bin/env python3
from peewee import Model, CharField, DateTimeField, PostgresqlDatabase
import datetime
import json


def db_setup():
    with open('./db_creds.json', 'r') as f:
        db_creds = json.load(f)
    return db_creds


db_creds = db_setup()

db = PostgresqlDatabase(
    db_creds['db_name'],
    user=db_creds['db_user'],
    password=db_creds['db_password'],
    host=db_creds['db_host'],
    port=db_creds['db_port']
)


class URL(Model):
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    status = CharField(
        default='new',
        choices=['new', 'downloaded', 'high_res', 'low_res']
    )

    class Meta:
        database = db


# Connect and create tables
db.connect()
db.create_tables([URL], safe=True)
