import os

COHERE_API_KEY = os.getenv('COHERE_API_KEY', 'your_cohere_api_key_here')
GOOGLE_CREDENTIALS_PATH = 'credentials/google_credentials.json'
WEAVIATE_URL = os.getenv('WEAVIATE_URL', 'http://localhost:8080')
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY', 'your_weaviate_api_key_here')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
STABILITY_API_KEY = os.getenv('STABILITY_API_KEY', 'your_stability_api_key_here')
GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID', 'your_google_project_id_here')
GOOGLE_LOCATION = os.getenv('GOOGLE_LOCATION', 'your_google_location_here')
