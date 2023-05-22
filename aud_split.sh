#!/bin/bash

# Input media file path
input_file=$1

# Duration of each segment in seconds (12 minutes)
segment_duration=720

# Output directory for storing segments
output_directory="aud_part/"

# Create output directory if it doesn't exist
mkdir -p "$output_directory"

# Get the total duration of the input file
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$input_file")

# Calculate the number of segments needed
num_segments=$((($duration + $segment_duration - 1) / $segment_duration)) # $((($y - $x) / 10))

# Split the input file into segments
for ((i=0; i<num_segments; i++))
do
    start_time=$((i * segment_duration))
    output_file="$output_directory/segment_$i.mp4"
    ffmpeg -i "$input_file" -ss "$start_time" -t "$segment_duration" -c copy "$output_file"
done

echo "File splitting completed."
