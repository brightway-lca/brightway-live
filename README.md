# Brightway JupyterLite Hub (powered by [WebAssembly](https://webassembly.org/))

[![Brightway](https://img.shields.io/static/v1?label=Brightway&message=ecosystem&color=45bfb0&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA2NSIgaGVpZ2h0PSI2OTAiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEwNjUgNjkwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGRlZnM+CiAgPGNsaXBQYXRoIGlkPSJjbGlwUGF0aDIxNzMiPgogICA8cGF0aCBkPSJtLTU5NSA0NDBoMWUzdi0xZTNoLTFlM3oiLz4KICA8L2NsaXBQYXRoPgogPC9kZWZzPgogPGcgdHJhbnNmb3JtPSJtYXRyaXgoMS4zIDAgMCAtMS4zIDY1MyA0MDMpIiBjbGlwLXBhdGg9InVybCgjY2xpcFBhdGgyMTczKSIgZmlsbD0iI2ZmZiI+CiAgPHBhdGggZD0ibTAgMGMwLTEuMi0xLjUtMy40LTAuNDctNS4yIDEuMy0yLjQgNS40LTEuNSA1LjgtM3YtMC4wMThsLTQuNy0wLjA1NC0yLTQuMWMtMS45IDAuNzEtMi40IDMuMi0zLjIgNi42LTAuNDQgMi0wLjcxIDMuNCAwLjA4OSA0LjctMTQtMy4zLTMwLTUuNC00NS01LjQtNDkgMC4wMzYtNzEgMTctMTA3IDI0IDEuNS0xLjEgMi43LTMuMyAyLjEtNC45bC02LjEgMi4yLTQtMy4xYy0xLjQgMS40LTAuNTggMi44LTIuMiA0LjgtMi4xIDIuNS01LjMgMi42LTUuMiAzIDAuODctMC4wNzIgMS43LTAuMTQgMi42LTAuMjItMS42IDAuMjQtMi41IDAuNC0yLjYgMC4yMi0zLjkgMC4zMS04IDAuNDktMTIgMC41MS02NiAwLjIyLTEwMi00Mi0xMjItNzkgMy42IDIuOSA4LjcgMS41IDEwIDEuMSA0LjItMS4xIDguOC00LjEgOC40LTYuMWwtNC41LTEuNSAwLjUyLTAuNTRjLTAuMjItMC4wMTktMC40My0wLjAxOS0wLjY1LTAuMDE5LTQuMiAwLjA1NS01LjEgMy45LTkuMiA0LjItMy44IDAuMjktNi40LTIuNy03LjItMS45LTEzLTI3LTE4LTUwLTE4LTUwaC0zNHM2LjcgMzQgMzAgNjhjLTEuNiAxIDEgNS0xLjEgOC4zLTIuNSAzLjgtOC40IDIuNC04LjggNC41LTAuMDE4IDAuMTMtMC4wMzYgMC4yNSAwIDAuMzhsNy4yLTAuNTIgMi41IDUuNWMxLjEtMC40IDItMS43IDMuOS00LjIgMS40LTEuOCAyLjQtMy4yIDMuMS00LjMgMjYgMzQgNjkgNjcgMTM5IDY3IDIuNSAwIDUtMC4wNzMgNy40LTAuMi0wLjU4IDIuMSA1IDMuNSA1LjcgOC4xIDAuNzQgNC44LTQuNyA3LjgtMy40IDEwIDAuMDE4IDAuMDE4IDAuMDM2IDAuMDU0IDAuMDU0IDAuMDcybDUuOC00LjQgNC43IDMuMWMwLjU2LTAuODcgMC42My0xLjctMC40NS04LTEuNC04LjItMS45LTktMi43LTkuNyA0MS01LjIgNjgtMjggMTE4LTI5IDE1LTAuNTQgMzAgMC43OCA0NCAzLjEtMC4yNyAwLjE2LTAuNTIgMC4zNi0wLjc2IDAuNjItMSAxLjEtMS4xIDMuMS0xLjQgNy4xLTAuMjUgNC4zLTAuNCA2LjYgMC40MiA3LjdsMi44LTMuMiAzLjIgMS4yYzAuMDM2LTAuMDcyIDAuMDU0LTAuMTYgMC4wNzItMC4yNCAwLjQ0LTEuOC0xLjEtMi43LTEuMS01LjYgMC0zLjUgMi4zLTQuOSAxLjgtNi41LTAuMDM2LTAuMDktMC4wNzItMC4xOC0wLjExLTAuMjUgNDUgOC43IDc4IDI4IDc5IDI4IDAtMC42My0zNS0yMi03OS0zM20tMzMyLTMwLTU1IDQuMS0zNSA0MC0xNyAyOC0xNSAyNC05LjcgMjctMjYgMTYgMzgtOS40IDM5LTI0IDMxLTI4IDI3LTM5IDE5LTMzem00MTEgNjUgMTEgNzkgNTcgNDYgNjggOS4zIDQ1LTAuMzkgNDcgMTYtMTYtMzYtMTMtMzQtMjQtNTgtMzItNDktMzktMjAtNDMgMy43em04OC0yNDktMTggMzItMjEgMjYtMzUgMzQtMjEgMjYtMjAgMjItMzcgNDgtMTcgMjAgNzAgMC44NyA1Ni00OSAyMi00MCAxNS0zNyAyLjgtMzJ6bTAgMC0xNyAxNy0zOSA2LjItNDQgMTMtNTAgMzMtMzAgNTUtMy4zIDUzIDEzIDI3IDEuOSAzLjcgMTctMjAgMzctNDggMjAtMjIgMjEtMjYgMzUtMzQgMjEtMjZ6bS05MSAzNDgtMTYtNTctMzEtNDYtMzMtMTIgMC4xNSAzLjkgMS42IDQ0IDQuNCAzNiA1LjEgMzQgNC4zIDQwIDIgMzQgMi4zIDM2IDEzIDQyIDQuNS0zNyAxNi0yMiAyMC0zN3ptLTQ3IDE1NC0xMy00Mi0yLjMtMzYtMi0zNC00LjMtNDAtNS4xLTM0LTQuNC0zNi0xLjYtNDQtMC4xNS0zLjktMi44IDMuMi00OCA1NS03LjIgMzcgMC43OCA2NCAyNiA0OCAzMyAyOXptLTE0NS0zOTktMjAgNDMtMTIgNDEtNi4xIDI0LTYuNyAyMCA1OC0yMSAxNS0yNiAxNi00NC00LjItMzctMTItNjEtNS4yIDI0em0yOC02MS0yNyAxOS0yMCAxMS0yOCAyMC0zMSAzMC02LjggNDggMTcgNDIgMjQgMTggMS41LTQuNiA1LjItMTYgNi4xLTI0IDEyLTQxIDIwLTQzIDIyLTM3em0tMTEgMzA1LTE4LTUxLTUyLTM0LTAuMjUgNS44LTAuODMgMTkgMS4yIDM5LTMuMSA0My02LjcgMzgtMTEgNDYtMTUgNjMgMjAtMjUgNDMtNDEgMzAtNDl6bS03MC03OSAwLjI1LTUuOC01NiA0Mi0xNyA2NSAyLjcgNTAgOS40IDQwIDE2IDE3IDguNCA0MCAxNS02MyAxMS00NiA2LjctMzggMy4xLTQzLTEuMi0zOXptLTU0LTE5NC0xMiAyMC0yMiAyNi0xOCAxNS0xNyAxNy0wLjEzLTAuNTYtOS43LTQ1IDIxLTM0IDIzLTEzIDIxLTguMiAzNy0xOS0xNSAxM3ptMjQtNDEtMTUgMTMtOC4zIDI4LTEyIDIwLTIyIDI2LTE4IDE1LTE3IDE3IDQyIDE0IDI0LTQuOCAxNS0xNiA4LjYtMzMgMS41LTI4LTMuNC0yMHptLTExMCAyMDItMjMtNTEtMi44IDQuOS0xOSAzMy0yNyAzOS0zMSAyOC0zOSAyNC0zOCA5LjQgMzIgMS4zIDMxIDEuNiAzMC0wLjI5IDQzLTE2IDMwLTMweiIvPgogPC9nPgo8L3N2Zz4K)](https://github.com/brightway-lca)
![License](https://img.shields.io/github/license/brightway-lca/brightway-learn?color=green&logo=Open%20Source%20Initiative&logoColor=white)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&logo=GitHub)](https://github.com/brightway-lca/brightway-documentation-readthedocs/discussions) \
[Pilot-in-Command](https://en.wikipedia.org/wiki/Pilot_in_command): [@michaelweinold](https://github.com/michaelweinold)

The development playground for the Brightway life-cycle assessment software package. [GitHub Actions](https://github.com/features/actions) and [Github Pages](https://pages.github.com/) with the [JupyterLite](https://github.com/jupyterlite/jupyterlite) are used to build/host this site.

| static documentation | interactive documentation | development playground |
| ---- | ------------- | ------------- |
| [docs.brightway.dev](https://github.com/brightway-lca/brightway-documentation) | (coming soon!) | [live.brightway.dev](https://github.com/brightway-lca/brightway-hub) | 


> [!IMPORTANT]
> A version of the hub based instead on the `xeus-python-kernel` is available in the `emscripten-forge` branch of this repo. 

> [!IMPORTANT]
> A version of the hub based instead on the `pyodide` Jupyterlite kernel is available in the `pyodide` branch of this repo.

## Building the Documentation

### Setup Python Environment

Set up a Python virtual environment that includes all packages required to build the documentation. A [Conda environment file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). The file is located at [``./environment.yml``](environment.yml). Install the environment `sphinx` by running from the repository root directory:

```bash
conda env create -f 'docs/environment.yaml'
```

and activate the environment:

```bash
conda activate sphinx
```

You are now ready to build the documentation...

### Building the Documentation

1. You can build the documentation by __triggering every build manually__: To trigger the build, run [`sphinx-build`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) from the repository root directory:

```bash
sphinx-build docs _build/html -b singlehtml -a
```

| option | value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `docs` | N/A |
| outdir | `_build/html` | N/A |
| -b | `singlehtml` | create only a single html page |
| -a | N/A | always write all output files |
| `-j` | `auto` | [speed up build by using multiple processes](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-j) |


You can now preview the documentation, built as a single html page at:

```
_build/html/homepage.html
```

2. You can also build the documentation by automatically triggering a build after every change to the source files, providing a "live" preview of changes. To trigger the automated builds, run [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild) from the repository root directory:

```bash
sphinx-autobuild docs _build/html -a -j auto --open-browser
```

| positional argument or option| value | description |
| ---------------------------- | ----- | ----------- |
| sourcedir | `docs` | N/A |
| outdir | `_build/html` | N/A |
| `-a` | N/A | always write all output files |
| `-j` | `auto` | [speed up build by using multiple processes](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-j) |
| `--open-browser` | N/A | automatically open browser |


You can now preview the documentation at (the browser window will open automatically ✨):
http://127.0.0.1:8000/

## 📚 References

Compare the `jupyterlite`:

- [How-to Guides](https://jupyterlite.readthedocs.io/en/latest/howto/index.html)
- [Reference](https://jupyterlite.readthedocs.io/en/latest/reference/index.html)
