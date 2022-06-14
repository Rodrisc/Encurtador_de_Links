from flask import Flask
from db import conetar_banco
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
conex, cursor = conetar_banco()

from routes import rotas