from flask import jsonify, Flask, request
from pymongo.mongo_client import MongoClient
from flask_basicauth import BasicAuth

uri = "mongodb+srv://chawakornpa:321654@chawakorn.f20t1pb.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'name'
app.config['BASIC_AUTH_PASSWORD'] = 'pass'
basic_auth = BasicAuth(app)

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)