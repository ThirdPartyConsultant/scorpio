from pymongo import Connection

class DataAccess:
    def __init__(self,dbName,collectionName):
        self.host = 'localhost'
        self.port = 27017
        self.connection = Connection(self.host, self.port)
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



if __name__ == '__main__':
    dataAccess = DataAccess("TheBoss","service")
    test_service = {"name":"test_service","desc":"test service description"}
    test_service2 = {"name":"test_service","desc":"test service description22"}
    objId_insert = dataAccess.insert(test_service)
    objId_insert = dataAccess.insert(test_service2)
    objId_list = dataAccess.select({"name":"test_service"})
    for i in objId_list:
        print i
        dataAccess.delete(i)
