from pytube import YouTube

def download_youtube_video(video_url, output_path="video.mp4"):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(filename=output_path)
    return output_path
