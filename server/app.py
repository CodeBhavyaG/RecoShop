from flask import Flask, jsonify ,request
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


    
    
    
    joined_data = data1.copy()
    joined_data['hits'].extend(data2['hits'])
    joined_data['total'] += data2['total']
    joined_data['totalHits'] += data2['totalHits']
    

    return jsonify(joined_data)


@app.route('/handle-click', methods=['POST'])
def handle_click():
    # 1. Get the JSON data sent from React
    data = request.get_json()
    
    # 2. Access specific fields
    item_id = data.get('id')
    username = data.get('title')
    
    print(f"User clicked item {item_id} by {username}") # This shows in your terminal

    # 3. Always send a response back to React
    return jsonify({"status": "success", "received": item_id}), 200

if __name__ == "__main__":
    app.run(debug=True)
