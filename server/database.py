
class Database:
    def __init__(self, path):
        self.load(path)
        pass

    """
    Todo-List Functions
    """

    def getList(self):
        return self.db

    def addList(self):
        self.db += [{
                "id": "asd1232r3w",
                "name": "name"
            }]
        self.save()
    
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
            self.db = file.read()