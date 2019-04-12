from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database

app = Flask(__name__)
CORS(app)

db = Database('db.json')


#parser = reqparse.RequestParser()
#parser.add_argument('titel')
#args = parser.parse_args()

"""
Todo-List Routes
"""

@app.route("/list/", methods=['GET', 'POST'])
def list():
    if request.method == 'GET':
        return jsonify(db.getList())
    else:
        return db.addList(request.args.get('title'))

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
def addItem(list, item):
    return list+item

@app.route("/item/<list>/<item>/", methods=['PUT'])
def updateItem(list, item):
    return list+item

@app.route("/item/<list>/<item>/", methods=['DELETE'])
def deleteItem(list, item):
    return list+item

if __name__ == '__main__':
    app.run(debug=True)