# 🎨 tmux-base16

A minimal and clean [Base16](https://github.com/chriskempson/base16) colorscheme
for tmux.

![showcase](https://loichyan.github.io/dotfiles/assets/tmux-base16.jpg)
[Information](https://github.com/loichyan/dotfiles/tree/snapshot#information)

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

Reload tmux environment with `tmux source-file ~/.tmux.conf`. You should now be
able to use the plugin.

## ⚙️ Options

### `@base16-palette-path`

**Default**: `#{@base16-palettes}/gruvbox-material.conf`

**Description**: Path to the base16 palette.

This option is expanded as a FORMAT before it takes effect. Therefore, you can
use palettes under `@base16-palettes`, which is set to the
[palettes directory](palettes) included in this plugin.

### `@base16-background`

**Default**: `dark`

**Description**: Which background to use, `dark` or `light`.

This option itself does not affect the appearance; instead, palette should be
responsible for it value.

### `@base16-border-lines`

**Default**: `rouned`

**Description**: Default border lines for popup windows and menus.

### `@base16-transparent`

**Default**: `off`

**Description**: Whether to remove backgrounds for most UI elements.

### `@base16-statusline`

**Default**: `on`

**Description**: Whether to configure tmux's statusline.

### `@base16-window-{content,current_content}`

**Default**: `##{window_name}##{window_flags}:##{pane_current_path}`

**Description**: Content displayed in window tabs when `@base16-statusline` is
enabled. The value is expanded as tmux FORMATS before taking effect.

### `@base16-status-right-content`

**Default**: `%a %H:%M`

**Description**: Content displayed in the right side of the statusline. The
value is expanded as tmux FORMATS before taking effect.

## ⌨️ Commands

A command is an executable shell script exported by this plugin, which you can
bind keys to.

### `@base16-toggle-background`

**Description**: Toggles the current background between `light` and `dark`. You
may explicitly specify the desired background as the only argument.

### `@base16-build-palette`

**Requirements**: Python >= **3.10**

**Description**: A useful script to build palette from templates. For the
structure of the configurations, see
[palettes/gruvbox-material.ini](palettes/gruvbox-material.ini).

## 🔤 Variables

This plugin also sets several variables that can be used in FORMATs.

### `@base16-palettes`

**Description**: Path to the [palettes directory](palettes) shipped with this
plugin.

### `@base16-templates`

**Description**: Path to the [templates directory](templates) shipped with this
plugin.

### `@baseXX`

From `@base00` to `@base0F` are sixteen palette variables loaded from the
provided palette file.

### `@base16_{fg,bg}`

`@base16_fg` and `@base16_bg` represent the default foreground and background
colors, respectively, depending on your configurations.

## 🎯 Goals

This plugin aims to provide a minimal theme that overrides tmux's default
colors, so third-party integrations won't be included. Additionally, it comes
with a opinionated statusline, but if it doesn’t suit your taste, you can create
your own using the exported theme variables.

## ⚖️ License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  <http://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or
  <http://opensource.org/licenses/MIT>)

at your option.
