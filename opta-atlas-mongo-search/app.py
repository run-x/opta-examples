from flask import Flask, json
from flask_pymongo import PyMongo
from os import environ
from sys import exit
from traceback import format_exc
from flask import request, render_template, jsonify
MONGO_URI = environ.get('MONGO_URI',"")
if not MONGO_URI:
    print("MONGO_URI is not defined. Was the environment variable set?")
    exit(1)
app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = MONGO_URI
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