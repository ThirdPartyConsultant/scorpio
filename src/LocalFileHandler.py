import os,sys

class LocalFileHandler:
    def __init__(self, rootPath="/tmp/"):
        self.rootPath = rootPath

    def listDir(self,path=""):
        elements = os.listdir(self.rootPath+path)
        result = []
        for element in elements:
            p = {}
            p['name'] = element
            print self.rootPath+path+"/"+element
            if os.path.isdir(self.rootPath+path+"/"+element):
                p['type'] = "dir"
            else:
                p['type'] = "object"
            result.append(p)

        return result

    def mkdirs(self,path=""):
        os.makedirs(self.rootPath+path)

    def listRoot(self):
        return os.listDir(self.rootPath)
        
