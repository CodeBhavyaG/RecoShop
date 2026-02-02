from flask import Flask, jsonify ,request #,send_file
from flask_cors import CORS
import requests
"from image_recommender import recommend_by_index"
"import os"
"from dotenv import load_dotenv"
from clip_utils import get_image_embedding
from sklearn.metrics.pairwise import cosine_similarity
"import numpy as np"
from collections import defaultdict
import random


"load_dotenv()"

UNSPLASH_ACCESS_KEY = "7cYn0Bhj1-rY5ssByImS323g5Pp2fvPwNtxQj7WS-qA"#os.getenv("UNSPLASH_ACCESS_KEY")

print("Unsplash key loaded:", bool(UNSPLASH_ACCESS_KEY))
print("Unsplash key value:", UNSPLASH_ACCESS_KEY)


app = Flask(__name__)
CORS(app)
"""
# First Pixabay API key
apikey1 = "54343504-5c1b955440ea9c04bd682c0b3"
url1 = f"https://pixabay.com/api/?key={apikey1}&q=yellow+flowers&image_type=photo&pretty=true"

# Second Pixabay API key
apikey2 = "54343504-5c1b955440ea9c04bd682c0b3"
url2 = f"https://pixabay.com/api/?key={apikey2}&q=sunset&image_type=photo&pretty=true"
"""


@app.route("/reconnect")
def index():
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }

    search_queries = [
    "nature",
    "city",
    "technology",
    "night life",
    "architecture",
    "people",
    "art",
    "travel",
    "car"
    ]

    all_results = []

    for q in search_queries:
        params = {
            "query": q,
            "per_page": 10
        }

        response = requests.get(
            "https://api.unsplash.com/search/photos",
            headers=headers,
            params=params
        )

        if response.status_code == 200:
            all_results.extend(response.json()["results"])

    # Shuffle so they appear mixed
    
    random.shuffle(all_results)

    return jsonify({"results": all_results})

"""
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
"""

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    clicked_image_url = data.get("image")

    if not clicked_image_url:
        return jsonify({"error": "No image URL provided"}), 400

    # Embed clicked image
    query_embedding = get_image_embedding(clicked_image_url)

    # Get candidate images from Unsplash
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    search_queries = [
    "nature",
    "city",
    "technology",
    "night life",
    "architecture",
    "people",
    "art",
    "travel",
    "car"
    ]

    candidates = []

    for q in search_queries:
        params = {
            "query": q,
            "per_page": 15
        }
        r = requests.get(
        "https://api.unsplash.com/search/photos",
        headers=headers,
        params=params
        )

        if r.status_code == 200:
            candidates.extend(r.json()["results"])

    grouped = defaultdict(list)

    # Embed candidates + compute similarity
    for img in candidates:
        img_url = img["urls"]["regular"]

        # Assign category based on search query fallback
        category = img.get("topic_submissions")
        category = list(category.keys())[0] if category else "misc"

        try:
            emb = get_image_embedding(img_url)
            score = cosine_similarity(
                query_embedding.cpu().numpy(),
                emb.cpu().numpy()
            )[0][0]

            grouped[category].append((score, img))
        except:
            continue

    # Pick top results per category
    recommendations = []

    for category in grouped:
        grouped[category].sort(reverse=True, key=lambda x: x[0])
        for score, img in grouped[category][:2]:  # top 2 per category
            recommendations.append({
                "image": img["urls"]["regular"],
                "title": img["alt_description"] or category,
                "score": float(score),
                "category": category
            })

    # Final sort & limit
    recommendations = sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )[:8]


    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True)
