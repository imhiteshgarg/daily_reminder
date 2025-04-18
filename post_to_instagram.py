import requests
import os

ACCESS_TOKEN = os.environ.get("IG_ACCESS_TOKEN")
IG_USER_ID = os.environ.get("IG_USER_ID")
IMAGE_URL = 'it-gets-easier.png'  # public URL to the image
CAPTION = "Daily post from GitHub Actions!"

def create_media_object():
    url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    payload = {
        "image_url": IMAGE_URL,
        "caption": CAPTION,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()["id"]

def publish_media(media_id):
    url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print("Post published!")

if __name__ == "__main__":
    media_id = create_media_object()
    publish_media(media_id)
