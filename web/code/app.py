import os
import sys

from flask import Flask
app = Flask(__name__)


""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# Add functions
from .views import api, web


# Add webpage routes
app.add_url_rule('/', view_func=web.home, methods=['GET'])
app.add_url_rule('/buscar_recetas_por_ingrediente', view_func=web.buscar_recetas_por_ingrediente, methods=['GET'])
app.add_url_rule('/obtener_receta/<id>', view_func=web.obtener_receta, methods=['GET'])


# Add api routes
app.add_url_rule('/api/insertar_ingrediente', view_func=api.insertar_ingrediente, methods=['POST'])
app.add_url_rule('/api/buscar_recetas_por_ingredientes', view_func=api.buscar_recetas_por_ingredientes, methods=['GET'])
