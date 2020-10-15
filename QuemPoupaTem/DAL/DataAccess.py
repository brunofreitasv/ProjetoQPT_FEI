import json
import os

class DataAccess(object):
    def __init__(self, file_name):
        self.__path = os.path.join(os.path.dirname( __file__ ), '../Data/' + file_name)
        self.dataBase = {}

    def saveChanges(self):
         with open(self.__path, 'w', encoding='utf-8') as handle:
            json.dump(self.dataBase, handle, indent = 3, ensure_ascii=False)

    def loadData(self):
         if os.path.getsize(self.__path) > 0:
            with open(self.__path, 'r', encoding='utf-8') as handle:
                self.dataBase = json.load(handle)