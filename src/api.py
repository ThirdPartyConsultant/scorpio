#!/usr/bin/python

from flask import request, Flask, jsonify
from flask import send_from_directory

app = Flask(__name__)
apiPath="/api/v1/"
localstorepath="/tmp/storage/"

@app.route(apiPath+'<uid>/<path:actionPath>')
def fileHandler(uid, actionPath):
    result = {"uid":uid, "actionPath":actionPath}
    action = request.args.get('action', '')
    result = {"uid":uid, "actionPath":actionPath,"action":action}
    return jsonify(result)

@app.route(apiPath+'urlsforuser')
def urlforusers():
    result = {
  "Code": "" ,
  "Status": "OK" , 
  "me": "https://dc1.safesync.com/api/v1/me" ,
  "filesroot": "https://dc1.safesync.com/api/v1/filesroot" ,
  "home": "https://dc1.safesync.com/api/v1/home" ,
  "sessiontoken": "https://dc1.safesync.com/api/v1/sessiontoken" ,
  "recyclebin": "https://dc1.safesync.com/api/v1/recyclebin" ,
  "teamfolders": "https://dc1.safesync.com/api/v1/:files:teamspaces" ,
  "safesyncfolder": "https://dc1.safesync.com/api/v1/:home:safesyncfolder" ,
  "pairfolders": "https://dc1.safesync.com/api/v1/:home:pairfolders"
    }
    return jsonify(result)


@app.route(apiPath+'/sessiontoken')
def sessiontoken():
    # show the user profile for that user
    loginName = request.args.get('loginName', '')
    realm = request.args.get('realm', '')
    password = request.args.get('password', '')
    service = request.args.get('service', '')
    return jsonify({ "Code": "", "Status": "OK", "sessiontoken": "Mzq8MyVZDq36m0HKkzSpToBTp9s7g0c1QDUh_T40CwtK4YFE3Fw-4NkqB-7gX3WziIJkeytAyD9tOmV4cGlyZXMhMTMxNjI29DpOc1KNOmh1bXlvOmZyZWVAaHVteW8uY2NzAyMSFyZWZyZTMxNzM5NTk1OXNoVW50aWwhMA" })
 

@app.route(apiPath+'me')
def me():
    # show the post with the given id, the id is an integer
    result = {
    "actions": [],
    "container": 0,
    "desc": "user@example.com",
    "http_host": "https://www.example.com",
    "icon": "friend",
    "id": "Fxxx:user",
    "name": "Example User",
    "noun": "person",
    "thumb": "null",
    "verified": "1",
    "spaceUsage":2152452,
    "spaceQuota":3000000
    }
    return jsonify(result)

@app.route(apiPath+'filesroot/<path:filename>')
def getFile(filename):
    return send_from_directory(localstorepath, filename, as_attachment=True)

@app.route(apiPath+'filesroot')
def filesroot():

    result = {
    "actions": [], 
    "childNoun": "items", 
    "columns": [], 
    "container": 1, 
    "desc": "", 
    "details": "null", 
    "filters": [], 
    "icon": "folder", 
    "id": "filesroot", 
    "items": 2, 
    "listMore": 0, 
    "listViews": [
        "List", 
        "Thumbs"
    ], 
    "name": "Folders", 
    "node": [
        {
            "actions": [
                {
                    "id": "listDir"
                }, 
                {
                    "id": "downloadMulti"
                }, 
                {
                    "id": "FetchFromWeb_Fetch", 
                }
            ], 
            "container": 1, 
            "desc": "File Folder", 
            "fClass": "", 
            "floor": "", 
            "icon": "folder", 
            "id": "99999999-000000001", 
            "name": "My Files", 
            "noun": "folder", 
            "open": 0, 
            "overlays": "null", 
            "sharingData": {}, 
            "sharingId": "sharing:99999999-000000001", 
            "sharingURI": "/api/v1/sharing:99999999-000000001", 
            "thumb": "null", 
            "uri": "https://dc1.safesync.com/api/v1/Fxxxx/"
        }, 
        {
            "actions": [
                {
                    "id": "listDir", 
                }
            ], 
            "container": 1, 
            "desc": "", 
            "details": "null", 
            "fClass": "null", 
            "floor": 0, 
            "icon": "recyclebins", 
            "id": "99999999:recyclebins", 
            "name": "Recycle Bin", 
            "noun": "container", 
            "open": 0, 
            "overlays":"null", 
            "thumb": "null", 
            "uri": "https://dc1.safesync.com/api/v1/99999999:recyclebins"
        }
    ], 
    "noun": "container", 
    "orderBy": "null", 
    "orderDirection": "Asc", 
    "overlays": "null", 
    "page": 1, 
    "pages": 1, 
    "parent": "null", 
    "perPage": 100, 
    "treeRoot": "filesroot", 
    "uri": "https://dc1.safesync.com/api/v1/filesroot"
}

    return jsonify(result)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8111)
