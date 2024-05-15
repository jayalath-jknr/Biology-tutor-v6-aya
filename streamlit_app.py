import streamlit as st
from utils.youtube_utils import download_youtube_video
from utils.audio_utils import extract_audio_from_video
from utils.transcription_utils import transcribe_audio
from utils.subtitle_utils import generate_subtitles_with_aya, generate_subtitles_with_gpt4, generate_subtitles_with_vertex_ai
from utils.vector_db_utils import store_transcription_in_weaviate

st.title("AI-based Biology Tutor Application")
st.write("""
Welcome to the AI-based Biology Tutor Application!

This application is designed to help students learn and understand various biology concepts through advanced AI technology.

**Features:**
- **Subtitle Generation for Biology Videos**: Generate subtitles for biology-related YouTube videos.
- **Biology Tutor**: Ask questions about biology concepts and get detailed explanations.
- **Study Material Generation**: Generate comprehensive study materials for different biology topics.

Use the navigation menu to explore different functionalities.
""")