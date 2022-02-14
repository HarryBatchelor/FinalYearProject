from importlib.metadata import requires
from typing_extensions import Required
from flask import Flask
from flask_restful import Api, Resource, reqparse
from tinydb import TinyDB, Query
import uuid

project = "slalompole"

app = Flask(__name__)
api = Api(app)
db = tinyDB(project+'.json')
query = Query()

slalompole_args = reqparse.RequestParser()
slalompole_args.add_argument("X", type=float, help="X is missing", required=True)
slalompole_args.add_argument("Y", type=float, help="Y is missing", required=True)
slalompole_args.add_argument("Z", type=float, help="Z is missing", required=True)

class Items(Resources):
    def get(self):
        return db.all()

    def put(self):
        id = uuid.uuid4().hex
        args = slalompole_args.parse_args()
        db.insert({'id': id, 'data' :args})
        return db.search(query.id == id), 201

class Item(Resource):
    def get(self, uid):
        return db.search(query.id == uid)

    def patch(self, uid):
        args = slalompole_args.parse_args()
        db.update({'data' :args}, query.id == uid)
        return db.search(query.id == uid), 201
    
    def delete(self, uid):
        db.remove(query.id == uid)
        return '', 204
    
api.add_resource(Items, "/"+project+"/")
api.add_resource(Items, "/"+project+"/<uid>")

if __name__ == "__main__":
    app.run(host='192.168.0.129', debug=False)