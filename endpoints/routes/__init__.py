from flask import jsonify, Blueprint, request
from endpoints.model import Endpoint
from endpoints.exceptions import Exceptions

routes_blueprint = Blueprint('routes_blueprint', __name__)
valida = Endpoint()

@routes_blueprint.errorhandler(Exceptions)
def error_handler(error):
    return jsonify({"message": error.message}), error.code

partes_carro = ["porta", "teto", "para-choque", "porta-malas", "volante"]

@routes_blueprint.route('/hello', methods=['GET'])
def hello():
    if(request.args.get('nome') == None):
        return jsonify({
            "message": "Olá! Como vai?"
        })
    else:
        nome = request.args.get('nome')
        return jsonify({
            "message": f'Olá {nome}! Seja bem vindo!'
        })

@routes_blueprint.route('/lista', methods=['GET'])
def lista():
    return jsonify(partes_carro), 200

@routes_blueprint.route('/lista/<string:nome>', methods=['GET'])
def elementoLista(nome):
    nome = nome.lower()
    retorno = valida.elementAlreadyExists(nome, partes_carro)
    return jsonify({
      "message": f'Elemento na lista: {retorno}'
    }), 200

@routes_blueprint.route('/lista/<string:nome>', methods=['POST'])
def addElemento(nome):
    nome = nome.lower()
    valida.addElement(nome, partes_carro)
    return jsonify({
      "message": "Elemento salvo"
    }), 201

@routes_blueprint.route('/lista/<string:nome>', methods=['DELETE'])
def removeElemento(nome):
    nome = nome.lower()
    valida.deleteElement(nome, partes_carro)
    return jsonify({
      "message": "Elemento deletado"
    }), 204

