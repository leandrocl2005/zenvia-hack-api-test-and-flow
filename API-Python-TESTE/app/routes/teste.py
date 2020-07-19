from math import ceil
from os import path
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from flask import request as FlaskRequest, current_app as app, Response
from ..models.base import db, api

from flask import jsonify
from flask import Blueprint, render_template, abort
import uuid

simple_page = Blueprint('simple_page', __name__) 

###########
### API de teste até a parte de back do node ficar ok.
###########

@simple_page.route('/api/oferecer',methods=['POST'])
def Procura_post():
    if FlaskRequest.method == 'POST':
        DataJson=FlaskRequest.get_json()
        print(DataJson)
        return jsonify({ "resultado": "ok" }) 
    return "",400

@simple_page.route('/api/procura',methods=['POST'])
def Oferecer_post():
    if FlaskRequest.method == 'POST':
        DataJson=FlaskRequest.get_json()
        print(DataJson)
        lista={
            "Resultado1": {"Distancia": "2627 metros","Empresa": "faço torta de maçã","Endereco": "Av. Orlando Rodrigues da Cunha 1677 Uberaba","Telefone": "33522251"},
            "Resultado2": {"Distancia": "3257 metros","Empresa": "faço empadinhas", "Endereco": "R. Tristão de Castro 265 Uberaba", "Telefone": "742825626"}
            }
        return jsonify({ "resultado": "ok" , "data":lista}) # jsonify(DataJson) #, 200
    return "",400
