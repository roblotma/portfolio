from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, this is my portfolio! My name is Mathilde, lot of love'