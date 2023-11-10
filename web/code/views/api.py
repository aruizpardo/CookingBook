import json
import os
import sys

from flask import request

""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aux_functions.database import get_db_engine

def insertar_ingrediente():
   """
   Inserta una ingrediente en la tabla correspondiente.

   Returns:
      El ID de la fila insertada.
   """

   engine = get_db_engine()
   ingrediente = request.json['nombre']

   sql = 'insert into Ingredientes (Nombre) VALUES (\'{nombre}\') returning IngredienteID'
   test = engine.execute(sql.format(nombre=ingrediente)).fetchone()
   engine.commit()

   return test


def buscar_recetas_por_ingredientes():
   engine = get_db_engine()
   ingredientes = json.dumps(request.json)
   incluye = ["sum(IngredienteID = {}) > 0".format(number) for number in (request.json['incluye'] if 'incluye' in request.json else [])]
   excluye = ["sum(IngredienteID = {}) = 0".format(number) for number in (request.json['excluye'] if 'excluye' in request.json else [])]
   condiciones = incluye + excluye

   sql = """
   select Recetas.Nombre FROM (
	   select RecetaID, ({condiciones}) as c2
      from RecetaIngredientes group by RecetaID
   ) t1 INNER JOIN Recetas ON Recetas.id = t1.RecetaID
   WHERE c2 = 1
   """.format(condiciones = " AND ".join(condiciones) if len(condiciones) > 0 else "1")

   recetas = engine.execute(sql).fetchall()
   recetas = [row['Nombre'] for row in recetas]

   return recetas