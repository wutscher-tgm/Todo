from flask import Flask
from database import Database

app = Flask(__name__)
db = Database('db.json')
"""
Todo-List Routes
"""
@app.route("/list/", methods=['GET'])
def getList():
    return db.getList()

@app.route("/list/<list>/", methods=['POST'])
def createList(list):
    return list

@app.route("/list/<list>/", methods=['PUT'])
def updateList(list):
    return list

@app.route("/list/<list>/", methods=['DELETE'])
def deleteList(list):
    return list


"""
Todo-Item Routes
"""

@app.route("/item/<list>/", methods=['GET'])
def getItem(list):
    return list

@app.route("/item/<list>/<item>/", methods=['POST'])
def createItem(list, item):
    return list+item

@app.route("/item/<list>/<item>/", methods=['PUT'])
def updateItem(list, item):
    return list+item

@app.route("/item/<list>/<item>/", methods=['DELETE'])
def deleteItem(list, item):
    return list+item

if __name__ == '__main__':
    app.run(debug=True)