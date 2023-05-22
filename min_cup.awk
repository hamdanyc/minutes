#!/usr/bin/awk
# 1. remove time stamp, 2. merge lines
# awk '{if (!/^[0-9]{2}:[0-9]{2}/) {printf "%s ", $0;next} {print ""}}' dept2 |awk '{printf("%s ",$0);}END{print ""}'
#
# split file by dept with tag #
# awk '/[AZ]/{close(f); f="dept" ++c;next} {print>f;}' file

awk '{if (!/^[0-9]{2}:[0-9]{2}/) print $0}' skrip.txt | awk '/[#]/{x="dept"++i;next}{print > x;}'

# summarise each files
rm *.srt
FILES="./dept*"
for f in $FILES
do
  echo "Processing $f file..."
  # ref to minit's para (insert)
  awk '/[0-9]{1}\.[0-9]/ {print $0}' "$f" > "$f.srt"
  # take action on each file. $f store current file name
  ots "$f" >> "$f.srt"
done
