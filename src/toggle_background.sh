#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
	if [[ -n $1 ]]; then
	    tmux set -g @base16-background "$1"
	elif [[ $(tmux show -gv @base16-background) == "light" ]]; then
	    tmux set -g @base16-background "dark"
	else
	    tmux set -g @base16-background "light"
	fi
	tmux source "$CURRENT_DIR/theme.conf"

}
main "$@"
