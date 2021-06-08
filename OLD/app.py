from flask import Flask
from flask import request, redirect

app = Flask(__name__)


@app.route('/')
def Hello():
    my_name = 'John'
    return f'Hello {my_name}'


@app.route('/blog/<id>', methods=['GET'])
def blok(id):
    return f"This is blog entry #{id}"


@app.route('/message', methods=['POST'])
def message():
    print(request.json())
    return redirect("/message")

