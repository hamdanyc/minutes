#!/bin/bash

sed -E 's/[0-9]{2}:[0-9]{2}.000 --> [0-9]{2}:[0-9]{2}.000//;s/[0-9]{2}:[0-9]{2}:[0-9]{2}.000 --> [0-9]{2}:[0-9]{2}:[0-9]{2}.000//;/^$/d;s/item#/\n&/' $1 > out.txt
if test -f "chunk/content1.txt"
then
    echo "Remove files on your filesystem."
    rm chunk/*.txt
fi
awk -f ../code/min_chunk.awk out.txt
sh ../code/min_cgpt.sh > $2
