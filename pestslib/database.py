from sqlite3 import IntegrityError
import string
from tkinter.tix import INTEGER
from xmlrpc.client import DateTime
import sqlalchemy as db
from pests import Pest, PestObservation, Illness, DiagnosticTesting

Pests = db.Table(
    'Pest',
    db.Column('Id', INTEGER, primary_key=True),
    db.Column('genus', string),
    db.Column('species', string)
)

PestObservations = db.Table(
    'PestObservation',
    db.Column('Id', INTEGER, primary_key=True),
    db.Column('city', string),
    db.Column('county', string),
    db.Column('obs_date', DateTime)
)
