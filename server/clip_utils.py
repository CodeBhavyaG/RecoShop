import torch
import clip
import requests
from PIL import Image
from io import BytesIO

device = "cpu"  # keep cpu for now

model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_embedding(image_url):
    response = requests.get(image_url, timeout=10)
    image = Image.open(BytesIO(response.content)).convert("RGB")

    image_input = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        embedding = model.encode_image(image_input)

    embedding = embedding / embedding.norm(dim=-1, keepdim=True)
    return embedding
