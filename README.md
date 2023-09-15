# Brightway JupyterLite Hub (powered by [WebAssembly](https://webassembly.org/))

[![Brightway](https://img.shields.io/static/v1?label=Brightway&message=ecosystem&color=45bfb0&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA2NSIgaGVpZ2h0PSI2OTAiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEwNjUgNjkwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGRlZnM+CiAgPGNsaXBQYXRoIGlkPSJjbGlwUGF0aDIxNzMiPgogICA8cGF0aCBkPSJtLTU5NSA0NDBoMWUzdi0xZTNoLTFlM3oiLz4KICA8L2NsaXBQYXRoPgogPC9kZWZzPgogPGcgdHJhbnNmb3JtPSJtYXRyaXgoMS4zIDAgMCAtMS4zIDY1MyA0MDMpIiBjbGlwLXBhdGg9InVybCgjY2xpcFBhdGgyMTczKSIgZmlsbD0iI2ZmZiI+CiAgPHBhdGggZD0ibTAgMGMwLTEuMi0xLjUtMy40LTAuNDctNS4yIDEuMy0yLjQgNS40LTEuNSA1LjgtM3YtMC4wMThsLTQuNy0wLjA1NC0yLTQuMWMtMS45IDAuNzEtMi40IDMuMi0zLjIgNi42LTAuNDQgMi0wLjcxIDMuNCAwLjA4OSA0LjctMTQtMy4zLTMwLTUuNC00NS01LjQtNDkgMC4wMzYtNzEgMTctMTA3IDI0IDEuNS0xLjEgMi43LTMuMyAyLjEtNC45bC02LjEgMi4yLTQtMy4xYy0xLjQgMS40LTAuNTggMi44LTIuMiA0LjgtMi4xIDIuNS01LjMgMi42LTUuMiAzIDAuODctMC4wNzIgMS43LTAuMTQgMi42LTAuMjItMS42IDAuMjQtMi41IDAuNC0yLjYgMC4yMi0zLjkgMC4zMS04IDAuNDktMTIgMC41MS02NiAwLjIyLTEwMi00Mi0xMjItNzkgMy42IDIuOSA4LjcgMS41IDEwIDEuMSA0LjItMS4xIDguOC00LjEgOC40LTYuMWwtNC41LTEuNSAwLjUyLTAuNTRjLTAuMjItMC4wMTktMC40My0wLjAxOS0wLjY1LTAuMDE5LTQuMiAwLjA1NS01LjEgMy45LTkuMiA0LjItMy44IDAuMjktNi40LTIuNy03LjItMS45LTEzLTI3LTE4LTUwLTE4LTUwaC0zNHM2LjcgMzQgMzAgNjhjLTEuNiAxIDEgNS0xLjEgOC4zLTIuNSAzLjgtOC40IDIuNC04LjggNC41LTAuMDE4IDAuMTMtMC4wMzYgMC4yNSAwIDAuMzhsNy4yLTAuNTIgMi41IDUuNWMxLjEtMC40IDItMS43IDMuOS00LjIgMS40LTEuOCAyLjQtMy4yIDMuMS00LjMgMjYgMzQgNjkgNjcgMTM5IDY3IDIuNSAwIDUtMC4wNzMgNy40LTAuMi0wLjU4IDIuMSA1IDMuNSA1LjcgOC4xIDAuNzQgNC44LTQuNyA3LjgtMy40IDEwIDAuMDE4IDAuMDE4IDAuMDM2IDAuMDU0IDAuMDU0IDAuMDcybDUuOC00LjQgNC43IDMuMWMwLjU2LTAuODcgMC42My0xLjctMC40NS04LTEuNC04LjItMS45LTktMi43LTkuNyA0MS01LjIgNjgtMjggMTE4LTI5IDE1LTAuNTQgMzAgMC43OCA0NCAzLjEtMC4yNyAwLjE2LTAuNTIgMC4zNi0wLjc2IDAuNjItMSAxLjEtMS4xIDMuMS0xLjQgNy4xLTAuMjUgNC4zLTAuNCA2LjYgMC40MiA3LjdsMi44LTMuMiAzLjIgMS4yYzAuMDM2LTAuMDcyIDAuMDU0LTAuMTYgMC4wNzItMC4yNCAwLjQ0LTEuOC0xLjEtMi43LTEuMS01LjYgMC0zLjUgMi4zLTQuOSAxLjgtNi41LTAuMDM2LTAuMDktMC4wNzItMC4xOC0wLjExLTAuMjUgNDUgOC43IDc4IDI4IDc5IDI4IDAtMC42My0zNS0yMi03OS0zM20tMzMyLTMwLTU1IDQuMS0zNSA0MC0xNyAyOC0xNSAyNC05LjcgMjctMjYgMTYgMzgtOS40IDM5LTI0IDMxLTI4IDI3LTM5IDE5LTMzem00MTEgNjUgMTEgNzkgNTcgNDYgNjggOS4zIDQ1LTAuMzkgNDcgMTYtMTYtMzYtMTMtMzQtMjQtNTgtMzItNDktMzktMjAtNDMgMy43em04OC0yNDktMTggMzItMjEgMjYtMzUgMzQtMjEgMjYtMjAgMjItMzcgNDgtMTcgMjAgNzAgMC44NyA1Ni00OSAyMi00MCAxNS0zNyAyLjgtMzJ6bTAgMC0xNyAxNy0zOSA2LjItNDQgMTMtNTAgMzMtMzAgNTUtMy4zIDUzIDEzIDI3IDEuOSAzLjcgMTctMjAgMzctNDggMjAtMjIgMjEtMjYgMzUtMzQgMjEtMjZ6bS05MSAzNDgtMTYtNTctMzEtNDYtMzMtMTIgMC4xNSAzLjkgMS42IDQ0IDQuNCAzNiA1LjEgMzQgNC4zIDQwIDIgMzQgMi4zIDM2IDEzIDQyIDQuNS0zNyAxNi0yMiAyMC0zN3ptLTQ3IDE1NC0xMy00Mi0yLjMtMzYtMi0zNC00LjMtNDAtNS4xLTM0LTQuNC0zNi0xLjYtNDQtMC4xNS0zLjktMi44IDMuMi00OCA1NS03LjIgMzcgMC43OCA2NCAyNiA0OCAzMyAyOXptLTE0NS0zOTktMjAgNDMtMTIgNDEtNi4xIDI0LTYuNyAyMCA1OC0yMSAxNS0yNiAxNi00NC00LjItMzctMTItNjEtNS4yIDI0em0yOC02MS0yNyAxOS0yMCAxMS0yOCAyMC0zMSAzMC02LjggNDggMTcgNDIgMjQgMTggMS41LTQuNiA1LjItMTYgNi4xLTI0IDEyLTQxIDIwLTQzIDIyLTM3em0tMTEgMzA1LTE4LTUxLTUyLTM0LTAuMjUgNS44LTAuODMgMTkgMS4yIDM5LTMuMSA0My02LjcgMzgtMTEgNDYtMTUgNjMgMjAtMjUgNDMtNDEgMzAtNDl6bS03MC03OSAwLjI1LTUuOC01NiA0Mi0xNyA2NSAyLjcgNTAgOS40IDQwIDE2IDE3IDguNCA0MCAxNS02MyAxMS00NiA2LjctMzggMy4xLTQzLTEuMi0zOXptLTU0LTE5NC0xMiAyMC0yMiAyNi0xOCAxNS0xNyAxNy0wLjEzLTAuNTYtOS43LTQ1IDIxLTM0IDIzLTEzIDIxLTguMiAzNy0xOS0xNSAxM3ptMjQtNDEtMTUgMTMtOC4zIDI4LTEyIDIwLTIyIDI2LTE4IDE1LTE3IDE3IDQyIDE0IDI0LTQuOCAxNS0xNiA4LjYtMzMgMS41LTI4LTMuNC0yMHptLTExMCAyMDItMjMtNTEtMi44IDQuOS0xOSAzMy0yNyAzOS0zMSAyOC0zOSAyNC0zOCA5LjQgMzIgMS4zIDMxIDEuNiAzMC0wLjI5IDQzLTE2IDMwLTMweiIvPgogPC9nPgo8L3N2Zz4K)](https://github.com/brightway-lca)
![License](https://img.shields.io/github/license/brightway-lca/brightway-learn?color=green&logo=Open%20Source%20Initiative&logoColor=white)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&logo=GitHub)](https://github.com/brightway-lca/brightway-documentation-readthedocs/discussions) \
[Pilot-in-Command](https://en.wikipedia.org/wiki/Pilot_in_command): [@michaelweinold](https://github.com/michaelweinold)

The interactive learning and teaching documentation for the Brightway life-cycle assessment software package. [GitHub Actions](https://github.com/features/actions) and [Github Pages](https://pages.github.com/) with the [Jupyter Book Theme](https://jupyterbook.org/en/stable/intro.html) and the [Thebe tool](https://thebe.readthedocs.io/en/stable/) used to build/host the interactive documentation.

| static documentation | interactive documentation | development playground |
| ---- | ------------- | ------------- |
| [docs.brightway.dev](https://github.com/brightway-lca/brightway-documentation) | (coming soon!) | [live.brightway.dev](https://github.com/brightway-lca/brightway-live) | 

This repo is based on the [`xeus-python-demo`](https://github.com/jupyterlite/xeus-python-demo) template. For testing purposes, [the JupyterLite Hub of this template](https://jupyterlite.github.io/xeus-python-demo/lab/index.html) can be used.

> [!IMPORTANT]
> A version of the hub based instead on the `pyodide` Jupyterlite kernel is available in the `pyodide` branch of this repo. 

<img width="525" alt="Screenshot 2023-09-15 at 09 50 53" src="https://github.com/brightway-lca/brightway-hub/assets/23102087/f2fa252b-bc73-4577-9f63-77e2526fc8cd">

## Quickstart
### Setup Repository

1. Clone this repository:

```bash
git clone https://github.com/brightway-lca/brightway-hub.git
```

### Setup Python Environment

> [!NOTE]
> To add content (Jupyter Notebooks, Python files, etc.) to the site, no further setup is required. However, if you want to build the site locally, you need to set up a Python environment.

Set up a Python virtual environment that allows you to build the JupyterLite hub locally. A [Conda environment file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). The file is located at [``./build-environment.yml``](./build-environment.yml). Install the environment `build-env` by running from the repository root directory:

```bash
conda env create -f 'build-environment.yml'
```

### Adding Content to the JupiterLite Environment

Jupyter Notebook, Python files, etc. can be added to the JupyterLite environment by adding them to the `content` directory.
### Building the JupyterLite Environment

You can build the site by pushing to the `main` branch. The GitHub Actions workflow [`deploy.yml`](.github/workflows/deploy.yml) will build the site and publish it.

> [!IMPORTANT]
> If a package is published to a [_channel_](https://docs.anaconda.com/reference/glossary/#channels) under a [_label_](https://docs.anaconda.com/reference/glossary/#label) other than `main`, the channel+label of the package must be specified for the installation to work as expected.
> The `Build and Deploy` workflow of [`jupyterlite/xeus-python`](https://github.com/jupyterlite/xeus-python-demo) does not currently support channel names as part of the package specs in the environment file `environment.yml`. This means that channel+label of relevant packages  must be defined in the `channels:` section of the `environment.yml` file. For example, the package `bw2calc` is installed from the `conda-forge` channel with the label `bw2calc_dev`:
> ```
> name: xeus-python-kernel
> channels:
>  - https://conda.anaconda.org/conda-forge/label/bw2calc_dev
>  - https://repo.mamba.pm/emscripten-forge
>  - https://conda.anaconda.org/conda-forge
>  - nodefaults
> dependencies:
> - bw2calc=2.0.dev14
> ```

> [!NOTE]
> `conda install` supports channel names as part of the package specs in the environment file. \
> [Use this syntax](https://github.com/conda/conda/issues/988#issuecomment-436454507):
> ```
> - https://conda.anaconda.org/conda-forge/label/bw2calc_dev::bw2calc=2.0.dev14
> - conda-forge::numpy
> ```

> [!NOTE]
> `conda build` does not (yet) support channel names as part of the package specs in the environment file. \
> (cf. https://github.com/conda/conda-build/issues/532).

### Using the JypterLite Environment

#### Reset the JupyterLite Environment

Currently, the interface of the JupiterLite environment does not provide a way to reset the environment.

##### Related Issues:

 - [ ] https://github.com/jupyterlite/jupyterlite/issues/9

This means that the environment must be reset manually. [Usually](https://jupyterlite.readthedocs.io/en/latest/howto/configure/storage.html), all data is stored in the browser's `IndexedDB`. You can reset the environment in your browser by following these steps:

- [Google Chrome](https://github.com/jupyterlite/jupyterlite/issues/9#issuecomment-875870620): 

> Developer > Developer Tools > Application > Storage > Indexed DB > JupyterLite Storage > Delete Database

- Mozilla Firefox:

> Tools > Page Info > Permissions > Maintain Offline Storage > Clear Storage
