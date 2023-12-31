from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True
# Importa las rutas después de crear la aplicación
from app.controllers import upload_controller
