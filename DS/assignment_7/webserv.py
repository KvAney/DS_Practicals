from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Bob"}
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify({"message": "Data added successfully"})

if __name__ == '__main__':
    app.run(debug=True)

