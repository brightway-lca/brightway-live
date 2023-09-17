# Brightway Live

```{button-link} https://live.brightway.dev/
:color: primary
:expand:
:tooltip: "Be sure to use Brightway Live as directed by your healthcare provider."
{octicon}`rocket;1em;white` Go Live Now!
```

## What is Brightway Live?

Brightway Live is a Python-based development environment [^1] that runs entirely in the browser. This means that it is independent of the hardware, the operating system or the local Python environment of the user. It is powered by WebAssembly [^2] and JupyterLite [^3]. It was built by [Michael Weinold](https://github.com/michaelweinold) after learning about the possibilities of Python in WebAssembly at the EuroSciPy conference in Basel in 2022.

## What can I do with Brightway Live?

At the moment, you can play around with it. You can load brightway packages (eg. `bw2io`, `bw2calc`, `bw2data` and `bw2analyzer`) and use them in a Jupyter Notebook or in a Python console. In the long run, you will be able to use this to teach life-cycle assessment with Brightway at scale. You will not need to worry about installation or setup of the software. You will not need to worry about the different hardware and operating systems that your students bring to class. You will not need to worry about setting up a JupyterHub server and the associated overhead.

```{eval-rst}
.. replite::
   :kernel: pyodide
   :height: 200px
   :prompt: Go Live!
   :prompt_color: #dc3545

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

[^1]: A development environment is the collection of processes and tools that are used to develop the source code for a program or software product.
[^2]: [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly) (often abbreviated "WASM") is _a binary instruction format and a runtime environment_. This means it acts as a "virtual machine for the web. Unlike high-level programming languages like JavaScript or Python, which are typically interpreted by a runtime environment, WebAssembly code is compiled to a binary format. This binary code is the same regardless of the user's device or operating system.
[^3]: [JupyterLite](https://jupyterlite.readthedocs.io) is a version of [JupyterLab](https://jupyter.org), which is optimized for the browser.

```{toctree}
---
hidden:
maxdepth: 1
---
Go Live <https://live.brightway.dev/>
content/instructions
content/limitations
content/faq
```
