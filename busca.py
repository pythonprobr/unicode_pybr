import json

from bottle import route, run, template, request

import requests

FORM = """
<form>
<input type="text" name="name">
<input type="submit" value="Buscar">
</form>

<h1>{{name}}</h1>

<table>
% for cidade in result:
    <tr>
        <td>{{cidade['uf']}}</td>
        <td>{{cidade['nome']}}</td>
        <td>{{cidade['capital']}}</td>
    </tr>
% end
</table>
"""

@route('/')
def index():
    name = request.query.get('name', '(sem nome)')
    resp = requests.get('http://127.0.0.1:8000/busca', params={'q':name})
    resultados = json.loads(resp.text)
    return template(FORM, name=name, result=resultados)

run(host='localhost', port=8080)
