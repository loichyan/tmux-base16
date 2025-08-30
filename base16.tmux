#!/usr/bin/env bash

# Name:     tmux-base16
# Version:  0.1.0
# Authors:  Loi Chyan <loichyan@foxmail.com>
# License:  MIT OR Apache-2.0

set -e
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
	tmux \
		set -g "@base16-toggle-background" "$CURRENT_DIR/src/toggle_background.sh" \; \
		set -g "@base16-build-palette" "$CURRENT_DIR/src/build_palette.py" \; \
		set -g @base16-palettes "$CURRENT_DIR/palettes" \; \
		source "$CURRENT_DIR/src/theme.conf"
}
main
