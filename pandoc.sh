#!/bin/bash
pandoc \
  -f markdown \
  --number-sections \
  --highlight-style=tango \
  -V colorlinks=true \
  "$1" -o "$2"

