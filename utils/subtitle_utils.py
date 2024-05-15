import cohere
import openai
from google.cloud import aiplatform
from config import COHERE_API_KEY, OPENAI_API_KEY, GOOGLE_PROJECT_ID, GOOGLE_LOCATION

def generate_subtitles_with_aya(text):
    co = cohere.Client(COHERE_API_KEY)
    response = co.generate(
        model='aya',
        prompt=text,
        max_tokens=200,
        temperature=0.5
    )
    subtitles = response.generations[0].text
    return subtitles

def generate_subtitles_with_gpt4(text):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=200,
        temperature=0.5
    )
    subtitles = response.choices[0].text.strip()
    return subtitles

def generate_subtitles_with_vertex_ai(text):
    aiplatform.init(project=GOOGLE_PROJECT_ID, location=GOOGLE_LOCATION)
    response = aiplatform.TextGeneration(model="text-bison@001").predict(inputs=[text])
    subtitles = response.predictions[0]['content']
    return subtitles
