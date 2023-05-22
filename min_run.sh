#! /usr/bin/sh
# summarise each files
FILES="fo hr fb kitchen steward security purchase maint aset it hk sales finance gm pengurus"
FS="fo.srt hr.srt fb.srt kitchen.srt steward.srt security.srt purchase.srt maint.srt aset.srt it.srt hk.srt sales.srt finance.srt gm.srt pengurus.srt"
SF=$1 # source file
truncate $FILES -s 0
truncate $FS -s 0
# prepare files
awk -f min_proc.awk "min_"$SF".txt"
for f in $FILES
do
  echo "gather $f file..."
  # ref to minit's para (insert)
  awk 'FNR==1 {print "\nDept:"toupper(FILENAME)}' "$f" > "$f.srt"
  # take action on each file. $f store current file name
  # summarise content; not run
  # ots "$f" | uniq >> "$f.srt"
  uniq "$f" >> "$f.srt"
done
cat $FS > "srt_"$SF".txt"
less "srt_"$SF".txt"
