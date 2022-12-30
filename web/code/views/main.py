from flask import request

import os
import pandas as pd
import sqlite3
import sys

""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aux_functions.database import get_db_engine

def home():
   engine = get_db_engine()

   ingredientes = engine.execute('select * from ingredientes').fetchall()
   print(ingredientes)

   return ingredientes[0]['nombre']


def insertar_ingrediente():
   engine = get_db_engine()
   ingrediente = request.json
   ingredientes = engine.execute('insert into ingredientes (id, nombre) VALUES ({id}, \'{nombre}\')'.format(id=ingrediente['id'], nombre=ingrediente['nombre']))
   return {"id": ingrediente['id']}

def insertar_instruccion():
   pass

def insertar_ingrediente_receta():
   pass

def insertar_receta():
   pass

def buscar_recetas_por_ingredientes():
   pass

def obtener_receta(id):
   engine = get_db_engine()

   sql_recetas = 'select * from recetas where id = ' + id
   sql_ingredientes = """
      SELECT
         ingredientes.nombre,
         ingredientes_receta.cantidad
      FROM ingredientes_receta
         INNER JOIN ingredientes ON ingredientes_receta.id_ingrediente = ingredientes.id
      WHERE
         ingredientes_receta.id_receta = {id_receta}
      """.format(id_receta = id)
   sql_instrucciones = """
      SELECT
         *
      FROM instrucciones
      WHERE id_receta = {id_receta}
      """.format(id_receta = id)

   receta = engine.execute(sql_recetas).fetchall()
   ingredientes = engine.execute(sql_ingredientes).fetchall()
   instrucciones = engine.execute(sql_instrucciones).fetchall()

   return {
      "receta": receta,
      "ingredientes": ingredientes,
      "instrucciones": instrucciones
   }
