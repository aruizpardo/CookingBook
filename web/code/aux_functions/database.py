import os

from pathlib import PurePath
from sqlalchemy.engine import create_engine

def get_db_engine():
    try:
        db_engine = create_engine("sqlite:////db/database.db")
        return db_engine
    except Exception as e:
        print (e)
        raise
