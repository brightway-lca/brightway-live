# FAQ

## Is the kernel stuck?

Sometimes it can take a while for a Jupyter Notebook cell to execute completely. This is indicated by a `*` in the cell number: `[*]` instead of `[1]`. If you see this, wait a few seconds and see if the cell completes. If it doesn't, you can check the JavaScript console of your browser:

::::{tab-set}

:::{tab-item} Google Chrome

```
View > Developer > JavaScript Console
```

:::

:::{tab-item} Safari

```
Develop > Show JavaScript Console
```

:::

:::{tab-item} Mozilla Firefox

```
Tools > Browser Tools > Browser Console
```

:::

:::{tab-item} Netscape Navigator

1. Build a time machine
2. Travel to the 2020s
3. Use a modern web browser

:::

::::

A console output of the kind

```
Loading scipy, numpy, openblas, lxml, xlrd, tqdm, pandas,
python-dateutil, pytz, certifi, idna, peewee, cffi, pycparser,
wrapt, typing-extensions, setuptools, distutils, pyparsing
```

indicates that the kernel is still working. Just wait a little.

:::{note}
If you're installing packages into the `jupyterlite-pyodide-kernel` using `micropip`, you should make sure you have a stable internet connection. Otherwise, executing the installation cell might take a while.
:::