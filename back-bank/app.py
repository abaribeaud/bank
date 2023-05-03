from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import logging
from datetime import datetime

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
    """ Get sub categories from database """
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

    # Get 10 last operations sorted by date in databse
    last_ope = operations.sort_values(by=["tr_date"], ascending=False).head(20)
    
    # Merge each operations with cat and sub cat
    last_ope = last_ope.merge(categories, left_on=["tr_category"], right_on=["cat_id"])
    last_ope = last_ope.merge(sous_categories, left_on=["tr_sub_category"], right_on=["sub_id"])
    last_ope = last_ope.drop(["tr_category", "tr_sub_category", "cat_id", "sub_id"], axis=1)

    # Rename columns
    last_ope = last_ope.rename(columns=col)

    # Sort by new column name 'Date'
    last_ope = last_ope.sort_values(by=["date"], ascending=False)
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

@app.route("/operations_with_category")
def get_operation_with_category():
    
    # Get start and end dates from request
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Get operations from database and subset with start and end dates
    ope = pd.to_datetime(operations["tr_date"], format="%Y-%m-%d %H:%M:%S") # YYYY-MM-DD HH:mm:ss
    ope = operations[(ope >= start_date) & (ope <= end_date)]

    # Subset of amount and category
    ope = ope[["tr_amount","tr_category"]]

    # Group by categorie and sum amount
    ope = ope.groupby("tr_category").sum()

    # Merge with categories and drop cat_id column
    ope = ope.merge(categories, left_index= True, right_on=["cat_id"])
    ope = ope.drop(["cat_id"], axis=1)
    
    ope = ope.to_json(orient="records")
    return ope

@app.route("/get_amount_by_month")
def get_amount_by_month():
    
    # Subset of amount and date
    ope = operations[["tr_date", "tr_amount"]].copy()

    # Add a year_month column
    ope["year_month"] = ope["tr_date"].apply(lambda x: x[:7])

    # Drop tr_date column
    ope = ope.drop("tr_date", axis=1)
    
    # Group by month_year and sum amount and add date column
    ope = ope.groupby("year_month").sum().reset_index()
    
    # Convert to json
    ope = ope.to_json(orient="records",index=True)
    return ope

@app.route("/get_balance_evolution")
def get_balance_evolution():
    
    # Subset of amount and date
    ope = operations[["tr_date", "tr_amount"]].copy()

    # Add a year_month column
    ope["year_month"] = ope["tr_date"].apply(lambda x: x[:7])

    # Drop tr_date column
    ope = ope.drop("tr_date", axis=1)
    
    # Group by month_year and sum amount and add date column
    ope = ope.groupby("year_month").sum().reset_index()
    
    # Cumsum amount
    ope["tr_amount"] = ope["tr_amount"].cumsum()

    # Convert to json
    ope = ope.to_json(orient="records",index=True)
    return ope
