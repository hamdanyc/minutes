#!/usr/bin/awk -f

BEGIN {
  word_count = 0
  chunk_count = 0
  max_words_per_chunk = 500
}

{
  # Split the line into words and count them
  num_words = split($0, words, " ")
  word_count += num_words
  
  # If the current chunk has reached the maximum word count,
  # write it to a file and start a new chunk
  if (word_count > max_words_per_chunk) {
    write_chunk()
    word_count = num_words
    chunk_count++
  }
  
  # Append the current line to the current chunk
  chunks[chunk_count] = chunks[chunk_count] $0 "\n"
}

END {
  # Write any remaining chunks to files
  if (word_count > 0) {
    write_chunk()
  }
}

function write_chunk() {
  chunk_filename = sprintf("chunk/chunk%d.txt", chunk_count + 1)
  print chunks[chunk_count] > chunk_filename
}
