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


# a common data objec
# TODO: assume the db name is TheBoss
class CommonDo(Resource):
    def delete(self, collectionName, sid):
        commonDo = DataAccess('TheBoss',collectionName)
        commonDo.delete({'sid':sid})
        return 201

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
api.add_resource(CommonDo, '/Cdo/<string:collectionName>/<string:sid>')
api.add_resource(CommonDo, '/Cdo/<string:collectionName>')


if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=8080)
