import os
import sys

from flask import Flask
app = Flask(__name__)


""" ------------- FOLDER INDEXATION ----------------- """
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# Add functions
from .views import main


# Add routes
app.add_url_rule('/', view_func=main.home, methods=['GET'])
app.add_url_rule('/buscar_recetas_por_ingredientes', view_func=main.buscar_recetas_por_ingredientes, methods=['GET'])
app.add_url_rule('/obtener_receta/<id>', view_func=main.obtener_receta, methods=['GET'])

# Insert data
app.add_url_rule('/insertar_ingrediente', view_func=main.insertar_ingrediente, methods=['POST'])
