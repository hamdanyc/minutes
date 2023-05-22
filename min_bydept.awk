#!/usr/bin/awk -f
BEGIN {
 dept[1] = "front office"; dept[2] = "hr"; dept[3] = "f&b"; dept[4] = "kitchen"; dept[5] = "steward"
 dept[6] = "security"; dept[7] = "purchasing"; dept[8] = "maintenance"; dept[9] = "asset"; dept[10] = "\bit\b"
 dept[11] = "house keeping"; dept[12] = "sales"; dept[13] = "finance"; dept[14] = "gm"; dept[15] = "pengurus"
 i = 0
 IGNORECASE = 1
}

# Set the input field separator to a comma
# For each line in the input file
{
  # If the first field matches the pattern "foo"
  if (/Dept#/ ~ $0) {
    # Add the current line to the group
    group = group $0 ","
    }
  else {
    # If the first field does not match the pattern "foo",
    # print the current group (if it exists) and reset the group variable
    if (group != "") {
      print group
      group = ""
    }
    # Print the current line
    print $0
  }
}

# At the end of the file, print the final group (if it exists)
END {
  if (group != "") {
    print group
  }
}
