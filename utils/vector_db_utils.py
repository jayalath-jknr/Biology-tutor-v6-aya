import weaviate
from config import WEAVIATE_URL, WEAVIATE_API_KEY

def init_weaviate_client():
    client = weaviate.Client(
        url=WEAVIATE_URL,
        auth_client_secret=WEAVIATE_API_KEY
    )
    return client

def store_transcription_in_weaviate(text, video_url):
    client = init_weaviate_client()
    data_object = {
        "text": text,
        "video_url": video_url
    }
    client.data_object.create(data_object, class_name="Transcription")
