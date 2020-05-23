from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import scrapethis 


app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/mars_data"           
mongo=PyMongo(app)



# Route to render html from Mongo
@app.route("/")
def home():
    
    #Find online record from MONGO DB
    mars_data=mongo.db.collection.find_one()
    #Return template and Data
    return render_template("Base.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():

    #mars_data=mongo.db.mars_data
    mars_data=scrapethis.scrape_info()
    mongo.db.collection.update({ }, mars_data, upsert=True)
    #return 'All Done!'

if __name__ == "__main__": 
    app.run(debug=True)
