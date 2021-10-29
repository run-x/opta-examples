from flask import Flask, json
from flask_pymongo import PyMongo
from os import environ
from sys import exit
from traceback import format_exc
from flask import request, render_template, jsonify

def make_conn_string():

    MONGO_URI = environ.get('MONGO_URI',"")
    MONGO_PASSWORD = environ.get('DB_PASSWORD', "")
    MONGO_USER = environ.get('DB_USER', "")
    DATABASE_NAME = environ.get('DATABASE_NAME',"")

    if "" in set([MONGO_URI,MONGO_PASSWORD,MONGO_USER]):
        print("Are the 3 environment variables set? MONGO_URI, MONGO_PASSWORD, MONGO_USER")
        exit(1)
    parts = MONGO_URI.split("//")
    if DATABASE_NAME:
        rtnStr = "//".join([
            parts[0],
            MONGO_USER + ":" + MONGO_PASSWORD + "@" + parts[1] + "/" + DATABASE_NAME + "?retryWrites=true&w=majority"
        ])
    else:
        rtnStr = "//".join([
            parts[0],
            MONGO_USER + ":" + MONGO_PASSWORD + "@" + parts[1]
        ])

    return rtnStr

MONGO_CONN_STRING = make_conn_string()
app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = MONGO_CONN_STRING
mongo = PyMongo(app) 
    
@app.route("/")
def send_html():
    return render_template('index.html')

@app.route("/search",  strict_slashes=False)
def search():
    query = request.args.get('arg')
    if not query:
        return []
    pipeline = [
    {
        "$search": {
            "text": {
                "query": query,
                "path": "fullplot"
            },
            "highlight": {
                "path": "fullplot"
            }
        }},
    {
        "$project": {
            "title": 1,
            "_id": 0,
            "year": 1,
            "fullplot": 1,
            "score": { "$meta": 'searchScore' },
            "highlight": { "$meta": 'searchHighlights' }
        }},
    {
        "$limit": 10
    }
    ]
    results = mongo.db.movies.aggregate(pipeline)
    
    resp = jsonify(list(results))
    return resp