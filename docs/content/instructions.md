# Instructions

## Resetting the JupyterLite Environment

Currently, the interface of the JupiterLite environment does not provide a way to reset the environment.

```{admonition} Related Issues
:class: note
https://github.com/jupyterlite/jupyterlite/issues/9
```

This means that the environment must be reset manually. Usually, all data is stored in the browser's IndexedDB. You can reset the environment in your browser by following these steps:

Google Chrome:

```
Developer > Developer Tools > Application > Storage > Indexed DB > JupyterLite Storage > Delete Database
```

Mozilla Firefox:

```
Tools > Page Info > Permissions > Maintain Offline Storage > Clear Storage
```