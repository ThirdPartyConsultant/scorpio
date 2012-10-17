#!/usr/bin/python
#
import os

from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory
from werkzeug import secure_filename
from LocalFileHandler import LocalFileHandler,ThinSyncDirFileCreate

apiPath = "/api/v1/"
localstorepath = "/tmp/storage"
upload_folder = localstorepath

allow_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
hostIP='10.1.192.65'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in allow_extensions

@app.route('/api/version')
def currentversion():
    result = {
    "Version": "1.1"
    }
    return jsonify(result)

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
  "me": "https://%s/api/v1/me"%(hostIP) ,
  "filesroot": "https://%s/api/v1/filesroot"%(hostIP) ,
  "home": "https://%s/api/v1/home"%(hostIP) ,
  "sessiontoken": "https://%s/api/v1/sessiontoken"%(hostIP) ,
  "recyclebin": "https://%s/api/v1/recyclebin"%(hostIP) ,
  "teamfolders": "https://%s/api/v1/:files:teamspaces"%(hostIP) ,
  "safesyncfolder": "https://%s/api/v1/:home:safesyncfolder"%(hostIP) ,
  "pairfolders": "https://%s/api/v1/:home:pairfolders"%(hostIP)
    }
    return jsonify(result)


@app.route(apiPath+'sessiontoken',methods=['GET','POST'])
def sessiontoken():
    # show the user profile for that user
    loginName = request.args.get('loginName', '')
    realm = request.args.get('realm', '')
    password = request.args.get('password', '')
    service = request.args.get('service', '')
    return jsonify({ "Code": "", "Status": "OK", "sessiontoken": "Mzq8MyVZDq36m0HKkzSpToBTp9s7g0c1QDUh_T40CwtK4YFE3Fw-4NkqB-7gX3WziIJkeytAyD9tOmV4cGlyZXMhMTMxNjI29DpOc1KNOmh1bXlvOmZyZWVAaHVteW8uY2NzAyMSFyZWZyZTMxNzM5NTk1OXNoVW50aWwhMA" })

@app.route(apiPath+'nobinroot')
def nobinroot():
    result = {
  "icon":"folder",
  "actions":[],
    "listViews":["List","Thumbs"],
    "treeRoot":"filesroot",
    "page":1,
    "filters":[],
    "node":[{"icon":"folder",
    "actions":[],
    "floor":"null",
    "thumb":"null",
    "desc":"File Folder",
    "id":"",
    "sharingURI":"",
    "canDragDropFiles":1,
    "name":"My Files",
    "noun":"folder",
    "container":1,
    "overlays":"null",
    "details":"null",
    "uri":"/api/v1/Mvf/",
    "fClass":"null","open":0,
    "sharingId":"",
    "sharingData":{}}],
    "childNoun":"items",
    "searchURI":"",
    "desc":"null",
    "id":"nobinroot",
    "orderDirection":"Asc",
    "parent":"null",
    "noun":"container",
    "name":"Folders",
    "container":1,
    "overlays":"null",
    "details":"null",
    "uri":"/api/v1/nobinroot",
    "searchId":"",
    "listMore":0,
    "orderBy":"null",
    "columns":[],
    "perPage":100,
    "items":3,
    "pages":1
    }

    return jsonify(result)
@app.route(apiPath+'Mvf/',methods=['GET','POST','PUT'])
@app.route(apiPath+'Mvf/<path:file>',methods=['GET','POST','PUT'])
def Mvf(file=None):

    if request.method == 'PUT':
		file = "/"+file
		filename = file.rsplit("/",1)[1]
		print "directories = "+ upload_folder +file
		with open((upload_folder+file), 'w') as f:
			f.write(request.data)
		ret = {}
		return jsonify(ret)

    if request.method == 'POST':
		varAction = request.args.get('action', '')
		varName = "/" + request.args.get('name',"")
		locFileObj = LocalFileHandler()
		
		if varAction == 'Create' and file:
			print "create directories "+upload_folder+"/"+file+varName
			locFileObj.mkdirs("/"+file+varName)
		
		elif varAction == 'Create':
			#print "varname = "+varName
			locFileObj.mkdirs(varName)
		
		result = {"Code":"CREATED",
					"Message":"CREATED",
					"Status":"OK",
					"added":[]}
		
		return jsonify(result)

    if request.method == 'GET' and file:
        if(LocalFileHandler().checkDir(file)):
        	result = ThinSyncDirFileCreate().processDirList("/"+file)
	    	return jsonify(result) 
        else:
    		return send_from_directory(localstorepath, file, as_attachment=True)
    else:
		result = {
"icon":"folder",
"actions":[
  {"id":"downloadMulti"},
  {"icon":"Link",
   "href":"#9-17:sharelinks",
   "label":"Show Links",
   "id":"shareLinks"},
   {"id":"newFolder"},
   {"tasks":0,
    "tree":0,
    "context":0,
    "id":"newFile"}],
    "listViews":["List",
    "Thumbs"],
    "treeRoot":"filesroot",
    "page":1,
    "filters":[],
    "node":"",
    "childNoun":"items",
    "searchURI":"",
    "desc":"File Folder",
    "id":"9-17",
    "canDragDropFiles":1,
    "orderDirection":"Asc",
    "parent":"null",
    "noun":"folder",
    "name":"My Files",
    "container":1,
    "overlays":"null",
    "details":"",
    "uri":"/api/v1/Mvf/",
    "searchId":"",
    "listMore":"null",
    "orderBy":"null",
    "columns":[],
    "perPage":100,
    "items":"2",
    "pages":1
    		}
		result['node'] = ThinSyncDirFileCreate().processFileList()
		print result
		return jsonify(result) 

@app.route(apiPath+'me')
def me():
    # show the post with the given id, the id is an integer
    result = {
      "http_host":"https://%s"%(hostIP),
      "spaceUsage":2152452,
      "spaceQuota":3000000,
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
    "details": "", 
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
            "uri": "https://%s/api/v1/Fxxxx/"%(hostIP)
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
            "uri": "https://%s/api/v1/99999999:recyclebins"%(hostIP)
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
    "uri": "https://%s/api/v1/filesroot"%(hostIP)
}

    return jsonify(result)

@app.route(apiPath + 'upload_file', methods=['GET', 'POST', 'PUT'])
def upload_file():
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    if request.method == 'POST' or request.method == 'PUT':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route(apiPath + 'uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8111)
