#!/usr/bin/awk -f
# input file min_dd_mm_yy.txt
# output file chunk

BEGIN {
  RS = "\n\n"     # Set the record separator to two consecutive newlines to read text groups
  max_words_per_chunk = 750
}

/Dept#/ {
  # Split the group into chunks of max_words_per_chunk words each
  split_into_chunks($0)
}

function split_into_chunks(text) {
  word_count = 0
  chunk_count = 0
  chunks = ""

  # Split the text into lines and process each line
  num_lines = split(text, lines, "\n")
  for (i = 1; i <= num_lines; i++) {
    # Split the line into words and count them
    num_words = split(lines[i], words, " ")
    word_count += num_words

    # If the current chunk has reached the maximum word count,
    # summarize it and start a new chunk
    if (word_count > max_words_per_chunk) {
      summarize_chunk(chunks)
      word_count = num_words
      chunk_count++
      chunks = ""
    }
    # Append the current line to the current chunk
    chunks = chunks lines[i] "\n"
  }
  # print "==>",chunks
  # Summarize any remaining chunk
  if (word_count > 0) {
    summarize_chunk(chunks)
  }
}

function summarize_chunk(text) {
  summary = text
  # Output the summary to a file
  summary_filename = sprintf("chunk/summary%d.txt", NR)
  print summary  > summary_filename
}
