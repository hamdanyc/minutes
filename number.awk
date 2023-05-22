#!/usr/bin/awk -f

{
  for (i = 1; i <= NF; i++) {
    if ($i ~ /[0-9]+$/) {
      j = index($i,".")
      print $i,substr($i,1,j-1)
    }
  }
}
