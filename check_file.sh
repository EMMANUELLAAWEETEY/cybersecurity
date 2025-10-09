#!/bin/bash

# Check if filename is provided
if [ -z "$1" ]; then
  echo "Usage: $0 filename"
  exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
  echo "File '$1' not found!"
  exit 1
fi

# Get counts using wc
lines=$(wc -l < "$1")
words=$(wc -w < "$1")
chars=$(wc -m < "$1")

# Output results
echo "file: $1"
echo "Lines: $lines"
echo "Words: $words"
echo "Characters: $chars"


