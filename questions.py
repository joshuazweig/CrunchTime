import os
import pymongo
import requests

user_key = os.environ.get('CRUNCHBASE_KEY')
mongo_user = os.environ.get('MONGO_USER')
mongo_pass = os.environ.get('MONGO_PASS')

MONGODB_URI = "mongodb://" + mongo_user + ":" + mongo_pass + "@ds061651.mongolab.com:61651/crunchtime"

print MONGODB_URI

client = pymongo.MongoClient(MONGODB_URI)
db = client.crunchtime

companies_db = db.companies




##Question type 1
#Year founded
def questionOne(company):
#####
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)

  question = "What year was " + company + " founded in." #get rid of org/
  correct_response = r.json()['data']['properties']['founded_on_year']

  response = [question, correct_response]

  response.append(correct_response + 12)
  response.append(correct_response - 3)
  response.append(correct_response + 4)

  return response
################################################################################

##Question type 2
#Funding to date

def questionTwo(company):
#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)

  question = "How much funding has " + company " recieved to date" #get rid of org/
  correct_response = r.json()['data']['properties']['total_funding_usd']

  response = [question, correct_response]

  response.append(correct_response / 2)
  response.append(correct_response * 1.2)
  response.append(correct_response * .75)

  return response

##################################################################################

##Question type 3
#Headquarters

def questionThree(company):
#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company + "headquarters", params=payload)

  question = "Where are the headquarters of " + company #get rid of org/
  correct_response = r.json()['data']['properties']['city']

  return response

##################################################################################


##Question type 4
#Headquarters

def questionFour(company):
#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company + "headquarters", params=payload)

  question = "Where are the headquarters of " + company #get rid of org/
  correct_response = r.json()['data']['properties']['city']


    return response

##################################################################################



##Question type 4
#Founder

def questionFive(company):
#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company + "founders", params=payload)

  question = "Which of the following people founded " + company #get rid of org/
  correct_response = r.json()['data']['properties']['name']


    return response

##################################################################################

##Question type 5
##Investors

def questionSix(company):
#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/" + company, params=payload)

  question = "Which of the following people invested in " + company #get rid of org/
  investor_list = r.json()['data']['properties']['investors']



  ##now pick random investor and for the rest of the choices cross reference them to make 
  #sure they are not on the list


    return response

##################################################################################


##Question type 6
#Founder

#####
company = "organization/facebook"
#####

  payload = {
             'user_key': user_key
             }
  #r = requests.get("https://api.crunchbase.com/v/2/" + company + "founders", params=payload)

  #question = "Which of the following people founded " + company #get rid of org/
  #correct_response = r.json()['data']['properties']['name']
##################################################################################


