import json

class Database:
    def __init__(self, path):
        self.path = path
        self.load()

    """
    Todo-List Functions
    """

    def getList(self):
        return self.db

    def addList(self, title):
        self.db.append({
                "id": self.getListId(),
                "title": title,
                "todos": []
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

    def getItem(self, listid):
        for list in self.db:
            if list['id'] == listid:
                return list['todos']

    def addItem(self, listid, item):
        for list in self.db:
            if int(list['id']) == int(listid):
                print('asdasdasd')
                list['todos'].append({
                    "title": item['title'],
                    "desc": item['desc']
                })
        return "success"
    
    def updateItem(self):
        pass
    
    def deleteItem(self):
        pass
    
    """
    File-Level Functions
    """

    def save(self):
        with open(self.path, "w+") as file:
            file.write(json.dumps(self.db))
    
    def load(self):
        with open(self.path, "r+") as file:
            self.db = json.loads(file.read())
    
    def getListId(self):
        maxId = 0;
        for list in self.db:
            if list['id'] > maxId:
                maxId = list['id']
        return maxId+1