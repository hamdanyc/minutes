#!/usr/bin/bash

# Desc: Proces minit file from audio transcript then summarise with chatGPT
# Run in ../min_out/ dir
# Prepare transcript from audio. Input audio.m4a; Output min_dd_mm_yy.txt
# Step 1: sh ../code/min_audwh.sh > min_dd_mm_yy.txt
#       : edit transcript text (min_dd_mm_yy.txt)
# Step 2: Run awk -f ../code/min_prep.awk min_dd_mm_yy.txt | uniq > out.txt
# Step 3: remove all files, split files into chunk in dir ../min_out/chunk/
# truncate -s 0 ../min_out/chunk/*.txt
rm chunk/*.txt && awk -f ../code/min_chunk.awk  out.txt
# Step 4: Get the summary & translate
sh ../code/min_cgpt.sh
