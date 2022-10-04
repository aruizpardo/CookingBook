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
app.add_url_rule('/', view_func=main.home)