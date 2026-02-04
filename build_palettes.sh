#!/usr/bin/env bash

find palettes -name '*.ini' | while read -r path; do
	dirname=$(dirname "$path")
	basename=$(basename "$path")
	name=${basename%.*}
	./src/build_palette.py -c "$path" -i templates/tmux.conf -o "$dirname/$name.conf"
done
