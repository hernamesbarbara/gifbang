#!/usr/bin/env python3
import subprocess
import os

# Path to the urls.txt file
urls_file_path = 'urls.txt'

# Function to download video as .webm


def download_video_as_webm(url):
    command = f'yt-dlp -f bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm] {url} -o "%(title)s.%(ext)s"'
    subprocess.run(command, shell=True)

# Function to convert .webm to .mp4


def convert_webm_to_mp4(webm_file):
    base = os.path.splitext(webm_file)[0]
    mp4_file = f"{base}.mp4"
    command = f'ffmpeg -i "{webm_file}" -vf "scale=\'min(1280,iw)\':min\'(720,ih)\':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -crf 23 -preset veryfast -an "{mp4_file}"'
    subprocess.run(command, shell=True)
    return mp4_file


# Read URLs from file and download videos
with open(urls_file_path, 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    if url:
        download_video_as_webm(url)

# Convert downloaded .webm files to .mp4 and delete .webm files
for file in os.listdir('.'):
    if file.endswith('.webm'):
        mp4_file = convert_webm_to_mp4(file)
        if os.path.exists(mp4_file):  # Check if conversion was successful
            os.remove(file)  # Delete the original .webm file
