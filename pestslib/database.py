import string
from tkinter.tix import COLUMN, INTEGER
from tokenize import String
import sqlalchemy as db
from pests import Pest, PestObservation, Illness, DiagnosticTesting

Pest = db.Table(
    'Pest',
    db.COLUMN('Id', INTEGER, primary_key=True),
    db.COLUMN('genus', String),
    db.COLUMN('species', String)
)
