# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
Here's a template for each release section. This file should only include updates
that are noticeable to end users between two releases. For developers, this project
follows <https://www.conventionalcommits.org/en/v1.0.0/> to track changes.

## [1.0.0] - YYYY-MM-DD

### Added

- (**breaking**) Always place breaking changes at the top of each subsection.
- Append other changes in chronological order under the appropriate subsection.
- Additionally, you may use `{{variable name}}` as a placeholder for the value
  of a named variable, which includes:
  - `PRNUM`: the number of the pull request
  - `DATE`: the date in `YYYY-MM-DD` format whenever the pull request is updated

### Changed

### Deprecated

### Removed

### Fixed

### Security

[1.0.0]: https://github.com/user/repo/compare/v0.0.0..v1.0.0
-->

## [Unreleased]

### Added

- Support overriding the content of the right side of the statusline ([#3])
- Show colored pane borders when in copy mode ([b1477fc])
- Improve the color of selection area ([2eb2c5a])

### Changed

- (**breaking**) Expand customized section content as tmux FORMATS ([#2])
- (**breaking**) Minimize the entire statusline ([#4])
- (**breaking**) Switch the default palette back to gruvbox-material ([6daad03])
- Use a thinner mode indicator, from `█` to `┃` ([0fcaf01])
- Use classic yellow copy mode indicator ([b8fd414])

### Fixed

- Suppress errors about unknown options ([c9ca977])

[#2]: https://github.com/loichyan/tmux-base16/pull/2
[#3]: https://github.com/loichyan/tmux-base16/pull/3
[#4]: https://github.com/loichyan/tmux-base16/pull/4
[0fcaf01]: https://github.com/loichyan/tmux-base16/commit/0fcaf01b00131787bbf27411471c4dcb8fbdef0a
[b1477fc]: https://github.com/loichyan/tmux-base16/commit/b1477fcffc1542b575123176cb77b4a2349193e7
[2eb2c5a]: https://github.com/loichyan/tmux-base16/commit/2eb2c5a5688b7e2cc18bb3139b163012bd260587
[c9ca977]: https://github.com/loichyan/tmux-base16/commit/c9ca977158c26bb5fa265b7dd1424179f462d437
[6daad03]: https://github.com/loichyan/tmux-base16/commit/6daad03c735539fb100108717e523559574a7c47
[b8fd414]: https://github.com/loichyan/tmux-base16/commit/b8fd41403fb64d81b1f77a86954774e9faa2ff96

## [0.1.0] - 2025-08-30

🎉 Initial release. See
[README](https://github.com/loichyan/tmux-base16/blob/v0.1.0/README.md) for more
details.

[0.1.0]: https://github.com/loichyan/tmux-base16/tree/v0.1.0
[Unreleased]: https://github.com/loichyan/tmux-base16/compare/v0.1.0..HEAD
