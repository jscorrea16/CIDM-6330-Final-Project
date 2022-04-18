from sqlite3 import IntegrityError
import string
from tkinter.tix import COLUMN, INTEGER
from tokenize import String
from xmlrpc.client import DateTime
import sqlalchemy as db
from pests import Pest, PestObservation, Illness, DiagnosticTesting

Pests = db.Table(
    'Pest',
    db.Column('Id', INTEGER, primary_key=True),
    db.Column('genus', String),
    db.Column('species', String)
)

PestObservations = db.Table(
    'PestObservation',
    db.Column('Id', INTEGER, primary_key=True),
    db.Column('city', String),
    db.Column('county', String),
    db.Column('obs_date', DateTime)
)
