import sqlite3
from sqlite3 import Cursor
from flask import Flask
from pestslib.pests import Pest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, Integer

con = sqlite3.connect('pests.db')
cur = con.cursor()


cur.execute('CREATE TABLE pest (Genus, species)')
cur.execute("INSERT INTO pest VALUES ('Culex', 'pipiens')")
cur.execute('CREATE TABLE pest_observation (City, Country, Date)')
cur.execute(
    "INSERT INTO pest_observation VALUES('Amarillo', 'Randall', '2022-03-22')")
cur.execute('CREATE TABLE illness(Type)')
cur.execute("INSERT INTO illness VALUES ('West Nile Virus')")
cur.execute('CREATE TABLE diagnostic_testing (Method, Antibody, Result, Date)')
cur.execute("INSERT INTO diagnostic_testing VALUES ('Cerebrospinal fluid', 'Immunoglobulin Mu', 'Positive', '2022-03-25')")
con.commit()
con.close()
