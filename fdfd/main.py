from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = sum(request.json.values())
    c = {'sum': a}
    return c

app.run()