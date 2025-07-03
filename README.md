# 🎨 tmux-base16

A minimal and clean [Base16](https://github.com/chriskempson/base16) colorscheme for tmux.

## 📦 Installation

### Requirements

- tmux >= **3.4** (not tested on earlier versions)

### With [tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)

Add this plugin to the list of TPM plugins in `.tmux.conf`:

```tmux
set -g @plugin "loichyan/tmux-base16"
```

### Manual installation

Clone the repo:

```sh
git clone https://github.com/loichyan/tmux-base16 ~/clone/path
```

Add this line to the bottom of `.tmux.conf`:

```tmux
run ~/clone/path/base16.tmux
```

Reload tmux environment with: `tmux source-file ~/.tmux.conf`. You should now
be able to use the plugin.

## ⚖️ License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <http://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <http://opensource.org/licenses/MIT>)

at your option.
