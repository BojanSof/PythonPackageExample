# Python package example

This is a python package example.
It has the purpose of showing how to create packages with multiple modules and run unit tests on GitHub Actions.

## Building the wheel package

To build the wheel package, run `python -m build` from the root of the package project.
Ensure that `build` package is installed.
The wheel package can be found under `dist` folder.

## Installing wheel package

Wheel package can be installed by calling `pip install <package.whl>`.