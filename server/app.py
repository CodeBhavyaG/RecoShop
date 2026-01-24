from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/reconnect")
def index():
    return {'recomend':1}

    # ... (previous code) ...

if __name__ == "__main__":
    app.run(debug=True)
