from flask import Flask , request , jsonify
from flask_cors import CORS
import requests 
app = Flask(__name__)

CORS(app)
apikey="54343504-5c1b955440ea9c04bd682c0b3"
urlvariable="https://pixabay.com/api/?key=54343504-5c1b955440ea9c04bd682c0b3&q=yellow+flowers&image_type=photo&pretty=true"
response=requests.get(urlvariable)
if response.status_code==200 :
    data = response.json()
else :
    data=f"error {response.status_code}" 
@app.route("/reconnect")
def index():
    return data

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

    # ... (previous code) ...

if __name__ == "__main__":
    app.run(debug=True)
