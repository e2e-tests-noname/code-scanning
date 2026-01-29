from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/com/public-group3880252/security-analysis/test')
def hello():
    return jsonify(message="Hello, World!")



def test_add():
    print('This is test')
