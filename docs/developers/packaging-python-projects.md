# How to do a deployment of a python project

See [Python Packaging User Guide](https://packaging.python.org/en/latest/), [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/), [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) and [Is setup.py deprecated?](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/) documentation

## Quick tutorial

1- Creating the package files:

* Create/edit the `setup.py` (build script for setuptools) and or pyproject.toml (a configuration file used by packaging tools).

* Create/edit the `LICENSE` file (license text for your Python Package).

* create/edit the `README.md` file (used to generate the html summary you see at the bottom of projects).

* Note: We use the following file structure (your project name = example_pkg):

```
|──Git_Projects
|  ├──example_pkg
|  |  ├──example_pkg # All stuffs of the example_pkg  are there (in /Git_Projects/example_pkg/example_pkg/)
|  ├──setup.py
|  ├──LICENSE
|  ├──README.md
```

2- Make sure you have the latest versions of setuptools, wheel, twine and build installed:

```bash
pip3 install --user --upgrade setuptools wheel twine build
```

3- Generating distribution archives:

Deprecated:
<strike>

```
python3 setup.py sdist bdist_wheel # From the same directory where setup.py is located
```

</strike>

The recommendation is to use:

```
python -m build # From the same directory where setup.py and pyproject.toml are located
```

* Note1: Make sure you have nothing in the `/Git_Projects/example_pkg/dist/` folder (or that it does not exist) before launching the previous command.

* Note2: The previous command will generate `/Git_Projects/example_pkg/dist/`, `/Git_Projects/example_pkg/build/` and `/Git_Projects/example_pkg/example_pkg.egg-info/` directories.

4- Uploading the distribution archives:

On Test PyPI:

```bash
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* # From /Git_Projects/example_pkg/
```

On the real Python Package Index:

```bash
python3 -m twine upload dist/* # From /Git_Projects/example_pkg/
```

5- To avoid problems in the future, delete the `/Git_Projects/example_pkg/dist/`, `/Git_Projects/example_pkg/build/` and `/Git_Projects/example_pkg/example_pkg.egg-info/` directories.
