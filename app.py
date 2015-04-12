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


@app.route("/question")
def question():
  
  return questions(2)
  # return "response"

################################################################################



def questions(questionNumber):
  company = get_random_company()

  payload = {
             'user_key': user_key
             }

  r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)
  if(questionNumber == 1):

    while 'founded_on_year' not in r.json()['data']['properties']:
      company = get_random_company()
      r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)

    question = "What year was " + company[13:] + " founded?" 
    correct_response = r.json()['data']['properties']['founded_on_year']
    response = [question, correct_response]
    while len(response) < 5:
      co = get_random_company()
      new_r = requests.get("https://api.crunchbase.com/v/2/" + co, params=payload)
      while 'founded_on_year' not in new_r.json()['data']['properties']:
        co = get_random_company()
        new_r = requests.get("https://api.crunchbase.com/v/2/" + co, params=payload)
      possible_response = new_r.json()['data']['properties']['founded_on_year']
      if correct_response != possible_response:
          response.append(possible_response)

      return jsonify(data=response)

  if(questionNumber == 2):
   
    while 'total_funding_usd' not in r.json()['data']['properties']:
      company = get_random_company()
      r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)

    question = "How much funding has " + company[13:] + " recieved to date?" #get rid of org/
    correct_response = r.json()['data']['properties']['total_funding_usd']
    response = [question, correct_response]
    while len(response) < 5:
      co = get_random_company()
      new_r = requests.get("https://api.crunchbase.com/v/2/" + co, params=payload)
      while 'total_funding_usd' not in new_r.json()['data']['properties']:
        co = get_random_company()
        new_r = requests.get("https://api.crunchbase.com/v/2/" + co, params=payload)
      possible_response = new_r.json()['data']['properties']['total_funding_usd']
      if correct_response != possible_response:
        response.append(possible_response)
    return jsonify(data=response)


if __name__ == "__main__":
  app.run()

