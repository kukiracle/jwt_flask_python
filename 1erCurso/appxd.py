from PIL import Image
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_restful import Api
from database import db
from config.config_db import FULL_URL_DB, migrate

from database import db
from config.config_db import FULL_URL_DB, migrate
from config.ma import ma

# k
from controllers.colour_controller import ColourList, ColourRegister
from controllers.direction_controller import DirectionList, DirectionRegister
from controllers.location_controller import LocationList, LocationRegister, LocationUpdate
from controllers.photo_controller import PhotoList, PhotoRegister
from controllers.image_controller import Upload
from controllers.atrasos_faltas_observaciones_controller import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# ma.init_app(app)
migrate.init_app(app, db)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# /api/v1/user -> get post put delete ( patch put )
# /api/v1/user?id=1&emmail=hola@q.com -> query string
# /api/v1/user/<:id> -> param
# /api/v1/user/<:id>/<role> -> param

# singin
# singout

# registro user

api.add_resource(ColourRegister, '/api/v1/coloursRegister')  # funca
api.add_resource(ColourList, '/api/v1/colourlist')  # funca

api.add_resource(DirectionRegister, '/api/v1/directionregistrer')
api.add_resource(DirectionList, '/api/v1/directionlist')
api.add_resource(LocationRegister, '/api/v1/locationregistrer')
api.add_resource(LocationList, '/api/v1/locationList')
api.add_resource(PhotoRegister, '/api/v1/photoregistrer')
api.add_resource(PhotoList, '/api/v1/photolist')
api.add_resource(Atrasos_faltas_observacionesList, '/api/v1/afolist')
api.add_resource(Atrasos_faltas_observacionesRegister, '/api/v1/aforegister')

# configurar flask-wtf
app.config['SECRET_KEY'] = 'llave_secreta'

# set FLASK_ENV=development

# flask db init
# pip install -r requirements.txt
# pip freeze > requirements.txt

# flask db stamp head     paso  1 para errores o actualizar ala ultima version
# flask db migrate        paso  2
# flask db upgrade        paso  3
#git commit -ammend --author="kukiracle <kukiracle@gmail.com>"
# git filter-branch -f --env-filter "
# GIT_AUTHOR_NAME='kukiracle'
# GIT_AUTHOR_EMAIL='kukiracle@gmail.com'
# GIT_COMMITTER_NAME='fixitos'
# GIT_COMMITTER_EMAIL='kukiracle@gmail.com'
# " HEAD