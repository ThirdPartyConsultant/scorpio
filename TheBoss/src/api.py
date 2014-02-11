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
ALL_SERVICE_LIST = { }

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

# merge new to origin, replace the value in string and array, recursive handle t he value in dict
def mergeDict(origin, new):
    for key in new.keys():
        if origin.has_key(key):
            if type(origin[key]) is dict:
                mergeddict = mergeDict(origin[key], new[key])
                origin[key] = mergeddict
            else:
                origin[key] = new[key]
        else:
            origin[key] = new[key]

    return origin


def getRandomID():
    characters = string.ascii_letters + string.digits
    id=  "".join(choice(characters) for x in range(randint(8, 8)))
    return id

def abort_if_doesnt_exist(sid, alist):
    if sid not in alist:
        abort(404, message=" {} doesn't exist".format(sid))



class Service(Resource):
    def get(self, name):
        abort_if_doesnt_exist(name, ALL_SERVICE_LIST)
        return ALL_SERVICE_LIST[name]

    def put(self):
        content = request.data
        new_service = json.loads(content)
        ALL_SERVICE_LIST[new_service['name']] = new_service
        return ALL_SERVICE_LIST


    
# 
class Person(Resource):
    def get(self, name, sid):
        abort_if_doesnt_exist(sid, ALL_PERSON_LIST)
        person = ALL_PERSON_LIST[sid]
        return person

    def delete(self, name, sid):
        abort_if_doesnt_exist(sid, ALL_PERSON_LIST)
        del ALL_PERSON_LIST[sid]
        return '', 204

    def put(self,name):
        args = parser.parse_args()
        content = request.data
        new_person = json.loads(content)
        current_datetime = str(datetime.datetime.now())
        person = {}
        sid = getRandomID()
        person['sid'] = sid
        person['service'] = name 
        person['createtime'] = current_datetime
        person['status'] = 'new' # status: new-> taken -> serving -> closed (removed, give-up, noshow)
        ALL_PERSON_LIST[sid] = person
        return person, 201

    def post(self,name, sid):
        abort_if_doesnt_exist(sid, ALL_PERSON_LIST)
        content = request.data
        update_person = json.loads(content)
        origin_person = ALL_PERSON_LIST[sid]
        result = mergeDict(origin_person, update_person)
        ALL_PERSON_LIST[sid] = result
        return ALL_PERSON_LIST[sid], 201

# 
class Status(Resource):
    def post(self, name, sid):
        args = parser.parse_args()
        content = request.data
        person = json.loads(content)
        ALL_PERSON_LIST[sid]['status'] = person['status']
        return 201

######################################################################
api.add_resource(Person, '/Person')
api.add_resource(Person, '/Person/<string:sid>')
api.add_resource(Service, '/Service/<string:name>')
api.add_resource(Service, '/Service')
api.add_resource(Person, '/Service/<string:name>/Person')
api.add_resource(Person, '/Service/<string:name>/Person/<string:sid>')
api.add_resource(Status, '/Service/<string:name>/Person/<string:sid>/Status')


if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=8080)
