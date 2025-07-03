#!/usr/bin/env bash

# Name:     tmux-toggle-popup
# Version:  0.1.0
# Authors:  Loi Chyan <loichyan@foxmail.com>
# License:  MIT OR Apache-2.0

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export_commands() {
    tmux set -g "@base16-toggle-background" "$CURRENT_DIR/src/toggle_background.sh"
}

set_defaults() {
    tmux \
        set -g @base16-palettes "$CURRENT_DIR/palettes" \; \
        set -goq @base16-palette-dark "$CURRENT_DIR/palettes/gruvbox-dark.conf" \; \
        set -goq @base16-palette-light "$CURRENT_DIR/palettes/gruvbox-light.conf" \; \
        set -goq @base16-background dark \; \
        set -goq @base16-border-lines rounded \; \
        set -goq @base16-transparent off \; \
        set -goq @base16-statusline on
}

main() {
    set_defaults
    export_commands
    tmux source "$CURRENT_DIR/src/theme.conf"
}
main
