import os

from pathlib import PurePath
from sqlalchemy.engine import create_engine

def get_db_engine():
    try:
        db_engine = create_engine("sqlite:////db/database.db").execution_options(autocommit=False)
        return db_engine.connect()
    except Exception as e:
        print (e)
        raise
