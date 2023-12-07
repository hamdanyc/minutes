#!/bin/awk -f

BEGIN {
    FS = "/"
}

# Function to extract numeric value from the file path
function extractNumericValue(path) {
    match(path, /[0-9]+/)
    return substr(path, RSTART, RLENGTH)
}

# Function to compare two file paths based on numeric value
function comparePaths(path1, path2) {
    return extractNumericValue(path1) - extractNumericValue(path2)
}

# Variable to store paragraphs and their content
{
    if (NF > 1) {
        currentPath = $0
        content = ""
    } else {
        content = content $0 "\n"
        paragraphs[currentPath] = content
    }
}

END {
    # Sorting and printing paragraphs based on numeric order
    n = asorti(paragraphs, sortedPaths, "comparePaths")
    for (i = 1; i <= n; i++) {
        path = sortedPaths[i]
        print path
        print paragraphs[path]
    }
}

