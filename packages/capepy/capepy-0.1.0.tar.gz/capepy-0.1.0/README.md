# CAPE Python Utilities

This repository contains a collection of utility functions useful for developing
on and interacting with the CAPE infrastructure. It basically provides an
abstraction layer over the core concepts such as ETL (extract, transform, load)
jobs and analysis pipelines that allow interacting with these types of
structures without worrying about the implementation details of each.

## Installation

```sh
pip install git+https://github.com/cape-ph/capepy.git
```

## Development

Install dependencies with

```sh
poetry install
```

We have Poetry set up to install into a virtual environment within the
repository as `.venv`. You can either use the Poetry shell feature or activate
this environment directly.

```sh
# Activate the Poetry shell
poetry shell
# Activate the virtual environment directly
source .venv/bin/activate
```
