from flask import Flask
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


    # ... (previous code) ...

if __name__ == "__main__":
    app.run(debug=True)
