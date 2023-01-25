from flask import Flask, request, jsonify, make_response
import json
from flask_cors import CORS


def validar_valores():
    if not request.data:
        raise Exception("Informe o número de A e B.")
    
    dados = json.loads(request.data)
    valor_a = dados.get('a')
    valor_b = dados.get('b')

    if not valor_a or not valor_b:
        raise Exception("Informe o número de A e B.")
    
    valor_a = float(valor_a)
    valor_b = float(valor_b)
    return valor_a, valor_b


app = Flask(__name__)
CORS(app)


@app.route('/calculator/hipotenusa', methods=['POST'])
def calcular_hipotenusa_route():
    try:
        cateto_a, cateto_b = validar_valores()
    except ValueError:
        return make_response("O valor de a e b deve ser um número.", 400)
    except Exception:
        return make_response("Informe o número de A e B.", 400)

    hipotenusa = (cateto_a**2 + cateto_b**2)**0.5

    return jsonify({'valor_a': cateto_a, 'valor_b': cateto_b, 'valor_c': hipotenusa})


@app.route('/calculator/cateto', methods=['POST'])
def calcular_cateto_route():
    try:
        valor_a, valor_b = validar_valores()
    except ValueError:
        return make_response("O valor de a e b deve ser um número.", 400)
    except Exception:
        return make_response("Informe o número de A e B.", 400)

    cateto_oposto = valor_a
    hipotenusa = valor_b

    if valor_a > valor_b:
        cateto_oposto = valor_b
        hipotenusa = valor_a       
    
    cateto_adjacente = ((hipotenusa**2)-(cateto_oposto**2))**(1/2)

    return jsonify({'valor_a': cateto_oposto, 'valor_b': hipotenusa, 'valor_c': cateto_adjacente})


if __name__ == '__main__':
    app.run(debug=True)
