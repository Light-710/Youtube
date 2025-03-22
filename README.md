# Youtube

# YouTube Downloader

Downloads YouTube videos using `yt-dlp`.

## Usage

1.  Install `yt-dlp`: `pip install yt-dlp`
2.  Add YouTube URLs to `video_list_links` in the script.
3.  Set `download_path`.
4.  Run the script: `python your_script.py`





```markdown
# YouTube Downloader

Downloads YouTube videos using `yt-dlp`.

## Usage

1. Install `yt-dlp`:  
   ```bash
   pip install yt-dlp
   ```

2. Add YouTube URLs to `video_links` in the script.  
   Example:  
   ```python
   video_links = [
       "https://www.youtube.com/watch?v=example1",
       "https://www.youtube.com/watch?v=example2",
   ]
   ```

3. Set `download_path` to specify where files will be saved.  
   Example:  
   ```python
   download_path = "D:\\youtube_downloads"  # Change this path
   ```

4. Run the script:  
   ```bash
   python your_script.py
   ```

---

**Note**: Ensure `ffmpeg` is installed for audio extraction. Use responsibly and comply with YouTube's terms of service.
```
