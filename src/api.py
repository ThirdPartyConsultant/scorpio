#!/usr/bin/python

from flask import request, Flask, jsonify
from flask import send_from_directory
from LocalFileHandler import LocalFileHandler 

app = Flask(__name__)
apiPath="/api/v1/"
localstorepath="/tmp/storage/"
hostIP='10.1.192.65'

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
    "filters":[{
        "tree":"textroot",
        "text":"Documents",
        "name":"text",
        "uri":"/api/v1/textroot"},
    {
    "tree":"sheetroot",
    "text":"Spreadsheets",
    "name":"sheet",
    "uri":"/api/v1/sheetroot"},
    {"tree":"presentationroot",
    "text":"Presentations",
    "name":"presentation",
    "uri":"/api/v1/presentationroot"},
    {"tree":"filesroot",
    "text":"Clear Filter",
    "name":"nofilters",
    "uri":"/api/v1/filesroot"}],
    "node":[{"icon":"folder",
    "actions":[{"id":"listDir"},
    {"id":"downloadMulti"},
    {"icon":"Link","href":"#9-17:sharelinks",
    "label":"Show Links",
    "id":"shareLinks"}],
    "floor":"null",
    "thumb":"null",
    "desc":"File Folder",
    "id":"9-17",
    "sharingURI":"/api/v1/sharing:9-17",
    "canDragDropFiles":1,
    "name":"My Files",
    "noun":"folder",
    "container":1,
    "overlays":"null",
    "details":"<div id=\"account_info\" class=\"container\">\n\n\t<div class=\"account_item account_plan\">\n\t\t<h1>Default TeamFolder Org</h1>\t\t\t<a href=\"javascript:popupWindow('ChangePassword',245,500,false,'/Pages/MyAccount/?action=password');\">Change Password</a>\t\t\t</div>\n\t\n\t<div class=\"account_item account_space\">\t\t\t\t<h1>Using 7.78 KB of 1 GB</h1>\t\t\t<a onclick=\"Action.DialogAction({ page: 'Pages/Dialog/SpaceUsage.htm', width: 450 });\">View details</a>\t</div>\n\t\t\t\n</div>\n\n<div id=\"info_right_bottom\" class=\"container\">\n\t\n\t<div class=\"clear\"></div>\n\n\t<div id=\"quick-links\" class=\"info_spacer_top\">\n\t\t<ul>\t\t\t<li><a href=\"#/updates/\" class=\"history\">View events history</a></li><li><a href=\"https://%s/pages/en/smartdrive\" class=\"downloads\" target=\"_blank\">Downloads</a></li>\t\t\t<li><a href=\"http://%s/HelpWindowsClientQuickStart.htm\" target=\"_blank\" class=\"help\">Get help</a></li>\t\t</ul>\n\t</div>\n\t\n</div>\n\n<script type=\"text/javascript\">\n\t\n\t(function(){\t\t\n\t\t$('info_right_text').update('\tAccount Information');\n\t\t\n\t\tfunction heightCheck(){\n\t\t\tvar b = $('info_right_bottom');\n\t\t\tif( !b ) return Event.stopObserving(window, 'resize', this);\n\t\t\t// Don't show the quick links if theres not enough height\n\t\t\tvar height = $('header').getHeight() + $('info_pane_details').getHeight() + b.getHeight();\n\t\t\t(document.viewport.getHeight() < height) ? b.hide() : b.show();\n\t\t}\n\t\t\n\t\tEvent.observe(window, 'resize', heightCheck);\t\n\t\theightCheck();\n\t\t\n\t})()\n\t\n</script>"%(hostIP,hostIP),
    "uri":"/api/v1/Mvf/",
    "fClass":"null","open":0,
    "sharingId":"sharing:9-17",
    "sharingData":{
    "icon":"null",
    "actions":[],
    "listViews":["Details"],
    "treeRoot":"filesroot",
    "page":"null",
    "filters":"null",
    "node":[],
    "childNoun":"permissions",
    "desc":"Sharing settings for !home",
    "id":"sharing:9-17",
    "orderDirection":"null",
    "parent":"/Mvf/",
    "noun":"folder",
    "name":"Sharing",
    "container":[],
    "overlays":"null",
    "uri":"/sharing:9-17",
    "searchId":"search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:sharing:9-17",
    "listMore":0,
    "orderBy":"null",
    "columns":[{
    "width":230,
    "orderBy":"name",
    "name":"entity",
    "label":"Entity",
    "param":"name"},
    {"width":60,
    "orderBy":"collaborator",
    "name":"collaborator",
    "label":"Collaborator",
    "param":"collaborator"},
    {"width":250,
    "orderBy":"tooltip",
    "name":"tooltip",
    "label":"Description",
    "param":"tooltip"}],
    "perPage":100,
    "items":0,
    "pages":1}},
    {"icon":"teamspaces",
    "actions":[{"tasks":0,
    "id":"listDir"},
    {"icon":"AddTeamspace",
    "alt":{"base":"Creates a new team folder in this organisation"},
    "label":{"base":"Create a folder"},
    "id":"createTeamspace",
    "code":"Action.DialogAction({ page: '/Pages/UserAdmin?type=TeamspaceName&ns_id=5:organisation'})"}],
    "noun":"container",
    "floor":0,
    "name":"Team Folders",
    "overlays":"null",
    "container":1,
    "details":"<div id=\"account_info\" class=\"container\">\n\n\t<div class=\"account_item account_plan\">\n\t\t<h1>Default TeamFolder Org</h1>\t\t\t<a href=\"javascript:popupWindow('ChangePassword',245,500,false,'/Pages/MyAccount/?action=password');\">Change Password</a>\t\t\t</div>\n\t\n\t<div class=\"account_item account_space\">\t\t\t\t<h1>Using 7.78 KB of 1 GB</h1>\t\t\t<a onclick=\"Action.DialogAction({ page: 'Pages/Dialog/SpaceUsage.htm', width: 450 });\">View details</a>\t</div>\n\t\t\t\n</div>\n\n<div id=\"info_right_bottom\" class=\"container\">\n\t\n\t<div class=\"clear\"></div>\n\n\t<div id=\"quick-links\" class=\"info_spacer_top\">\n\t\t<ul>\t\t\t<li><a href=\"#/updates/\" class=\"history\">View events history</a></li><li><a href=\"https://%s/pages/en/smartdrive\" class=\"downloads\" target=\"_blank\">Downloads</a></li>\t\t\t<li><a href=\"http://%s/HelpWindowsClientQuickStart.htm\" target=\"_blank\" class=\"help\">Get help</a></li>\t\t</ul>\n\t</div>\n\t\n</div>\n\n<script type=\"text/javascript\">\n\t\n\t(function(){\t\t\n\t\t$('info_right_text').update('\tAccount Information');\n\t\t\n\t\tfunction heightCheck(){\n\t\t\tvar b = $('info_right_bottom');\n\t\t\tif( !b ) return Event.stopObserving(window, 'resize', this);\n\t\t\t// Don't show the quick links if theres not enough height\n\t\t\tvar height = $('header').getHeight() + $('info_pane_details').getHeight() + b.getHeight();\n\t\t\t(document.viewport.getHeight() < height) ? b.hide() : b.show();\n\t\t}\n\t\t\n\t\tEvent.observe(window, 'resize', heightCheck);\t\n\t\theightCheck();\n\t\t\n\t})()\n\t\n</script>"%(hostIP,hostIP),
    "thumb":"null",
    "uri":"/api/v1/:files:teamspaces",
    "open":0,
    "fClass":"null",
    "desc":"null",
    "id":":files:teamspaces"},{
    "icon":"sharedwith",
    "actions":[{
    "tasks":0,
    "id":"listDir"}],
    "noun":"container",
    "floor":0,
    "name":"Shared With Me",
    "overlays":"null",
    "container":1,
    "details":"null",
    "thumb":"null",
    "uri":"/api/v1/:files:relations",
    "open":0,
    "fClass":"null",
    "desc":"null",
    "id":":files:relations"}],
    "childNoun":"items",
    "searchURI":"/api/v1/search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:nobinroot",
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
    "searchId":"search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:nobinroot",
    "listMore":0,
    "orderBy":"null",
    "columns":[{
    "width":230,
    "orderBy":"GROUP",
    "name":"group",
    "label":"Type",
    "param":"name"}],
    "perPage":100,
    "items":3,
    "pages":1
    }

    return jsonify(result)

@app.route(apiPath+'Mvf/')
def Mvf():
    result = {
"icon":"folder",
"actions":[{"id":"downloadMulti"},{"icon":"Link",
"href":"#9-17:sharelinks",
"label":"Show Links",
"id":"shareLinks"},{"id":"newFolder"},{"tasks":0,
"tree":0,
"context":0,
"id":"newFile"}],
"listViews":["List",
"Thumbs"],
"treeRoot":"filesroot",
"page":1,
"filters":[{"tree":"textroot",
"text":"Documents",
"name":"text",
"uri":"/api/v1/9:text"},{"tree":"sheetroot",
"text":"Spreadsheets",
"name":"sheet",
"uri":"/api/v1/9:sheet"},{"tree":"presentationroot",
"text":"Presentations",
"name":"presentation",
"uri":"/api/v1/9:presentation"},{"tree":"filesroot",
"text":"Clear Filter",
"name":"nofilters",
"uri":"/api/v1/Mvf/"}],
"node":[{"icon":"text",
"actions":[{"id":"download"},{"id":"downloadMulti"},{"id":"link"},{"id":"link_facebook"},{"id":"link_twitter"},{"id":"link_linkedin"},{"id":"share"},{"id":"listVersions"},{"id":"open"},{"tasks":0,
"tree":0,
"context":0,
"id":"erase"},{"id":"recycle"},{"id":"rename"},{"id":"moveCopy"}],
"floor":1,
"thumb":"null",
"desc":"Text File",
"id":"9-25",
"sharingURI":"/api/v1/sharing:9-25",
"displaySize":"6.03 KB",
"name":"test1",
"noun":"document",
"container":0,
"overlays":"null",
"details":"null",
"displayModified":"10/08/12 06:30 PM",
"uri":"test1.txt",
"modified":1349692206,
"fClass":"Text",
"open":0,
"sharingId":"sharing:9-25",
"sharingData":{"icon":"null",
"actions":[],
"listViews":["Details"],
"treeRoot":"filesroot",
"page":"null",
"filters":"null",
"node":[],
"childNoun":"permissions",
"desc":"Sharing settings for test1",
"id":"sharing:9-25",
"orderDirection":"null",
"parent":"/Mvf/test1.txt",
"noun":"document",
"name":"Sharing",
"container":[],
"overlays":"null",
"uri":"/sharing:9-25",
"searchId":"search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:sharing:9-25",
"listMore":0,
"orderBy":"null",
"columns":[{"width":230,
"orderBy":"name",
"name":"entity",
"label":"Entity",
"param":"name"},{"width":60,
"orderBy":"collaborator",
"name":"collaborator",
"label":"Collaborator",
"param":"collaborator"},{"width":250,
"orderBy":"tooltip",
"name":"tooltip",
"label":"Description",
"param":"tooltip"}],
"perPage":100,
"items":0,
"pages":1}},{"icon":"",
"actions":[{"id":"download"},{"id":"downloadMulti"},{"id":"link"},{"id":"link_facebook"},{"id":"link_twitter"},{"id":"link_linkedin"},{"id":"share"},{"id":"listVersions"},{"id":"open"},{"tasks":0,
"tree":0,
"context":0,
"id":"erase"},{"id":"recycle"},{"id":"rename"},{"id":"moveCopy"}],
"floor":1,
"thumb":"null",
"desc":"Microsoft Windows Shortcut",
"id":"9-27",
"sharingURI":"/api/v1/sharing:9-27",
"displaySize":"1.75 KB",
"name":"WinSCP",
"noun":"file",
"container":0,
"overlays":"null",
"details":"null",
"displayModified":"10/08/12 06:30 PM",
"uri":"WinSCP.lnk",
"modified":1349692209,
"fClass":"",
"open":0,
"sharingId":"sharing:9-27",
"sharingData":{"icon":"null",
"actions":[],
"listViews":["Details"],
"treeRoot":"filesroot",
"page":"null",
"filters":"null",
"node":[],
"childNoun":"permissions",
"desc":"Sharing settings for WinSCP",
"id":"sharing:9-27",
"orderDirection":"null",
"parent":"/Mvf/WinSCP.lnk",
"noun":"file",
"name":"Sharing",
"container":[],
"overlays":"null",
"uri":"/sharing:9-27",
"searchId":"search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:sharing:9-27",
"listMore":0,
"orderBy":"null",
"columns":[{"width":230,
"orderBy":"name",
"name":"entity",
"label":"Entity",
"param":"name"},{"width":60,
"orderBy":"collaborator",
"name":"collaborator",
"label":"Collaborator",
"param":"collaborator"},{"width":250,
"orderBy":"tooltip",
"name":"tooltip",
"label":"Description",
"param":"tooltip"}],
"perPage":100,
"items":0,
"pages":1}}],
"childNoun":"items",
"searchURI":"/api/v1/search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:9-17",
"desc":"File Folder",
"id":"9-17",
"canDragDropFiles":1,
"orderDirection":"Asc",
"parent":"null",
"noun":"folder",
"name":"My Files",
"container":1,
"overlays":"null",
"details":"<div id=\"account_info\" class=\"container\">\n\n\t<div class=\"account_item account_plan\">\n\t\t<h1>Default TeamFolder Org</h1>\t\t\t<a href=\"javascript:popupWindow('ChangePassword',245,500,false,'/Pages/MyAccount/?action=password');\">Change Password</a>\t\t\t</div>\n\t\n\t<div class=\"account_item account_space\">\t\t\t\t<h1>Using 7.78 KB of 1 GB</h1>\t\t\t<a onclick=\"Action.DialogAction({ page: 'Pages/Dialog/SpaceUsage.htm', width: 450 });\">View details</a>\t</div>\n\t\t\t\n</div>\n\n<div id=\"info_right_bottom\" class=\"container\">\n\t\n\t<div class=\"clear\"></div>\n\n\t<div id=\"quick-links\" class=\"info_spacer_top\">\n\t\t<ul>\t\t\t<li><a href=\"#/updates/\" class=\"history\">View events history</a></li><li><a href=\"https://%s/pages/en/smartdrive\" class=\"downloads\" target=\"_blank\">Downloads</a></li>\t\t\t<li><a href=\"http://%s/HelpWindowsClientQuickStart.htm\" target=\"_blank\" class=\"help\">Get help</a></li>\t\t</ul>\n\t</div>\n\t\n</div>\n\n<script type=\"text/javascript\">\n\t\n\t(function(){\t\t\n\t\t$('info_right_text').update('\tAccount Information');\n\t\t\n\t\tfunction heightCheck(){\n\t\t\tvar b = $('info_right_bottom');\n\t\t\tif( !b ) return Event.stopObserving(window, 'resize', this);\n\t\t\t// Don't show the quick links if theres not enough height\n\t\t\tvar height = $('header').getHeight() + $('info_pane_details').getHeight() + b.getHeight();\n\t\t\t(document.viewport.getHeight() < height) ? b.hide() : b.show();\n\t\t}\n\t\t\n\t\tEvent.observe(window, 'resize', heightCheck);\t\n\t\theightCheck();\n\t\t\n\t})()\n\t\n</script>"%(hostIP,hostIP),
"uri":"/api/v1/Mvf/",
"searchId":"search:BAgIMTIzNDU2NzgECAgIAwEAAAAKBUZpbGVzCQAAAGZpbGVDbGFzcw%3D%3D:9-17",
"listMore":"null",
"orderBy":"null",
"columns":[{"width":230,
"orderBy":"fileName",
"name":"name",
"label":"Name",
"param":"name"},{"width":60,
"orderBy":"fileSize",
"name":"size",
"label":"Size",
"param":"displaySize"},{"width":150,
"orderBy":"fileType",
"name":"desc",
"label":"Type",
"param":"desc"},{"width":100,
"orderBy":"fileModified",
"name":"modified",
"label":"Last Modified",
"param":"displayModified"}],
"perPage":100,
"items":"2",
"pages":1
    }

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
