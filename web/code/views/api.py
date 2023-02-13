import os
import sys

from flask import request

""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aux_functions.database import get_db_engine

def insertar_ingrediente():
   engine = get_db_engine()
   ingrediente = request.json
   ingredientes = engine.execute('insert into ingredientes (id, nombre) VALUES ({id}, \'{nombre}\')'.format(id=ingrediente['id'], nombre=ingrediente['nombre']))
   return {"id": ingrediente['id']}


def buscar_recetas_por_ingredientes():
   pass