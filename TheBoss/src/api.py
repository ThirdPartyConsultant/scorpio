import sys
import datetime
import json
import string
from random import *
from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory
from flask.ext.restful import reqparse, abort, Api, Resource
from apiHandler import ApiHandler
from DataAccess import DataAccess
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
api = Api(app)

ALL_PERSON_LIST = { }
ALL_SERVICE_LIST = { }

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
serviceData = DataAccess('TheBoss','service')
personData = DataAccess('TheBoss','person')

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
        records = serviceData.select({'name':name})
        if records.count() == 0:
            abort(404, message=" {} doesn't exist".format(name))
        else:
            service = records.next()
            del service['_id'] 
            return service

    def put(self):
        content = request.data
        new_service = json.loads(content)
        objId = serviceData.insert(new_service)
        del new_service['_id']
        return new_service
    
# 
class Person(Resource):
    def get(self, name, sid):
        records = personData.select({'sid':sid})
        if records.count() == 0:
            abort(404, message=" {} doesn't exist".format(sid))
        else:
            person = records.next()
            del person['_id']
            return person

    def delete(self, name, sid):
        abort_if_doesnt_exist(sid, ALL_PERSON_LIST)
        del ALL_PERSON_LIST[sid]
        return '', 204

    def put(self,name):
        args = parser.parse_args()
        #content = request.data
        #new_person = json.loads(content)
        current_datetime = str(datetime.datetime.now())
        person = {}
        sid = getRandomID()
        person['sid'] = sid
        person['service'] = name 
        person['createtime'] = current_datetime
        person['status'] = 'new' # status: new-> taken -> serving -> closed (removed, give-up, noshow)
        personData.insert(person)
        del person['_id']
        return person, 201

    def post(self,name, sid):
        person =  {}
        records = personData.select({'sid':sid})
        if records.count() == 0:
            abort(404, message=" {} doesn't exist".format(sid))
        else:
            person = records.next()
            del person['_id'] 

        content = request.data
        update_person = json.loads(content)
        origin_person = person
        result = mergeDict(origin_person, update_person)
        
        personData.update({'sid':sid},{"$set": result})
        return result, 201

# 
class CommonDo(Resource):
    def post(self,collectionName, sid):
        currentContent =  {}
        commonDo = DataAccess('TheBoss',collectionName)
        records = commonDo.select({'sid':sid})
        if records.count() == 0:
            abort(404, message=" {} doesn't exist".format(sid))
        else:
            currentContent = records.next()
            del currentContent['_id'] 

        content = request.data
        updateContent = json.loads(content)
        
        result = mergeDict(currentContent, updateContent)
        commonDo.update({'sid':sid}, {"$set": result})
        return JSONEncoder().encode(result), 201
        
        commonDo.update({'sid':sid},{"$set": result})

    def put(self, collectionName):
        commonDo = DataAccess('TheBoss',collectionName)
        content = request.data
        jsonContent = json.loads(content)
        sid = getRandomID()
        jsonContent['sid'] = sid
        print "before=="
        print jsonContent
        commonDo.insert(jsonContent)
        return JSONEncoder().encode(jsonContent), 201
        #return jsonContent, 201

    def get(self, collectionName, sid):
        commonDo = DataAccess('TheBoss',collectionName)
        records = commonDo.select({'sid':sid})
        if records.count() == 0:
            abort(404, message=" {} doesn't exist".format(sid))
        else:
            content = records.next()
            return JSONEncoder().encode(content), 201

######################################################################
api.add_resource(Person, '/Person')
api.add_resource(Person, '/Person/<string:sid>')
api.add_resource(Service, '/Service/<string:name>')
api.add_resource(Service, '/Service')
api.add_resource(Person, '/Service/<string:name>/Person')
api.add_resource(Person, '/Service/<string:name>/Person/<string:sid>')
api.add_resource(CommonDo, '/Cdo/<string:collectionName>/<string:sid>')
api.add_resource(CommonDo, '/Cdo/<string:collectionName>')


if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=8080)
