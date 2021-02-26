from flask import Flask
from flask import jsonify
from db.index import Db

app = Flask(__name__)
#Instanciate data base
database = Db()

@app.route('/api/badge/<limit>', methods=['GET'], strict_slashes=False)
def get_badge_limit(limit):
    #Get data from db
    data = database.get(limit)
    data_to_return = []
    #Contruct JSON from return
    for item in data:
        data_json = {
            'value': item[0],
            'date': item[1]
        }
        data_to_return.append(data_json)
    #Return and convert to JSON
    return jsonify(data_to_return)

@app.route('/api/badge/all', methods=['GET'], strict_slashes=False)
def get_badge():
    #Get data from db
    data = database.all()
    data_to_return = []
    #Contruct JSON from return
    for item in data:
        data_json = {
            'value': item[0],
            'date': item[1]
        }
        data_to_return.append(data_json)
    #Return and convert to JSON
    return jsonify(data_to_return)

def startApi():
    app.run(debug=True)