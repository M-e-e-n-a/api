from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId
import certifi

# Replace this with your MongoDB Atlas URI
mongo_uri = "mongodb+srv://web3:web3onwards2023@nfthing.irkavfn.mongodb.net/?retryWrites=true&w=majority"

# Create a Flask app
app = Flask(__name__)


# Function to connect to the MongoDB collection and retrieve data
def get_collection_data():
    # Use the certifi package to provide CA certificates
    client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
    db = client.test
    collection = db.hindi50
    data = []

    for doc in collection.find({}):
        # Check if 'other_field' exists in the document
        if 'other_field' in doc:
            data.append({"_id": str(doc["_id"]), "other_field": doc["other_field"]})
        else:
            # Handle the case where 'other_field' is missing
            data.append({"_id": str(doc["_id"]), "other_field": None})

    return data


# Route to display the content
@app.route('/api/content', methods=['GET'])
def display_content():
    data = get_collection_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

