# YouTube MP3 Downloader
This Python script allows you to search for songs on YouTube, download them as MP3 files, and save them to your computer.

## Features
- Search YouTube: Enter a song name to search for a YouTube video.
- Download and Convert: Download the video and convert it to an MP3 file.

## Requirements
To run this script, you need to have the following installed:

- Python 3.x
- pytube
- yt-dlp
- FFmpeg

### Installing Dependencies
1. **Install Python Packages**:
   - Install **pytube** and **yt-dlp** using pip:
    ```
    pip install pytube yt-dlp
    ```
2. **Install FFmpeg**:
   - Windows: Download FFmpeg from https://ffmpeg.org/download.html, extract it, and add the bin folder to your system's PATH.

## How to use
1. **Clone or donwload script**:
   - Download the script from the repository or copy the code to your local machine.
2. **Run the script**:
   - Execute the script using Python:
     ```
     python youtube_mp3_downloader.py
     ```
3. **Follow the promts:**
   - Enter teh song name when promted
   - The script will search for the song on YouTube, download the first result, and convert it to an MP3 file in the specified output directory

## Contributing
if you find any bugs or have feature re`uests, please open and issue or submit a pull request. Contrubutions are wellcome!

## Acknowledgments
- This project uses **pytube** for searching YouTube and **yt-dlp** for downloading and converting videos.
- Thanks to the open-source community for the tools and libraries used in this project.
