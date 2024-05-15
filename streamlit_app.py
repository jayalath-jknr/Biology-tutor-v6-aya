import streamlit as st
from utils.youtube_utils import download_youtube_video
from utils.audio_utils import extract_audio_from_video
from utils.transcription_utils import transcribe_audio
from utils.subtitle_utils import generate_subtitles_with_aya, generate_subtitles_with_gpt4, generate_subtitles_with_vertex_ai
from utils.vector_db_utils import store_transcription_in_weaviate

st.title("YouTube Video Subtitle Generator")

video_url = st.text_input("Enter YouTube Video URL:")
model_choice = st.selectbox(
    "Choose a subtitle generation model:",
    ("Aya (Cohere)", "GPT-4", "Vertex AI")
)

if st.button("Generate Subtitles"):
    if video_url:
        with st.spinner("Downloading video..."):
            video_path = download_youtube_video(video_url)
            st.write("Video downloaded:", video_path)
            
            with st.spinner("Extracting audio..."):
                audio_path = extract_audio_from_video(video_path)
                st.write("Audio extracted:", audio_path)
                
                with st.spinner("Transcribing audio..."):
                    captions = transcribe_audio(audio_path)
                    st.write("Transcribed Audio:", captions)
                    
                    with st.spinner("Generating subtitles..."):
                        if model_choice == "Aya (Cohere)":
                            subtitles = generate_subtitles_with_aya(captions)
                        elif model_choice == "GPT-4":
                            subtitles = generate_subtitles_with_gpt4(captions)
                        else:
                            subtitles = generate_subtitles_with_vertex_ai(captions)
                        
                        st.write("Generated Subtitles:", subtitles)
                        store_transcription_in_weaviate(captions, video_url)
    else:
        st.error("Please enter a valid YouTube video URL.")

st.markdown("""
### Instructions:
1. Enter the YouTube video URL.
2. Choose a subtitle generation model.
3. Click on 'Generate Subtitles' to fetch and generate subtitles for the video.
""")
