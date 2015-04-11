import os, sys
from flask import Flask, render_template, jsonify
import pymongo
import requests
import random

user_key = os.environ.get('CRUNCHBASE_KEY')
mongo_user = os.environ.get('MONGO_USER')
mongo_pass = os.environ.get('MONGO_PASS')

if not user_key or not mongo_user or not mongo_pass:
  print "must export vars"
  sys.exit(0)

MONGODB_URI = "mongodb://" + mongo_user + ":" + mongo_pass + "@ds061651.mongolab.com:61651/crunchtime"

client = pymongo.MongoClient(MONGODB_URI)
db = client.crunchtime
companies_db = db.companies

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/random")
def rand():
  return get_random_company() 

def get_random_company():  
  company = companies_db.find().limit( -1 ).skip( int(random.random() * companies_db.count()) ).next()
  return company['p']

if __name__ == "__main__":
	app.run()