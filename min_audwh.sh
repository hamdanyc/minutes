#!/bin/bash
# usage sh ../code/min_audwh.sh > min_dd_mm_yy.txt

file_list=$(ls $HOME/Documents/minit_mesyuarat_wp/audio/aud_part/*.m4a)
# rm  $HOME/Documents/minit_mesyuarat_wp/audio/aud_vtt/*
for files in $file_list
do
    # n=$(expr substr $files 54 8)
    curl https://api.openai.com/v1/audio/transcriptions \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: multipart/form-data" \
      -F model="whisper-1" \
      -F file="@$files" \
      -F response_format=vtt
    # > $HOME/Documents/minit_mesyuarat_wp/audio/aud_vtt/$n.vtt
done
