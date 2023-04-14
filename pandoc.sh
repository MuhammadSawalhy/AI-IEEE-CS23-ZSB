#!/bin/bash
pandoc \
  -f markdown+implicit_figures \
  --number-sections \
  --highlight-style=tango \
  -V colorlinks=true \
  --metadata title="$3" \
  --metadata author="Muhammad Samir Assawalhy" \
  --metadata date="$(date +%Y-%m-%d)" \
  "$1" -o "$2"

