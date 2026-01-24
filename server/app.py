from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# First Pixabay API key
apikey1 = "54343504-5c1b955440ea9c04bd682c0b3"
url1 = f"https://pixabay.com/api/?key={apikey1}&q=yellow+flowers&image_type=photo&pretty=true"

# Second Pixabay API key 
apikey2 = "54343504-5c1b955440ea9c04bd682c0b3"
url2 = f"https://pixabay.com/api/?key={apikey2}&q=sunset&image_type=photo&pretty=true"

@app.route("/reconnect")
def index():
    # Call first API
    response1 = requests.get(url1)
    if response1.status_code == 200:
        data1 = response1.json()
    else:
        data1 = {"error": f"API1 error {response1.status_code}"}

    
    response2 = requests.get(url2)
    if response2.status_code == 200:
        data2 = response2.json()
    else:
        data2 = {"error": f"API2 error {response2.status_code}"}


    combined_data = [
         data1,
         data2]
    

    return jsonify(combined_data)

if __name__ == "__main__":
    app.run(debug=True)

