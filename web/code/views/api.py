import json
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
   engine = get_db_engine()
   ingredientes = json.dumps(request.json)
   incluye = ["sum(id_ingrediente = {}) > 0".format(number) for number in (request.json['incluye'] if 'incluye' in request.json else [])]
   excluye = ["sum(id_ingrediente = {}) = 0".format(number) for number in (request.json['excluye'] if 'excluye' in request.json else [])]
   condiciones = incluye + excluye

   sql = """
   select recetas.nombre FROM (
	   select id_receta, ({condiciones}) as c2
      from ingredientes_receta group by id_receta
   ) t1 INNER JOIN recetas ON recetas.id = t1.id_receta
   WHERE c2 = 1
   """.format(condiciones = " AND ".join(condiciones) if len(condiciones) > 0 else "1")

   recetas = engine.execute(sql).fetchall()
   recetas = [row['nombre'] for row in recetas]

   return recetas