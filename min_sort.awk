#!/usr/bin/awk -f
# GPLv3 appears here
# usage: ./sorter.awk -v var=NUM FILE

# BEGIN { FS=";"; }

{ # dump each lines into an array; match the marker
    ARRAY[$0] = $R;
}

END {
    asorti(ARRAY,SARRAY);
    # get length
    j = length(SARRAY);
    
    for (i = 1; i <= j; i++) {
        printf("%s %s\n", SARRAY[i],ARRAY[SARRAY[i]])
    }
}
