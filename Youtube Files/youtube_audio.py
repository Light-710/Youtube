import yt_dlp
import os

# List of video URLs
video_links = []

# Set download path
download_path = "D:\\youtube_audios"  # Folder path to save downloaded audios

# Create the folder if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Configure download options for lossless audio quality
ydl_opts = {
    'format': 'bestaudio/best',  # Download best audio quality available
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',     # FLAC format for lossless quality
        'preferredquality': '0',      # Highest quality setting for lossless
    }],
    'verbose': True,
    'progress': True
}

# Download audio
for link in video_links:
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {link}")
            ydl.download([link])
            print(f"Successfully downloaded audio from: {link}")
    except Exception as e:
        print(f"Error downloading {link}: {str(e)}")

print(f"\nAll downloads completed! Files saved to: {download_path}")