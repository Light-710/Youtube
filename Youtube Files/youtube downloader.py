import yt_dlp
import os

# Function to get user input for download path
def get_download_path():
    while True:
        path = input("Enter the download path (e.g., D:\\youtube_videos): ").strip()
        if path:
            return path
        print("Download path cannot be empty. Please try again.")

# Function to get video URLs from the user
def get_video_urls():
    video_list_links = []
    print("Enter YouTube video URLs (one at a time). Type 'done' when finished:")
    while True:
        url = input("Enter URL: ").strip()
        if url.lower() == "done":
            break
        if url:
            video_list_links.append(url)
        else:
            print("URL cannot be empty. Please try again.")
    return video_list_links

# Main script
if __name__ == "__main__":
    # Get download path from user
    download_path = get_download_path()

    # Create the folder if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Get video URLs from user
    video_list_links = get_video_urls()

    # Configure download options for the highest quality
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Download best video + audio
        "merge_output_format": "mp4",         # Output format after merging
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),  # Save with title as file name
    }

    # Download videos
    if video_list_links:
        for link in video_list_links:
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    print(f"Downloading: {link}")
                    ydl.download([link])
                    print(f"Download completed for: {link}")
            except Exception as e:
                print(f"Error downloading {link}: {str(e)}")
        print(f"\nAll downloads completed! Files saved to: {download_path}")
    else:
        print("No URLs provided. Exiting.")