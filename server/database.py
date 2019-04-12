import json

class Database:
    def __init__(self, path):
        self.load(path)
        pass

    """
    Todo-List Functions
    """

    def getList(self):
        return self.db

    def addList(self, title):
        self.db.append({
                "id": self.getId(),
                "title": title
            })
        self.save()
        return "success"
    
    def updateList(self):
        pass
    
    def deleteList(self):
        pass
    
    """
    Todo-Item Functions
    """

    def getItem(self):
        pass

    def addItem(self):
        pass
    
    def updateItem(self):
        pass
    
    def deleteItem(self):
        pass
    
    """
    File-Level Functions
    """

    def save(self):
        pass
    
    def load(self, path):
        with open(path, "r+") as file:
            self.db = json.loads(file.read())
    
    def getId(self):
        return 1