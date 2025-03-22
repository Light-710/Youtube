import yt_dlp
import os

# Get video URL input


li=["https://youtu.be/vI6mMW17lvA?si=HADpsZ5ytadw9C4i" , "https://youtu.be/cNb9wDCRh-Q?si=ClTqHcBIP8rBCuwX" , "https://youtu.be/GuX9uFz_qnU?si=86OhNqJ_CqWfcWXM"] 



# Set download path
download_path = "D:\\youtube_videos"  # Folder to save downloaded videos
if not os.path.exists(download_path):
    os.makedirs(download_path)  # Create the folder if it doesn't exist

# Configure download options for the highest quality
ydl_opts = {
    "format": "bestvideo+bestaudio/best",  # Download best video + audio
    "merge_output_format": "mp4",         # Output format after merging
    "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),  # Save with title as file name
}

# Download video
for link in li:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(f"Download completed! Video saved to: {download_path}")
