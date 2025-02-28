from flask import Flask, request, jsonify
from Newthon import NewtonRaphson
 
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        return jsonify({"received_data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400



@app.route('/newton/resolve', methods=['POST'])
def newton_resolve():
    data = request.get_json()
    return NewtonRaphson.resolver(data.get('function'), data.get('initial_point'))

app.run(debug=True)
