from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def subtract_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def multiply_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def divide_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))

if __name__ == '__main__':
    app.run()