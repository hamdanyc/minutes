#!/bin/awk -f
BEGIN {
    cmd = system("ls -lrth")
#    while ( ( cmd | getline result ) > 0 ) {
#        print result
#    }
       	print cmd
    close(cmd);
}
