import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_biology_explanation(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Explain the following biology concept: {question}",
        max_tokens=200,
        temperature=0.5
    )
    explanation = response.choices[0].text.strip()
    return explanation

def generate_study_material(topic):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate study material for the topic: {topic}",
        max_tokens=500,
        temperature=0.5
    )
    study_material = response.choices[0].text.strip()
    return study_material
