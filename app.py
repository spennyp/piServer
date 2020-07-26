from flask import Flask
from flask_restful import Api
from paths import *

app = Flask(__name__)
api = Api(app)

api.add_resource(TellSlack, '/tell-slack')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8060", debug=True)
