import os
import sqlalchemy
from sqlalchemy import Table, Column, String, Integer
from databases import Database

if os.path.exists('local.db'):
    os.remove('local.db')

engine = sqlalchemy.create_engine('sqlite:///some.db')
metadata = sqlalchemy.MetaData(engine)


spaceship = Table(
    'spaceship',
    metadata,
    Column('id', Integer),
    Column('name', String),
    Column('weight', Integer),
)

weapon = Table(
    'weapon',
    metadata,
    Column('id', Integer),
    Column('name', String),
    Column('velocity', Integer),
    Column('damage', Integer),
)

spaceship_weapon = Table(
    'spaceship_weapon',
    metadata,
    Column('spaceship_id', Integer),
    Column('weapon_id', Integer),
)


database = Database('sqlite:///some.db')
