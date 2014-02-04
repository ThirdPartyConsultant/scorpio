import sys
import datetime
import json
import string
from random import *
from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory
from flask.ext.restful import reqparse, abort, Api, Resource
from apiHandler import ApiHandler

app = Flask(__name__)
api = Api(app)

ALL_PERSON_LIST = { }

def getRandomID():
    characters = string.ascii_letters + string.digits
    id=  "".join(choice(characters) for x in range(randint(8, 8)))
    return id

def abort_if_doesnt_exist(sid):
    if sid not in ALL_PERSON_LIST:
        abort(404, message=" {} doesn't exist".format(sid))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# 
class Person(Resource):
    def get(self, sid):
        abort_if_doesnt_exist(sid)
        return TODOS[todo_id]

    def delete(self, sid):
        abort_if_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self):
        args = parser.parse_args()
        content = request.data
        new_person = json.loads(content)
        current_datetime = str(datetime.datetime.now())
        person = {}
        person['sid'] = getRandomID()
        person['createtime'] = current_datetime
        person['status'] = 'new' # status: new-> taken -> serving -> closed (removed, give-up, noshow)
        ALL_PERSON_LIST['sid'] = person
        return ALL_PERSON_LIST, 201



##
## Actually setup the Api resource routing here
##
api.add_resource(Person, '/Person')


if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=5000)
