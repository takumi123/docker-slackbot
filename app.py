from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hello world from docker"})

def lambda_handler(event, context):
    with app.app_context():
        return hello().get_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)