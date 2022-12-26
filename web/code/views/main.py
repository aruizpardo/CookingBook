import os
import pandas as pd
import sqlite3
import sys

""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aux_functions.database import get_db_engine

def home():
   connection = sqlite3.connect('/db/database.db')
   connection.row_factory = sqlite3.Row

   ingredientes = connection.execute('select * from ingredientes').fetchall()
   print(ingredientes)

   return ingredientes[0]['nombre']