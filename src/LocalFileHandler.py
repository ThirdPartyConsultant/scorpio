import os,sys,time,copy

class LocalFileHandler:
    def __init__(self, rootPath="/tmp/storage"):
        self.rootPath = rootPath

    def listDir(self,path=""):
        elements = os.listdir(self.rootPath+path)
        result = []
        for element in elements:
            p = {}
            p['name'] = element
            print self.rootPath+path+"/"+element
            itemInfo = os.stat(self.rootPath+path+"/"+element)
            if os.path.isdir(self.rootPath+path+"/"+element):
                p['type'] = "dir"
            else:
                p['type'] = "object"
            p['size'] = itemInfo.st_size
            p['displaysize'] = "%0.2f KB" % (itemInfo.st_size/(1024.0))
            p['mtime'] = int(itemInfo.st_mtime)
            p['displaytime'] = time.ctime(int(itemInfo.st_mtime))
            
            result.append(p)

        return result

    def mkdirs(self,path=""):
        os.makedirs(self.rootPath+path)

    def listRoot(self):
        return os.listdir(self.rootPath)
        
    def checkDir(self,path=""):
    	print "Checking Directroy = " + path
    	if os.path.isdir(self.rootPath+"/"+path):
    		return True
    	else:
	    	return False
    	
        
class ThinSyncListStructure:
    def __init__(self,rootPath=""):
    	print "ThinSyncStructure rootPath = " + rootPath 
    	self.rootPath = rootPath
        self.curList = []
        self.filestruct =  {"icon":"",
                           "actions":[
                             {"id":"download"},
                             {"id":"downloadMulti"},
                             {"id":"link"},
                             {"id":"link_facebook"},
                             {"id":"link_twitter"},
                             {"id":"link_linkedin"},
                             {"id":"share"},
                             {"id":"listVersions"},
                             {"id":"open"},
                             {"tasks":0,
                              "tree":0,
                              "context":0,
                              "id":"erase"},
                             {"id":"recycle"},
                             {"id":"rename"},
                             {"id":"moveCopy"}],
                            "floor":1,
                            "thumb":"null",
                            "desc":"Text File",
                            "id":"",
                            "sharingURI":"",
                            "displaySize":"6.03 KB",
                            "name":"test1",
                            "noun":"document",
                            "container":0,
                            "overlays":"null",
                            "details":"null",
                            "displayModified":"10/08/12 06:30 PM",
                            "uri":"/api/v1/Mvf",
                            "modified":1349692206,
                            "fClass":"Text",
                            "open":0,
                            "sharingId":"",
                            "sharingData":{}
                           }
        self.dirstruct = {
						"icon":"folder",
						"actions":[
  								{"id":"downloadMulti"},
  								{"icon":"Link",
   								"href":"",
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
   						"id":"2",
   						"canDragDropFiles":1,
   						"orderDirection":"Asc",
   						"parent":"null",
   						"noun":"folder",
   						"name":"My Files",
   						"container":1,
   						"overlays":"null",
   						"details":"",
   						"uri":"/api/v1/Mvf",
   						"searchId":"",
   						"listMore":"null",
   						"orderBy":"null",
   						"columns":[],
   						"perPage":100,
   						"items":"2",
   						"pages":1
   								 }
    
    def addObject(self,dirfile):
        self.curList.append(dirfile)
        
    def createFile(self,myfile):
    	ret = copy.deepcopy(self.filestruct)
    	ret['name'] = myfile['name'].split('.')[0]
    	ret['displayModified'] = myfile['displaytime']
    	ret['displaySize'] = myfile['displaysize']
    	ret['modified'] = myfile['mtime']
    	ret['uri'] += self.rootPath + "/" +myfile['name']
    	
    	return ret
    
    def createDir(self,mydir):
        ret = copy.deepcopy(self.dirstruct)
        ret['name'] = mydir['name'].split('.')[0]
    	ret['uri'] += self.rootPath + "/" + mydir['name']
    	print ret['uri']
    	
    	return ret
    	
    def getdirtemplate(self):
        return self.dirstruct
    	
    def testList(self):
    	self.addObject(self.filestruct)
        self.addObject(self.filestruct)
        print self.curList
        
    def getLists(self):
        return self.curList
        
    def setRootPath(self,setPath=''):
    	self.rootPath=setPath



class ThinSyncDirFileCreate:
	def __init__(self, curPath=""):
		self.curPath = curPath
		self.localObj = LocalFileHandler()
		self.localList = self.localObj.listDir(curPath)
		self.thinSyncStruc = ThinSyncListStructure(curPath)
		self.curList = []
		self.itemnum = 0
	
	def getLists(self):
		return
		
	def getCount(self):
		return self.itemnum
		
	def processFileList(self):
		for item in self.localList:
			self.itemnum+=1
			if item['type'] == 'object':
				self.thinSyncStruc.setRootPath(self.curPath)
				ret = self.thinSyncStruc.createFile(item)
				self.thinSyncStruc.addObject(ret)
			else:
				ret = self.thinSyncStruc.createDir(item)
				self.thinSyncStruc.addObject(ret)
				
		
		return self.thinSyncStruc.getLists()

	def processDirList(self, path=''):
		ret = self.thinSyncStruc.getdirtemplate()
		#print "process Dir List path = " + path
		subNode = ThinSyncDirFileCreate(path)
		ret['node'] = subNode.processFileList()
		modpath = path.rsplit("/",1)[0]
		ret['parent'] = "/api/v1/Mvf/" + modpath.lstrip("/")
		ret['uri'] = "/api/v1/Mvf"+path
		ret['items'] = subNode.getCount()
		ret['name'] = path.split('/').pop(-1)
		#print "My path = " + ret['name']

				
		return ret
		
	
	def testList(self):
	    print self.localList
	    

	    
