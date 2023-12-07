{
  for (i = 1; i <= NR; i += 2) {
    print $i
    if (i < NR) {
      print ""
    }
  }
}

