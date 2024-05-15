from pydub import AudioSegment

def extract_audio_from_video(video_path, audio_output_path="audio.wav"):
    audio = AudioSegment.from_file(video_path)
    audio.export(audio_output_path, format="wav")
    return audio_output_path
