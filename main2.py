import requests

host = 'http://127.0.0.1:5000/'

r = requests.post(host,
                  json={'data': [1, 2, 3]})
print(r.text)

r = requests.post(host,
                  json={'data': [1, 2, 3]})

assert r.json() == {'sum': 6}

r2 = requests.post(host,
                  json={'data': [-1, -2, -3]})

assert r2.json() == {'sum': -6}


print(r2.text)


