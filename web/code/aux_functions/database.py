import os

from pathlib import PurePath
from sqlalchemy.engine import create_engine

def get_db_engine():
    try:
        file_path = os.path.realpath(__file__)
        abs_path = PurePath(file_path)
        rel_path = str(abs_path.parents[1])
        db_engine = create_engine("sqlite:///"+rel_path+"/log_db/ms-log.db")
        return db_engine
    except Exception as e:
        print (e)
        raise
