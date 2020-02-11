from flask import Flask, jsonify, request
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"about" : "hello world" })
if __name__ == "__main__":
    app.run(debug=True)