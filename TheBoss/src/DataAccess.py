#from pymongo import Connection # Deprecated
from pymongo import MongoClient

class DataAccess:
    def __init__(self,dbName,collectionName):
        self.host = 'localhost'
        self.port = 27017
        #self.connection = Connection(self.host, self.port)
        self.client = MongoClient(self.host, self.port)
        self.db = self.connection[dbName]
        self.collection = self.db[collectionName]
                        
    def insert(self, obj):
        objId = self.collection.insert(obj)
        print dir(self.collection)
        return objId

    def delete(self, obj):
        self.collection.remove(obj)

    def select(self, obj):
        return self.collection.find(obj)

    def update(self, oriObj, newObj ):
        self.collection.update(oriObj, newObj)


if __name__ == '__main__':
    dataAccess = DataAccess("TheBoss","person")
    
#    test_service = {"name":"test_service","desc":"test service description"}
#    test_service2 = {"name":"test_service","desc":"test service description22"}
#    objId_insert = dataAccess.insert(test_service)
#    objId_insert = dataAccess.insert(test_service2)
    objId_list = dataAccess.select({"service":"rest1","sid":"JU7q1QnK"})
    print objId_list
    tobe = {'status': 'serving'}
    for i in objId_list:
        dataAccess.update({"service":"rest1","sid":"JU7q1QnK"},{"$set":tobe})
#        dataAccess.delete(i)

    objId_list = dataAccess.select({"service":"rest1"})
    for i in objId_list:
        print i

 #   not_exist_obj = dataAccess.select({"name":"rest1"})
 #   print not_exist_obj.count()
