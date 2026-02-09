# RecoShop – AI Powered Image Recommendation System

## Overview

RecoShop is a full‑stack web application that mimics a Pinterest‑style image browsing experience and enhances it with an AI‑based recommendation engine. The project demonstrates how modern computer vision models can be integrated into a real web application to provide personalized, visually similar image suggestions.

The system uses React for the frontend, Flask for the backend, the Unsplash API for image data, and OpenAI’s CLIP model to generate image embeddings for similarity‑based recommendations.

---

## Demo Video

You can add a demonstration video of the project below. Simply replace the placeholder link with your own video URL.

**Project Walkthrough Video:**
[Click here to watch the demo video]((https://drive.google.com/file/d/1-W0GD4yKJurERVk5TwRUOPYzvRh5fnCx/view?usp=drive_link))

---

## Features

* Dynamic image feed fetched from Unsplash API
* Multi‑category browsing (Nature, City, Technology, Night Life)
* AI‑powered visual recommendations using CLIP embeddings
* Cosine similarity ranking for accurate results
* Clean and responsive React UI
* Flask REST API backend
* Real‑time interaction between frontend and backend

---

## Technology Stack

### Frontend

* React.js
* JavaScript
* HTML & CSS

### Backend

* Python
* Flask
* Flask‑CORS
* Requests

### AI / Machine Learning

* OpenAI CLIP Model
* PyTorch
* Scikit‑learn (Cosine Similarity)

### External APIs

* Unsplash Image API

---

## Architecture

The project follows a three‑layer architecture:

1. **Frontend Layer (React)**

   * Displays images to users
   * Sends user interactions to backend
   * Renders AI‑generated recommendations

2. **Backend Layer (Flask API)**

   * Handles API requests from React
   * Communicates with Unsplash API
   * Coordinates AI processing

3. **AI Layer (CLIP Model)**

   * Generates embeddings for images
   * Computes similarity between images
   * Ranks recommendations based on visual features

### Data Flow

User Click → React Frontend → Flask API → CLIP Embedding → Unsplash Candidates → Similarity Ranking → Recommendations Returned → Displayed in UI

---

## How Recommendations Work

1. User clicks an image on the main feed.
2. The frontend sends the image URL to the backend.
3. The backend generates an embedding using the CLIP model.
4. Candidate images are fetched from Unsplash.
5. Each candidate is embedded and compared to the clicked image using cosine similarity.
6. The most visually similar images are returned as recommendations.
7. React displays these images dynamically.

---

## Installation and Setup

### Prerequisites

* Python 3.x
* Node.js
* Unsplash Developer Account

### Backend Setup

1. Navigate to the server directory

```
cd server
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create a .env file

```
UNSPLASH_ACCESS_KEY=your_access_key_here
```

4. Run Flask server

```
python app.py
```

### Frontend Setup

1. Navigate to frontend directory

```
cd client
```

2. Install dependencies

```
npm install
```

3. Start the React app

```
npm run dev
```

---

## API Endpoints

### GET /reconnect

Returns a diverse set of images from multiple categories for the main feed.

### POST /recommend

Request body:

```
{
  "image": "image_url"
}
```

Returns AI-generated visually similar images ranked using CLIP embeddings and cosine similarity.
Returns AI‑generated visually similar images.

---

## Future Improvements

* Add user authentication
* Save user preferences and history
* Caching of embeddings for faster performance
* Pagination and infinite scrolling
* Support for more image categories
* Mobile application version

---

## Performance Notes

Because the recommendation system uses the CLIP deep learning model to compute image embeddings in real time, generating recommendations involves multiple neural network inferences and similarity calculations. As a result:

* Recommendation latency can be higher than normal API responses (typically a few seconds per request)
* Performance depends on CPU/GPU speed and internet connection
* Each click requires downloading and processing multiple images


## Author

Created as a personal learning project in full‑stack AI integration.

Feel free to contribute or improve the project!

---

### License

This project is for educational purposes and uses the Unsplash API under their developer guidelines.
