# IllumiDesk Jupyter Proxy for VS Code

[VS Code](https://code.visualstudio.com/) is one of the more popular IDE's. `VS Code` has become a legitimate alternative for data scientists and data analysts thanks in part to its native support for `Jupyter Notebooks` and third party extensions that enhance user productivity. This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template).

## Installation

```bash
pip install illumidesk-vscode-proxy
```

## Requirements

### Install Code Server

The [`code-server`](https://github.com/cdr/code-server) tool webifies `VS Code`. This package is intented to run in environments that run Jupyter Notebooks within a containerized environment such as `docker`.

### Install Jupyter Notebook

This extension relies on the Jupyter Notebook to run. [Refer to Jupyter's official documentaion](https://jupyter.org/install) for installation instructions.

### Install illumidesk-vscode-proxy

Install the package with pip:

```
pip install illumidesk-vscode-proxy
```

## Why?

This setup launches VS Code in a new browser tab. Refer to [`jupyter-server-proxy`'s](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-from-python-packages) documentation for additional configuration settings.

## Attributions

- [`jupyter-vscode-proxy`](https://github.com/betatim/vscode-binder/tree/master/jupyter_vscode_proxy)
- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
