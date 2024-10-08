---
title: 'Brightway Live: Complet Life-Cycle Assessment Calculations in the Browser'
tags:
  - Python
  - Brightway
  - sustainability
  - lca
  - life-cycle assessment
  - teaching
  - wasm
  - webassembly
authors:
  - name: Michael Philipp Weinold
    orcid: 0000-0003-4859-2650
    equal-contrib: false
    affiliation: 1, 2
  - name: Christopher Mutel
    orcid: 0000-0002-7898-9862
    equal-contrib: false
    affiliation: 2
affiliations:
 - name: Center for Energy and Environmental Sciences, Paul Scherrer Institute (PSI), Villigen, Switzerland
   index: 1
 - name: Department of Mechanical and Process Engineering, ETH Zurich, Zurich, Switzerland
   index: 2
 - name: Départ de Sentier (DdS), Riniken AG, Switzerland
   index: 3
date: 01 December 2024
bibliography: references.bib

---

# Summary

Life-cycle assessment has become a uibiquitous tool in decision making.
It is used in industry, policy and every day economic transactions.
The number of students required to learn it has grown rapidly over the past year.
While some well-established software packages exist, some are proprietary, limiting their use in a teaching environment.
The open source Brightway software framework is a popular choice for teaching, but requires installation on a local computer.
Experience has shown that the setup (local Python environment, matching versions, etc.) can take many man-hours.


Even with 

# Statement of need

`Brightway Live` is an implementation of the JupyterLite distribution
of the JupyterLab web-based interactive development environment.
It provides WASM support for the Brightway life-cycle assessment software framework `[Mutel_2017]`.
It works with other Brightway packages, such as `Temporalis` `[Cardellini_2018]`.

`Brightway Live` was designed to be used in a teaching environment. With increases in performance of Python in WASM...

`Gala` is an Astropy-affiliated Python package for galactic dynamics. Python
enables wrapping low-level languages (e.g., C) for speed without losing
flexibility or ease-of-use in the user-interface. The API for `Gala` was
designed to provide a class-based and user-friendly interface to fast (C or
Cython-optimized) implementations of common operations such as gravitational
potential and force evaluation, orbit integration, dynamical transformations,
and chaos indicators for nonlinear dynamics. `Gala` also relies heavily on and
interfaces well with the implementations of physical units and astronomical
coordinate systems in the `Astropy` package [@astropy] (`astropy.units` and
`astropy.coordinates`).

`Gala` was designed to be used by both astronomical researchers and by
students in courses on gravitational dynamics or astronomy. It has already been
used in a number of scientific publications [@Pearson:2017] and has also been
used in graduate courses on Galactic dynamics to, e.g., provide interactive
visualizations of textbook material [@Binney:2008]. The combination of speed,
design, and support for Astropy functionality in `Gala` will enable exciting
scientific explorations of forthcoming data releases from the *Gaia* mission
[@gaia] by students and experts alike.

# Figures

TODO:

Figure 1: Load times of all Brightway packages (local machine, WASM-pyodide, WASM-xeus)

Figure 2: Calculation performance (graph traversal, matrix calculcation, same platforms as above)

Figure 3: WASM infrastructure overview

Figure 4: Tools for interactive webapps/dashboards



Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

This work has been supported by the Swiss Innovation Agency Innosuisse in the context of the WISER flagship project (PFFS-21-72). In addition, Michael P. Weinold gratefully acknowledges the support of the Swiss Study Foundation. The authors further gratefully acknowledge helpful conversations and contributions from the developers of [the Pyodide project](https://github.com/pyodide/), the [Emscripten Forge project](https://github.com/emscripten-forge), [the Jupyter Xeus project](https://github.com/jupyter-xeus) and [the JupyterLite project](https://github.com/jupyterlite). Michael Weinold gratefully acknowledges funding from the Swiss Innovation Agency Innosuisse through the WISER flagship project.

# References

