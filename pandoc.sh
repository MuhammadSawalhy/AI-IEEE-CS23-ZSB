#!/bin/bash
pandoc \
  -f markdown+implicit_figures \
  --number-sections \
  --highlight-style=tango \
  -V colorlinks=true \
  --metadata author="Muhammad Samir Assawalhy" \
  --metadata date="\today" \
  "$1" -o "$2"

