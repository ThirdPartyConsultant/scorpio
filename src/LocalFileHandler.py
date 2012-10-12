import os,sys,time,copy

class LocalFileHandler:
    def __init__(self, rootPath="/tmp"):
        self.rootPath = rootPath

    def listDir(self,path=""):
        elements = os.listdir(self.rootPath+path)
        result = []
        for element in elements:
            p = {}
            p['name'] = element
            print self.rootPath+path+element
            itemInfo = os.stat(self.rootPath+path+element)
            if os.path.isdir(self.rootPath+path+element):
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
        
class ThinSyncListStructure:
    def __init__(self):
        self.curList = []
        self.filestruct =  {"icon":"text",
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
                            "uri":"test1.txt",
                            "modified":1349692206,
                            "fClass":"Text",
                            "open":0,
                            "sharingId":"",
                            "sharingData":{}
                           }
        self.dirstruct = {}
    
    def addObject(self,dirfile):
        self.curList.append(dirfile)
        
    def createFile(self,myfile):
    	ret = copy.deepcopy(self.filestruct)
    	ret['name'] = myfile['name']
    	ret['displayModified'] = myfile['displaytime']
    	ret['displaySize'] = myfile['displaysize']
    	ret['modified'] = myfile['mtime']
    	ret['uri'] = myfile['name']
    	
    	return ret
    	
    def testList(self):
    	self.addObject(self.filestruct)
        self.addObject(self.filestruct)
        print self.curList
        
    def getLists(self):
        return self.curList



class ThinSyncDirFileCreate:
	def __init__(self, curPath="/"):
		self.localObj = LocalFileHandler()
		self.localList = self.localObj.listDir(curPath)
		self.thinSyncStruc = ThinSyncListStructure()
		self.curList = []
	
	def getLists(self):
	
		return    
	def processFileList(self):
		for item in self.localList:
			if item['type'] == 'object':
				print item['name']
				ret = self.thinSyncStruc.createFile(item)
				self.thinSyncStruc.addObject(ret)
				
		return self.thinSyncStruc.getLists()

	
	def testList(self):
	    print self.localList
	    
