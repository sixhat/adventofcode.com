#!/usr/bin/env bash

set -e
ano=$(date +%Y)
echo "Advent of Code $ano"
dia=$(date +%d)
url="https://adventofcode.com/$ano/"

#mkdir -p "$ano"
#mkdir -p "$ano/$dia"
#touch "$ano/$dia/input"
#touch "$ano/$dia/demo"
#touch "$ano/$dia/day$dia.pl"
#code "$ano"

open "$url"

