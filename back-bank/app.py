from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import logging

app = Flask(__name__)
CORS(app)

categories = pd.read_csv("../db-bank/categories_dump.csv")
sous_categories = pd.read_csv("../db-bank/sub_categories_dump.csv")


logging.info(categories)

@app.route("/categories")
def get_categories():
    """ Get categories on database """
    cat_label = categories.to_json(orient="records")
    return cat_label

@app.route("/sous_categories")
def get_sub_categories():
    """ Get categories on database """
    sub_cat = sous_categories.to_json(orient="records")
    return sub_cat