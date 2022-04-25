import time
import os
import sys
from flask.helpers import make_response
from flask import Flask,jsonify,g
from flask import request,abort
from flask_restful import Api
from resources.routes import initialize_routes 

app = Flask(__name__)
"""Importar config params desde archivo config-params y environment .env.dev""" 
app.config.from_pyfile('config_params.py')

import routes

api=Api(app)
routes.initialize_routes(api)


if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0',port=5000)