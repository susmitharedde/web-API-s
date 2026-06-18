from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello, World!"
    })

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)

    return jsonify({
        "num1": num1,
        "num2": num2,
        "sum": num1 + num2
    })

if __name__ == '__main__':
    app.run(debug=True)
