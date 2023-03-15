from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    counter = 0
    b = list(request.json['data'])
    for i in range(len(b)):
        counter += b[i]

    c = {'sum':counter}
    return c

app.run()