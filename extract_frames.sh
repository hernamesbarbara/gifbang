#!/usr/bin/env bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path/to/video.mp4>"
    exit 1
fi

# Get the video file path from the command line
video_path="$1"

# Check if the file exists
if [ ! -f "$video_path" ]; then
    echo "Error: File not found at '$video_path'"
    exit 1
fi

# Directory where to save extracted frames
output_dir="./frames"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Extract frames at one frame per second
ffmpeg -i "$video_path" -vf "fps=1" "$output_dir/frame_%04d.png"

echo "Frames extracted to $output_dir"
