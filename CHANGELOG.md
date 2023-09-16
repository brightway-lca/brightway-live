# `brightway-live` (based on `pyodide`) Changelog

This changelog follows the guidelines porposed by the ['keep a changelog'](https://keepachangelog.com/en/1.1.0/) project.

## v0.1.0-beta (2023-09-16)

### branch `pyodide`

Initial release of `brightway-live` (based on `pyodide`). \
Based on `jupyterlite-pyodide-kernel==0.1.2` (running `pyodide==0.24.0`).

#### Added

Packages `lxml` and `peewee` are now included in the Pyodide package list. Try `import lxml` or `import peewee`:

 -  https://github.com/brightway-lca/brightway-live/issues/8 by @michaelweinold
 -  https://github.com/brightway-lca/brightway-live/issues/9 by @michaelweinold (already in [Pyodide package list](https://pyodide.org/en/stable/usage/packages-in-pyodide.html))

#### Changed

 - https://github.com/brightway-lca/brightway-live/issues/33

#### Deprecated

N/A

#### Removed

N/A

#### Fixed

- https://github.com/brightway-lca/brightway-live/issues/30 by @michaelweinold
- https://github.com/brightway-lca/brightway-live/issues/29 by @cmutel
- https://github.com/brightway-lca/brightway-live/issues/22 by @michaelweinold (was added in [Pyodide version 0.24.0](https://github.com/pyodide/pyodide/releases))

#### Security

N/A

### branch `emscripten-forge`

#### Added

#### Changed

The GitHub Actions workflow was updated to use the latest versions of actions:

 - https://github.com/brightway-lca/brightway-live/issues/33