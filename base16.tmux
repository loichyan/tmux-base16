#!/usr/bin/env bash

# Name:     tmux-toggle-popup
# Version:  0.1.0
# Authors:  Loi Chyan <loichyan@foxmail.com>
# License:  MIT OR Apache-2.0

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export_commands() {
    tmux set -g "@base16-toggle-background" "$CURRENT_DIR/src/toggle_background.sh"
}

main() {
    set_defaults
    export_commands
    tmux set -g @base16-palettes "$CURRENT_DIR/palettes"
    tmux source "$CURRENT_DIR/src/theme.conf"
}
main
