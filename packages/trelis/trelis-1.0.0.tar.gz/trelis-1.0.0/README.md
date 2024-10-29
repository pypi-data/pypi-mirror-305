# trelis

[![Github Actions Status](https://github.com/TrelisResearch/trelis-jupyter-assistant/workflows/Build/badge.svg)](https://github.com/TrelisResearch/trelis-jupyter-assistant/actions/workflows/build.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TrelisResearch/trelis-jupyter-assistant/main?urlpath=lab)


A JupyterLab Code Assistant

## Requirements

- JupyterLab >= 4.0.0
- Node >= 22.6
- Yarn

## Install

To install the extension, execute:

```bash
pip install trelis
```
to install with node and yarn (for example, in a remote GPU server like RunPod), first run:
```
import os
import subprocess

def check_node_yarn():
    # Check if Node.js is installed
    try:
        node_version = subprocess.check_output(["node", "--version"]).decode().strip()
        print(f"Node.js is installed: {node_version}")
    except FileNotFoundError:
        print("Node.js is not installed.")
        install_node()

    # Check if Yarn is installed
    try:
        yarn_version = subprocess.check_output(["yarn", "--version"]).decode().strip()
        print(f"Yarn is installed: {yarn_version}")
    except FileNotFoundError:
        print("Yarn is not installed.")
        install_yarn()

def install_node():
    print("Installing Node.js...")
    # Download Node.js binary (you can change the version if needed)
    os.system("curl -O https://nodejs.org/dist/v22.6.0/node-v22.6.0-linux-x64.tar.xz --silent")
    
    # Extract Node.js
    os.system("tar -xf node-v22.6.0-linux-x64.tar.xz --no-same-owner")
    
    # Add Node.js to the PATH for the current notebook session
    node_bin_path = os.path.abspath("node-v22.6.0-linux-x64/bin")
    os.environ['PATH'] = node_bin_path + ":" + os.environ['PATH']
    print(f"Node.js installed to {node_bin_path}")

    # Verify installation
    node_version = subprocess.check_output(["node", "--version"]).decode().strip()
    print(f"Node.js version: {node_version}")

def install_yarn():
    print("Installing Yarn...")
    # Install Yarn via script
    os.system("curl -o- -L https://yarnpkg.com/install.sh | bash")
    
    # Add Yarn to the PATH for the current notebook session
    yarn_bin_path = os.path.expanduser("~/.yarn/bin")
    os.environ['PATH'] = yarn_bin_path + ":" + os.environ['PATH']
    print(f"Yarn installed to {yarn_bin_path}")

    # Verify installation
    yarn_version = subprocess.check_output(["yarn", "--version"]).decode().strip()
    print(f"Yarn version: {yarn_version}")

# Run the check and installation process
check_node_yarn()
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall trelis
```

## Contributing (Private)

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

First:
```
conda create -n jupyterlab-ext --override-channels --strict-channel-priority -c conda-forge -c nodefaults jupyterlab=4 nodejs=20 git copier=9 jinja2-time
```
then:
```
conda activate jupyterlab-ext
```

Or just:
```
python -m venv jupyterlab-ext
source jupyterlab-ext/bin/activate
```
Then:
```
Then, run:
```
npm install -g yarn
yarn install
pip install -ve .
jupyter labextension develop --overwrite .
pip install jupyterlab
jlpm
jlpm build
jlpm watch
```
This will watch the source directory and allow you to run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
pip uninstall trelis
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `trelis-jupyter-assistant` within that folder.

### Testing the extension

#### Frontend tests

This extension is using [Jest](https://jestjs.io/) for JavaScript code testing.

To execute them, execute:

```sh
jlpm
jlpm test
```

#### Integration tests

This extension uses [Playwright](https://playwright.dev/docs/intro) for the integration tests (aka user level tests).
More precisely, the JupyterLab helper [Galata](https://github.com/jupyterlab/jupyterlab/tree/master/galata) is used to handle testing the extension in JupyterLab.

More information are provided within the [ui-tests](./ui-tests/README.md) README.

### Packaging the extension

See [RELEASE](RELEASE.md)
