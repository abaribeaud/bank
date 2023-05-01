from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import logging

app = Flask(__name__)
CORS(app)

categories = pd.read_csv("../db-bank/categories_dump.csv")
sous_categories = pd.read_csv("../db-bank/sub_categories_dump.csv")
operations = pd.read_csv("../db-bank/transactions_dump.csv")

col = {"tr_id": "id","tr_date": "date","tr_type":"type","tr_amount": "montant","tr_label": "destinataire","cat_label": "categorie", "sub_label": "sousCategorie","tr_description":"intitule"}

@app.route("/categories", methods=['GET'])
def get_categories():
    """ Get categories from database """
    cat_label = categories.to_json(orient="records")
    return cat_label

@app.route("/sous_categories", methods=['GET'])
def get_sub_categories():
    """ Get categories from database """
    sub_cat = sous_categories.to_json(orient="records")
    return sub_cat

@app.route("/operations", methods=['GET'])
def get_operation():
    """ Get operations from database """
    ope = operations.to_json(orient="records")
    return ope


@app.route("/last_10_operations", methods=['GET'])
def get_last_10_operation():
    """ Get operations from database """
    last_ope = operations.sort_values(by=["tr_date"], ascending=False).head(20)
    
    last_ope = last_ope.merge(categories, left_on=["tr_category"], right_on=["cat_id"])
    last_ope = last_ope.merge(sous_categories, left_on=["tr_sub_category"], right_on=["sub_id"])
    last_ope = last_ope.drop(["tr_category", "tr_sub_category", "cat_id", "sub_id"], axis=1)

    last_ope = last_ope.rename(columns=col)
    ope = last_ope.to_json(orient="records")
    return ope


@app.route("/add_operations", methods=['POST'])
def post_operation():
    """ Post operations from database """
    print(request.json)
    # TODO : Modifier la base de données
    return "200"

@app.route("/delete_operations/<id>", methods=['DELETE'])
def delete_operation(id):
    """ Post operations from database """
    print(id)
    # TODO : Modifier la base de données
    return "200"