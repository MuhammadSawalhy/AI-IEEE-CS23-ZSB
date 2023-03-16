#!/bin/bash
pandoc \
  -f markdown+implicit_figures \
  --number-sections \
  --highlight-style=tango \
  -V colorlinks=true \
  -V author="Muhammad Samir Assawalhy" \
  -V date="\today" \
  "$1" -o "$2"

