#!/usr/bin/env bash

while read -r fullname; do
	dirname=$(dirname "$fullname")
	filename=$(basename "$fullname")
	name=${filename%.*}
	./src/build_palette.py -i "$fullname" -o "$dirname/$name.conf"
done < <(find palettes -name '*.ini')
