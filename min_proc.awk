#!/usr/bin/awk -f

@include "min_lib.awk"
# "fo hr fb kitchen steward security purchase maint aset it hk sales finance gm control"
BEGIN {
 dept[1] = "fo"; dept[2] = "hr"; dept[3] = "fb"; dept[4] = "kitchen"; dept[5] = "steward"
 dept[6] = "security"; dept[7] = "purchase"; dept[8] = "maint"; dept[9] = "aset"; dept[10] = "it"
 dept[11] = "hk"; dept[12] = "sales"; dept[13] = "finance"; dept[14] = "gm"; dept[15] = "pengurus"
 i = 0
 IGNORECASE = 1
}
{
  rep_with()
  if ($1 == "dept#") { # split file at the marker & write
    x = dept[$2]
    next
  }
  if (!/^[0-9]{2}:[0-9]{2}/) {
  if (NF >= 2 )  # remove time stamp & word < 2
    print $0 > x
  else; if (/[0-9]{1}\.[0-9]|tangguh|selesai|kekal|progress|remove|remain|done|settle|keluar/) print $0 > x
  }
}
