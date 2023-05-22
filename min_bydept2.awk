#!/usr/bin/awk -f

BEGIN {
  FS="|";    # Set the field separator to newline
  RS="";      # Set the record separator to empty string to read multiple lines as a single record
}

{
  dept = $1;  # Store the department name in a variable

  # If this is the first record for this department, print the department header
  if (!seen[dept]) {
    print(dept, "|");
    seen[dept] = 1;   # Mark the department as seen to avoid printing its header again
  }

  # Print the current record without the department name
  print substr($0, length(dept)+2);
  # print $1,$2,"..."($NF);
}

