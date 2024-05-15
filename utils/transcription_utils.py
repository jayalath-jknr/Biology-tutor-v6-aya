from google.cloud import speech
import io
import os

def transcribe_audio(audio_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials/google_credentials.json'
    client = speech.SpeechClient()

    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)

    return " ".join(transcriptions)
