import numpy as np
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "model"

catalog_features = np.load(
    DATA_DIR / "catalog_features.npy",
)

with open(DATA_DIR / "knn_index.pkl", "rb") as f:
    knn = pickle.load(f)

with open(DATA_DIR / "catalog_info.pkl", "rb") as f:
    catalog_info = pickle.load(f)

def recommend_by_index(index, top_n=5):
    query = catalog_features[index:index+1]
    distances, indices = knn.kneighbors(query)

    results = []
    for idx in indices[0][1:top_n+1]:
        results.append({
    "keyword": catalog_info["categories"][idx] or "nature"
})

    return results

if __name__ == "__main__":
    results = recommend_by_index(0)
    print("TEST RECOMMENDATIONS:")
    for r in results:
        print(r)
