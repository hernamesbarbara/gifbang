#!/usr/bin/env bash

for file in ./data/*.mp4; do
  echo "Before Conversion:"
  ffprobe -v error -select_streams v:0 -show_entries \
  stream=width,height,duration,r_frame_rate,codec_name -of default=noprint_wrappers=1 "$file"
  
  ffprobe -v error -select_streams a:0 -show_entries \
  stream=channels,codec_name -of default=noprint_wrappers=1 "$file"
  
#   filesize=$(stat -c%s "$file")
    filesize=$(stat -f%z "$file")
  
  echo "Name: $(basename "$file")"
  echo "Kind: MPEG-4 movie"
  echo "Size: $filesize bytes"
  echo "Audio channels: Stereo" # Assuming stereo as default
  echo "$(printf '*%.0s' {1..80})"
  echo

  output="${file%.mp4}_480p.mp4"
  
  ffmpeg -i "$file" \
    -vf "scale=852:480" \
    -c:v libx264 -preset slow -crf 28 \
    -c:a aac -b:a 128k "$output"
  
  if [ $? -eq 0 ]; then
    echo "Conversion successful: $output"
    echo "After Conversion:"
    
    ffprobe -v error -select_streams v:0 -show_entries \
    stream=width,height,duration,r_frame_rate,codec_name -of default=noprint_wrappers=1 "$output"
    
    ffprobe -v error -select_streams a:0 -show_entries \
    stream=channels,codec_name -of default=noprint_wrappers=1 "$output"
    
    # filesize=$(stat -c%s "$output")
    filesize=$(stat -f%z "$output")
    
    echo "Name: $(basename "$output")"
    echo "Kind: MPEG-4 movie"
    echo "Size: $filesize bytes"
    echo "Audio channels: Stereo" # Assuming stereo as default
  else
    echo "Conversion failed: $output"
    rm -f "$output"
  fi
done
