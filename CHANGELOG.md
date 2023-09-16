# `brightway-live` (based on `pyodide`) Changelog

This changelog follows the guidelines proposed by the ['keep a changelog'](https://keepachangelog.com/en/1.1.0/) project. \
See also the [development meeting minutes](https://github.com/brightway-lca/brightway-live/discussions/21).

## v0.1.1-beta (2023-09-16)

### Branch `main`

Added Sphinx documentation files. The documentation is now available at https://docs.brightway.dev/projects/live/.

## v0.1.0-beta (2023-09-16)

### Not related to a specific Branch

#### Added

Deprecated packages and those with pure-Python alternatives were removed from the Brightway dependency list:

 - https://github.com/brightway-lca/brightway-hub/issues/7 by @cmutel and @michaelweinold

### Branch `pyodide`

Initial release of `brightway-live` (based on `pyodide`). \
Based on `jupyterlite-pyodide-kernel==0.1.2` (running `pyodide==0.24.0`).

#### Added

Packages `lxml` and `peewee` are now included in the Pyodide package list. Try `import lxml` or `import peewee`:

 -  https://github.com/brightway-lca/brightway-live/issues/8 by @michaelweinold
 -  https://github.com/brightway-lca/brightway-live/issues/9 by @michaelweinold (already in [Pyodide package list](https://pyodide.org/en/stable/usage/packages-in-pyodide.html))

#### Changed

The GitHub Actions workflow was updated to use the latest versions of actions:

 - https://github.com/brightway-lca/brightway-live/issues/33 by @michaelweinold

#### Fixed

- https://github.com/brightway-lca/brightway-live/issues/30 by @michaelweinold
- https://github.com/brightway-lca/brightway-live/issues/29 by @cmutel
- https://github.com/brightway-lca/brightway-live/issues/22 by @michaelweinold (was added in [Pyodide version 0.24.0](https://github.com/pyodide/pyodide/releases))

### Branch `emscripten-forge`

#### Added

Packages `lxml` and `peewee` are now included in the emscripten-forge repository. They can be used to build the site by specifying them in the `environment.yml` file. In JupyterLite, try `import lxml` or `import peewee`:

- https://github.com/brightway-lca/brightway-hub/issues/8 by @michaelweinold
- https://github.com/brightway-lca/brightway-hub/issues/9 by @michaelweinold

`dev` versions of Brightway packages (eg. `bw2io==0.9dev22`) were added to conda to facilitate the `emscripten-forge` build:

- https://github.com/brightway-lca/brightway-hub/issues/19 by @michaelweinold with help from @m-rossi

#### Changed

The GitHub Actions workflow was updated to use the latest versions of actions:

 - https://github.com/brightway-lca/brightway-live/issues/33 by @michaelweinold

#### Fixed

Various build issues were fixed:

- https://github.com/brightway-lca/brightway-hub/issues/3 by @michaelweinold
- https://github.com/brightway-lca/brightway-hub/issues/18 by @michaelweinold
- https://github.com/brightway-lca/brightway-hub/issues/23 by @michaelweinold and @cmutel
- https://github.com/brightway-lca/brightway-hub/issues/26 by @michaelweinold and @cmutel
- https://github.com/emscripten-forge/empack/issues/81 by @DerThorsten
