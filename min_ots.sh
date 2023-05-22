#! /usr/bin/sh
# summarise each files
FILES="fo hr fb kitchen steward security purchase maint aset it hk sales finance gm control"
FS="fo.srt hr.srt fb.srt kitchen.srt steward.srt security.srt purchase.srt maint.srt aset.srt it.srt hk.srt sales.srt finance.srt gm.srt control.srt"
truncate $FILES -s 0
truncate $FS -s 0
awk -f min_proc.awk $1
for f in $FILES
do
  echo "summarise $f file..."
  # ref to minit's para (insert)
  awk 'FNR==1 {print "\nDept:"toupper(FILENAME)}' "$f" > "$f.srt"
  # take action on each file. $f store current file name
  ots "$f" >> "$f.srt"
done
cat $FS > minit.txt
