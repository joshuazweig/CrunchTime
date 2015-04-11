from flask import Flask, render_template
import pymongo

MONGODB_URI = "mongodb://localhost:27017/crunchtime"

app = Flask(__name__)

client = pymongo.MongoClient(MONGODB_URI)
db = client.knz
companies_db = db.companies

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()