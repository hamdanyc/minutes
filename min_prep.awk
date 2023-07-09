#!/usr/bin/awk -f
# usage: awk -f min_prep min_dd_mm_23.txt (from audio transcript)
# output: out.txt 
# mark dept header from dept list on match dept::keyword
# mark ref to para ie. para 2.2.1

@include "/home/abi/Documents/minit_mesyuarat_wp/code/min_lib.awk"
# "fo hr fb kitchen steward security purchase maint aset it hk sales finance gm control"
BEGIN {
   dept[1] = "front office"; dept[2] = "hr"; dept[3] = "f&b"; dept[4] = "kitchen"; dept[5] = "steward"
   dept[6] = "security"; dept[7] = "purchasing"; dept[8] = "maintenance"; dept[9] = "asset"; dept[10] = "\bit\b"
   dept[11] = "housekeeping"; dept[12] = "sales"; dept[13] = "finance"; dept[14] = "operation"; dept[15] = "pengurus"
   i = 0
   m = 0
   IGNORECASE = 1
   print "Dept#",toupper(dept[1])
   print "Syif pagi ..."
   print "Syif petang ..."
   print "Syif malam ..."
   print "daily room report"
   print "Living-in: 280"
   print "Standard: 279"
   print "Deluxe: 35"
   print "VIP: 6"
   print "Transit: 7"
   print "Standard: 3"
   print "Deluxe: 3"
   print "VIP: 1"
   print "Homestay Perwira: 0"
}
{
  rep_with()

  if (!/^[0-9]{2}:[0-9]{2}/) {  # remove time stamp & word < 2
   {
     for (i = 1; i < 16; i++)
       if (!seen[dept[i]] && $0 ~ dept[i]){
	      print "\nDept#",toupper(dept[i])
         seen[dept[i]] = 1
       }
       #if ($0 ~ /Cef/) print "\nDept#",toupper(dept[4])
       if ($0 ~ /[Aa]ssalam|selamat|good/) {
	    m++
	    print "\nDept#",toupper(dept[m])
       }
   }
   if ($0 != "") print $0
   {
      for (i = 1; i <= NF; i++)
         if ($i ~ /[0-9]+$/) {
         k = index($i,".")
         j = substr($i,1,k-1)
         if (j != "") print "-->",$i,toupper(dept[j])
       } # for loop
   }
  }
} # main
