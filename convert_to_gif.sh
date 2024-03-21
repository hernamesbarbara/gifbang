#!/usr/bin/env bash

# Video file path
video_path="./data/SKYDIVE-MOTIVATION_480p.mp4"

# Duration of the GIF in seconds
duration=10

# Output directory for GIFs
output_dir="./gifs-generated"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Check if at least one frame number (interpreted as seconds) is provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 start_time1 [start_time2 ...]"
    echo "Each start_time should correspond to a second in the video."
    exit 1
fi

# Loop through all provided start times (in seconds)
for start_time in "$@"; do

    # Output GIF path within the specified directory
    output_gif="${output_dir}/HighMotion_${start_time}.gif"

    echo "Creating GIF starting at $start_time seconds: $output_gif"

    # Convert the segment to a GIF
    ffmpeg -ss "$start_time" -t "$duration" -i "$video_path" \
    -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif "$output_gif"
done

echo "Conversion complete."
