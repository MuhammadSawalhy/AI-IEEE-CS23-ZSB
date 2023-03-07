#!/bin/bash
pandoc -f markdown --highlight-style=tango --number-sections -V colorlinks=true "$1" -o "$2"

