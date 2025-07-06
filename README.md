# 🎨 tmux-base16

A minimal and clean [Base16](https://github.com/chriskempson/base16) colorscheme for tmux.

![showcase](https://github.com/user-attachments/assets/18deae4b-9ba2-4c03-83de-cc31b65e7cf0)

<details>
<summary>Information</summary>
<br>

- font: [Rec Mono Duotone](https://www.recursive.design)
- tmux: [tmux-base16](https://github.com/loichyan/tmux-base16)
- Neovim: [Meowim](https://github.com/loichyan/Meowim)

</details>

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

Reload tmux environment with `tmux source-file ~/.tmux.conf`. You should now be able to use the
plugin.

## ⚙️ Options

### `@base16-palette-dark`

**Default**: `#{@base16-palettes}/gruvbox-dark.conf`

**Description**: Path to the base16 palette for dark backgrounds.

This option is expanded as a FORMAT before it takes effect. Therefore, you can use palettes under
`@base16-palettes`, which is set to the [palettes directory](palettes) included in this plugin.

### `@base16-palette-light`

**Default**: `#{@base16-palette-light}/gruvbox-light.conf`

**Description**: Path to the base16 palette for light backgrounds.

### `@base16-background`

**Default**: `dark`

**Description**: Which background to use, `dark` or `light`.

### `@base16-border-lines`

**Default**: `rouned`

**Description**: Default border lines for popup windows and menus.

### `@base16-transparent`

**Default**: `off`

**Description**: Whether to remove backgrounds for most UI elements.

### `@base16-statusline`

**Default**: `on`

**Description**: Whether to configure tmux's statusline.

## ⌨️ Commands

Commands are shell scripts exported by this plugin, which you can bind keys to. The basic usage is
`tmux bind-key run-shell '#{@command_name} ...args'`.

### `@base16-toggle-background`

**Description**: Toggles the current background between `light` and `dark`. You may specify the
desired background as its optional argument.

## 🔤 Variables

This plugin also sets several variables that can be used in FORMATs.

### `@baseXX`

From `@base00` to `@base0F` are sixteen palette variables loaded from the provided palette file.

### `@base16_{fg,bg}`

`@base16_fg` and `@base16_bg` represent the default foreground and background colors, respectively,
depending on your configurations.

## 🎯 Goals

This plugin aims to provide a minimal theme that overrides tmux's default colors, so third-party
integrations won't be included. Additionally, it comes with a opinionated statusline, but if it
doesn’t suit your taste, you can create your own using the exported theme variables.

## ⚖️ License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  <http://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <http://opensource.org/licenses/MIT>)

at your option.
