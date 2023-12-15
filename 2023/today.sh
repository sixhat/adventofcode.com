#!/bin/sh
set -ex

today=$(date -u +%d)
mkdir -p "$today"
cp -r template/* "$today"
mv "$today/template.py" "$today/$today.py"

open "https://adventofcode.com/2023/day/$today"
code .