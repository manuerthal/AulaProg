# exemplo mínimo
# derivado de: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

# importações
from flask import Flask, jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json

# configurações
app = Flask(__name__) # vínculo com o Flask
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'meugrandebd.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app) # vínculo com o SQLAlchemy

class Compania(db.Model):
    # atributos da pessoa
    id = db.Column('n', db.Integer, primary_key=True)
    nome = db.Column('name',db.String(254))
    dominio = db.Column('domain',db.String(254))
    ano = db.Column('year founded', db.String(254))
    industria = db.Column('industry',db.String(254))
    tamanho = db.Column('size range', db.String(254))
    localizacao = db.Column('locality', db.String(254))
    pais = db.Column('country', db.String(254))
    linkedin = db.Column('linkedin url', db.String(254))
    empregados_atual = db.Column('current employee estimate', db.String(254))
    empregados_total = db.Column('total employee estimate', db.String(254))

    def json(self):
        base = {}
        for key, value in self.__dict__.items(): # percorrer nomes dos atributos
            if key != "_sa_instance_state": # nome de atributo doido que eu não quero
                base.update({key: value})
        #print(base)            
        return base

# para exibir versões das bibliotecas:
# pip3 freeze
# para instalar requisitos:
# pip3 install -r requirements.txt
# ou:
# pip3 install flask
# pip3 install flask_sqlalchemy


@app.route("/listar/<int:offset>/<int:limit>")
def listar(offset, limit):
    # obter os dados da classe informada
    dados = db.session.query(Compania).offset(offset).limit(limit)
    # converter dados para json
    lista_jsons = [ x.json() for x in dados ]
    # converter a lista do python para json
    resposta = jsonify(lista_jsons)
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    # permitir envio do cookie
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta

app.run(debug=True)