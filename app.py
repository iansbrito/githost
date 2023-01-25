from flask import Flask, request, jsonify, make_response
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/calculator', methods=['POST'])
def calculator():
    dados=json.loads(request.data)
    a= str(dados.get('a'))
    b= str(dados.get('b'))
    if not a or not b:
        return make_response("Informe o número de A e B.", 400)
    try:    
        a=float(a)
        b=float(b)
    except ValueError:
        return make_response("Informe o número de A e B.", 400)
    c = (a**2 + b**2)**0.5
    
    return jsonify({'a': a,'b':b, 'c':c})
@app.route('/ca', methods=['POST'])
def ca():
    dados=json.loads(request.data)
    a= str(dados.get('a'))
    b= str(dados.get('b'))
    if not a or not b:
        return make_response("Informe o número de A e B.", 400)
    try:    
        a=float(a)
        b=float(b)
    except ValueError:
        return make_response("Informe o número de A e B.", 400)
    if a>b:
        co = float(b)
        h = float(a)
    if b>a:
        co=float(a)
        h=float(b)
    ca=((h**2)-(co**2))**(1/2)
    
    return jsonify({'a': a,'b':b, 'c':ca})


if __name__ == '__main__':
    app.run(debug=True)
