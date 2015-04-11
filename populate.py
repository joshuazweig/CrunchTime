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

page = 1

while True:
  print page
  payload = {'organization_types': 'company', 
             'page': page,
             'user_key': user_key
             }
  r = requests.get("https://api.crunchbase.com/v/2/organizations", params=payload)

  for item in r.json()['data']['items']:
    print item['path']
    companies_db.insert({'p': item['path']})

  page += 1

  if r.json()['data']['paging']['next_page_url'] == None:
    break

print "done! finished " + page + " pages."

# for company in companies_db.find():
#   print company
