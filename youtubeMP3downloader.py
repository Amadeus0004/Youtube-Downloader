import os
from pytube import Search
import yt_dlp

def search_youtube(song_name):
    """Search for the song on YouTube and return the first result URL."""
    search = Search(song_name)
    video = search.results[0]  # get the first result
    return f"https://www.youtube.com/watch?v={video.video_id}"

def download_and_convert(url, output_dir):
    """Download the video from YouTube and convert it to MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    output_dir = "Music"  # Replace with your desired output directory

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while True:
        song = input("Enter the song name (or type 'exit' to quit): ").strip()
        if song.lower() == 'exit':
            print("Exiting the program.")
            break

        if song:
            try:
                print(f"Searching for {song} on YouTube...")
                url = search_youtube(song)
                print(f"Downloading and converting {song}...")
                download_and_convert(url, output_dir)
                print(f"{song} downloaded and converted successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Please enter a valid song name.")

if __name__ == "__main__":
    main()
